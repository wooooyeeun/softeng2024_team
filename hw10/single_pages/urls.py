from django.urls import path

from . import views

app_name = "single_pages"

urlpatterns = [
    path('about/', views.about_page, name='about'),
    path('', views.landing_page, name='landing_page'),
    path("blog_page/", views.blog_list, name='blog_list'),
    path("portfolio/", views.portfolio_page, name='portfolio_page'),
]

