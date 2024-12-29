from django.urls import path
from . import views

app_name = "todo_app"

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('delete-list/<int:list_id>/', views.delete_todo_list, name='delete_todo_list'),
    path('add-item/<int:list_id>/', views.add_todo_item, name='add_todo_item'),
    path('delete-item/<int:item_id>/', views.delete_todo_item, name='delete_todo_item'),
    path('update-color/<int:list_id>', views.update_color, name='update_color'),
]