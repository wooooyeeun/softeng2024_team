from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Category, Tag
from django.core.exceptions import PermissionDenied
from django.utils.text import slugify
import random
import csv
import os

def index(request):
    images = [
        {'file': 'jeonju.png', 'alt': '여수 밤바다', 'title': '여수 밤바다~', 'description': '낭만적인 밤바다'},
        {'file': 'jeonju.png', 'alt': '전주 한옥마을', 'title': '전주 한옥마을', 'description': '우와~ 한옥마을!'},
        {'file': 'jeonju.png', 'alt': '순천', 'title': '순천', 'description': '순천순천'},
    ]
    random.shuffle(images)
    images = images[:3]

    options = [
        {'name': '지역별', 'image': 'region.jpg', 'link': '/region/'},
        {'name': '테마별', 'image': 'theme.jpg', 'link': '/theme/'},
        {'name': '계절별', 'image': 'season.jpg', 'link': '/season/'},
    ]
    return render(request, 'travel_page/index.html', {'images': images, 'options': options})

def load_region_data(csv_file_path):
    data = {'restaurants': {}, 'touristSpots': {}, 'attractions': {}}
    try:
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                category = row['category']
                region = row['region']
                name = row['name']
                image = row['image']

                # 데이터 구조 확인
                if category not in data:
                    continue
                if region not in data[category]:
                    data[category][region] = []

                data[category][region].append({
                    'name': name,
                    'image': image,
                })
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return data

# 지역별 페이지
def region(request):
    region_csv_path = os.path.join('travel_page/static/travel_page/data', 'region_data.csv')
    travel_csv_path = os.path.join('travel_page/static/travel_page/data', 'travel_data.csv')

    jeonbuk = []
    jeonnam = []
    category_data = load_region_data(travel_csv_path)

    try:
        with open(region_csv_path, encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['province'] == '전라북도':
                    jeonbuk.append({'name': row['region'], 'image': row['image']})
                elif row['province'] == '전라남도':
                    jeonnam.append({'name': row['region'], 'image': row['image']})
    except Exception as e:
        print(f"Error reading region_data.csv: {e}")

    return render(request, 'travel_page/region.html', {
        'jeonbuk': jeonbuk,
        'jeonnam': jeonnam,
        'category_data': category_data,
    })

def detail_view(request, name):
    travel_csv_path = os.path.join('travel_page/static/travel_page/data', 'travel_data.csv')
    travel_data = []
    try:
        with open(travel_csv_path, encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                travel_data.append(row)
    except Exception as e:
        print(f"CSV 파일 읽기 오류: {e}")

    detail = next((item for item in travel_data if item['name'] == name), None)
    if not detail:
        return render(request, '404.html')  # 데이터가 없을 경우 404 페이지
    return render(request, 'travel_page/region_detail.html', {'detail': detail})

class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            response = super(PostCreate, self).form_valid(form)

            tags_str = self.request.POST.get('tags_str')
            if tags_str:
                tags_str = tags_str.strip()

                tags_str = tags_str.replace(',', ';')
                tags_list = tags_str.split(';')

                for t in tags_list:
                    t = t.strip()
                    tag, is_tag_created = Tag.objects.get_or_create(name=t)
                    if is_tag_created:
                        tag.slug = slugify(t, allow_unicode=True)
                        tag.save()
                    self.object.tags.add(tag)

            return response

        else:
            return redirect('/blog/')

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category']

    template_name = 'blog/post_update_form.html'

    def get_context_data(self, **kwargs):
        context = super(PostUpdate, self).get_context_data()
        if self.object.tags.exists():
            tags_str_list = list()
            for t in self.object.tags.all():
                tags_str_list.append(t.name)
            context['tags_str_default'] = '; '.join(tags_str_list)

        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def form_valid(self, form):
        response = super(PostUpdate, self).form_valid(form)
        self.object.tags.clear()

        tags_str = self.request.POST.get('tags_str')
        if tags_str:
            tags_str = tags_str.strip()
            tags_str = tags_str.replace(',', ';')
            tags_list = tags_str.split(';')

            for t in tags_list:
                t = t.strip()
                tag, is_tag_created = Tag.objects.get_or_create(name=t)
                if is_tag_created:
                    tag.slug = slugify(t, allow_unicode=True)
                    tag.save()
                self.object.tags.add(tag)

        return response

class PostList(ListView):
    model = Post
    ordering = '-pk'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(
        request,
        'blog/post_list.html',
        {
            'post_list': post_list,
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),
            'category': category,
        }
    )

def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()

    return render(
        request,
        'blog/post_list.html',
        {
            'post_list': post_list,
            'tag': tag,
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),
        }
    )



