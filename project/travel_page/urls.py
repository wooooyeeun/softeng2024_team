from django.urls import path
from . import views

app_name = "travel_page"

urlpatterns = [
    path('', views.index, name='index'),  # 메인 페이지: 지역별/카테고리별 선택
    path('region/', views.region, name='region'),
    path('detail/<str:name>/', views.detail_view, name='detail_view'),
    path('update_post/<int:pk>/', views.PostUpdate.as_view(), name='update_post'),
    path('create_post/', views.PostCreate.as_view(), name='create_post'),
    path('tag/<str:slug>/', views.tag_page, name='tag_page'),
    path('category/<str:slug>/', views.category_page, name='category_page'),
    path('post_list/', views.PostList.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
]