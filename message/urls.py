from django.conf.urls import url                                                                                                                                                         
from . import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [ 
    url('', views.index, name="home"),
]
