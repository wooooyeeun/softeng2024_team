from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = "blog"

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)