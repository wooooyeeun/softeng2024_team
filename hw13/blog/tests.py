
from django.test import TestCase, Client

# from django.test import TestCase, Client
# from bs4 import BeautifulSoup
# from django.contrib.auth.models import User
# from .models import Post, Category, Tag
#
# class TestView(TestCase):
#     def setUp(self):
#         self.client = Client()
#
#         self.user_pizza = User.objects.create_user(username='pizza', password='cheating1004')
#         self.user_hamburger = User.objects.create_user(username='hamburger', password='mcdonalds12')
#
#         self.category_delicious = Category.objects.create(name='delicious', slug='delicious')
#         self.category_me = Category.objects.create(name='me', slug='me')
#         self.tag_yummy = Tag.objects.create(name='yummy', slug='yummy' )
#         self.tag_hmm = Tag.objects.create(name='hmm', slug='hmm')
#
#         self.post_007=Post.objects.create(
#             title='맥도날드',
#             content='베토디',
#             category=self.category_delicious,
#             author=self.user_hamburger
#         )
#         self.post_007.tags.add(self.tag_yummy)
#
#     def category_card_test(self, soup):
#         categories_card = soup.find('div', id='categories-card')
#         self.assertIn('Categories', categories_card.text)
#         self.assertIn(f'{self.category_delicious.name} ({self.category_delicious.post_set.count()})', categories_card.text)
#         self.assertIn(f'미분류 (1)', categories_card.text)
#
#     def test_category_page(self):
#         response = self.client.get(self.category_delicious.get_absolute_url())
#         self.assertEqual(response.status_code, 200)
#
#         soup = BeautifulSoup(response.content, 'html.parser')
#         self.navbar_test(soup)
#         self.category_card_test(soup)
#
#         self.assertIn(self.category_delicious.name, soup.h1.text)
#
#         main_area = soup.find('div', id='main-area')
#         self.assertIn(self.category_delicious.name, main_area.text)
#         self.assertIn(self.post_007.title, main_area.text)
#         self.assertIn(self.post_008.title, main_area.text)
#
#     def test_post_list(self):
#         self.assertEqual(Post.objects.count(), 4)
#
#         response = self.client.get('/blog/')
#         self.assertEqual(response.status_code, 200)
#         soup = BeautifulSoup(response.content, 'html.parser')
#
#         self.navbar_test(soup)
#         self.category_card_test(soup)
#
#         main_area = soup.find('div', id='main_area')
#         self.assertNotIn('아직 게시물이 없습니다', main_area.text)
#
#         post_006_card = main_area.find('div', id='post-1')
#         self.assertIn(self.post_006.title, post_006_card.text)
#         self.assertIn(self.post_006.category.name, post_006_card.text)
#         self.assertNotIn(self.tag_yummy, post_006_card.text)
#         self.assertIn(self.tag_hmm, post_006_card.text)
#
#         post_007_card = main_area.find('div', id='post-2')
#         self.assertIn(self.post_007.title, post_007_card.text)
#         self.assertIn(self.post_007.category.name, post_007_card.text)
#         self.assertIn(self.tag_yummy, post_007_card.text)
#         self.assertNotIn(self.tag_hmm, post_007_card.text)
#
#         post_009_card = main_area.find('div', id='post-4')
#         self.assertIn('미분류', post_009_card.text)
#         self.assertIn(self.post_009.title, post_009_card.text)
#         self.assertNotIn(self.tag_yummy, post_009_card.text)
#         self.assertNotIn(self.tag_hmm, post_009_card.text)
#
#         self.assertIn(self.user_pizza.username.upper(), main_area.text)
#         self.assertIn(self.user_hamburger.username.upper(), main_area.text)
#
#         Post.objects.all().delete()
#         self.assertEqual(Post.objects.count(), 0)
#         response = self.client.get('/blog/')
#         soup = BeautifulSoup(response.content, 'html.parser')
#
#         main_area = soup.find('div', id='main_area')
#         self.assertIn('아직 게시물이 없습니다', main_area.text)
#
#
#     def test_post_detail(self):
#         self.assertEqual(self.post_001.get_absolute_url(), '/blog/1/')
#
#         response = self.client.get(self.post_001.get_absolute_url())
#         self.assertEqual(response.status_code, 200)
#         soup = BeautifulSoup(response.content, 'html.parser')
#
#         self.navbar_test(soup)
#
#         self.category_card_test(soup)
#
#         self.assertIn(self.post_001.title, soup.title.text)
#
#         main_area = soup.find('div', id='main_area')
#         post_area = main_area.find('div', id ='post-area')
#         self.assertIn(self.post_001.title, post_area.text)
#         self.assertIn(self.category_delicious.name, post_area.text)
#
#         self.assertIn(self.user_hamburger.username.upper(), post_area.text)
#         self.assertIn(self.post_001.content, post_area.text)

