from django.shortcuts import render
from django.http import Http404
import json
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
import datetime

def index(request,date):
	return render(request,'time_wise/index.html',{'date':date})

def calender(request):
	content = open('C:\Users\user\Desktop\IOTProject\smart_notifier\static\scraped_data.txt').read()
	print(content)
	date = datetime.datetime.now().date();
	time = datetime.datetime.now().time();
	return render(request, 'calender/calender.html',{'date':date,'time':time , 'content':content})