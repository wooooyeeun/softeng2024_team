from django.urls import path
from . import views

app_name = "travel_page"

urlpatterns = [
    path('', views.index, name='index'),  # 메인 페이지: 지역별/카테고리별 선택
    path('region/', views.region, name='region'),
    path('detail/<str:name>/', views.detail_view, name='detail_view'),
]