from django.urls import path
from . import views

app_name = "community"

urlpatterns = [
    path('update_post/<int:pk>/', views.PostUpdate.as_view(), name='update_post'),
    path('create_post/', views.PostCreate.as_view(), name='create_post'),
    path('tag/<str:slug>/', views.tag_page, name='tag_page'),
    path('category/<str:slug>/', views.category_page, name='category_page'),
    path('', views.PostList.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
]

