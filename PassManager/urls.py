from django.urls import path
from PassManager import views

urlpatterns = [
        # path('', views.hello_world, name='home'),
        path('register', views.register, name='register'),
        path('', views.login, name='login'),
        path('login', views.login, name='login'),
        path('dashboard', views.dashboard, name='dashboard'),
        path('entry-get', views.getEntryDetails, name='entry-get'),
        path('del/<int:id>',views.deleteEntry, name='delete'),
        path('logout',views.logout, name='logout'),
        ]
