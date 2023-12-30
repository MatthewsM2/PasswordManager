from django.urls import path
from PassManager import views

urlpatterns = [
        path('', views.hello_world, name='hello_world'),
        path('register', views.register, name='register'),
        path('login', views.login, name='login'),
        path('dashboard', views.dashboard, name='dashboard'),
        ]
