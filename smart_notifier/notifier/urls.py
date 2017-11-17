from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
	# url(r'(?P<final_string>[0-9]([,]+)([a-z]+)([,]+)([0-9-]+)([,]+))',views.writedata , name='writedata'),
	url(r'^(?P<date>[0-9]+)/writedata', views.writedata,name='writedata'),
	url(r'^(?P<date>[0-9]+)/delete', views.delete,name='delete'),
	url(r'^(?P<date>[0-9]+)/', views.index , name='index'),
	url(r'^calender$', views.calender , name='calender'),    
]