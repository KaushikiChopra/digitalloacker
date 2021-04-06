from django.contrib import admin
from django.urls import path, include
from Your_locker import views
from django.conf.urls import url
from .views import *




app_name = 'Your_locker'

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home ,name="home"),
    path("logout", views.logoutuser ,name="logoutuser"),
    path("upload" , views.upload , name="upload"),
    url("YourFile", views.Homes, name="Homes"),
    url('^home/(?P<home_id>\d+)/$', views.detail , name='detail'),
   # url("home/locker" , views.HomeCreate.as_view(), name="home_locker"),


    
]
