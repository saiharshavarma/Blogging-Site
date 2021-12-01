from django.urls import path
from . import views

urlpatterns = [
    path('register_customer', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile/<slug:profile_slug>', views.profile, name='profile'),
    path('blog-delete/<slug:the_slug>', views.profile, name='blog_delete'),
]