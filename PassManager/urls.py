from django.urls import path
from PassManager import views

urlpatterns = [
        # path('', views.hello_world, name='home'),
        path('register', views.register, name='register'),
        path('', views.login, name='login'),
        path('login', views.login, name='login'),
        path('dashboard', views.dashboard, name='dashboard'),
        path('logout',views.logout, name='logout'),
        ]
