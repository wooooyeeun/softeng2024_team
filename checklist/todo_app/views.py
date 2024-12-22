from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import ToDoList, ToDoItem


def todo_list(request):
    lists = ToDoList.objects.prefetch_related('items')
    if request.method == 'POST':
        if 'new_list' in request.POST:
            title = request.POST.get('title')
            if title:
                ToDoList.objects.create(title=title)
        elif 'delete_list' in request.POST:
            list_id = request.POST.get('list_id')
            todo_list = get_object_or_404(ToDoList, id=list_id)
            todo_list.delete()
        elif 'color' in request.POST:
            list_id = request.POST.get('list_id')
            todo_list = get_object_or_404(ToDoList, id=list_id)
            todo_list.color = request.POST.get('color', '#000000')
            todo_list.save()
        return redirect('todo_list')
    return render(request, 'todo_list.html', {'lists': lists})

def add_todo_item(request, list_id):
    todo_list = get_object_or_404(ToDoList, id=list_id)
    if request.method == 'POST':
        subtitle = request.POST.get('subtitle')
        if subtitle:
            ToDoItem.objects.create(list=todo_list, subtitle=subtitle)
    return redirect('todo_list')

def delete_todo_item(request, item_id):
    item = get_object_or_404(ToDoItem, id=item_id)
    item.delete()
    return redirect('todo_list')

def delete_todo_list(request, list_id):
    todo_list = get_object_or_404(ToDoList, id=list_id)
    todo_list.delete()
    return redirect('todo_list')


def update_color(request, list_id):
    todo_list = get_object_or_404(ToDoList, id=list_id)
    if request.method == 'POST':
        new_color = request.POST.get('color', '#000000')
        todo_list.color = new_color
        todo_list.save()
        return redirect('todo_list')




def toggle_item(request, item_id):
    item = get_object_or_404(ToDoItem, id=item_id)
    item.is_checked = not item.is_checked
    item.save()
    return JsonResponse({'is_checked': item.is_checked})
# Create your views here.
