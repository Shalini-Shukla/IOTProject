from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^(?P<date>[0-9]+)/', views.index , name='index'),
    url(r'^calender/', views.calender , name='calender'),
]
