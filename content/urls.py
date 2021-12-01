from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog_upload', views.blog_upload, name='uploading_blogs'),
    path('blogs/<slug:the_slug>', views.blog_details, name='blog_details'),
]
