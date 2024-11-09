from django.urls import path
from . import views
app_name = "blog"

urlpatterns = [
    path('blog/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('blog/', views.PostList.as_view(), name='post_list'),
]

