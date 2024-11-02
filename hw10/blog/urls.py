from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('blog/<int:pk>/', views.single_post_page),
    path('blog/', views.index, name='index'),
    path('about/', views.about_page, name='about'),
    path('', views.landing_page, name='landing_page'),
    path("blog_1/", views.blog_list, name='blog_list'),
    path("portfolio/", views.portfolio_page, name='portfolio_page'),
]

