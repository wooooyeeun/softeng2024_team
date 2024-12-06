from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('create_post/', views.PostCreate.as_view()),
    path('category/<str:slug>/', views.category_page),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('', views.PostList.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),

]
