from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('tag/<str:slug>/', views.tag_page, name='tag_page'),
    path('category/<str:slug>/', views.category_page, name='category_page'),
    path('', views.PostList.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
]
