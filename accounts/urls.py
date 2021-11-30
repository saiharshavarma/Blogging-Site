from django.urls import path
from . import views

urlpatterns = [
    path('register_customer', views.register, name='register_customer'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]