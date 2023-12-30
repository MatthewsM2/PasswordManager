from django.urls import path
from PassManager import views

urlpatterns = [
        path('', views.hello_world, name='hello_world'),
        ]
