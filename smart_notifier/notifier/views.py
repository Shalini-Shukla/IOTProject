from django.shortcuts import render
from django.http import Http404
import json
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
import datetime

def index(request,date):
	month_date = 'November '+date;
	print(month_date) 
	content = open('C:\\Users\\Samrat\\Desktop\\IOTProject\\smart_notifier\\static\\data\\'+month_date+'.txt').read()
	events = content.split('\n')
	del[events[len(events)-1]]
	print(events)
	return render(request,'time_wise/index.html',{'date':date,'events':events})

def calender(request):
	content = open('C:\Users\Samrat\Desktop\IOTProject\smart_notifier\static\scraped_data.txt').read()
	eventsAndDate = content.split('\n');
	events = [''] * (len(eventsAndDate)/2)
	date_event = [''] * (len(eventsAndDate)/2)
	for i in range(0,len(eventsAndDate)/2):
		events[i] = eventsAndDate[i]
	for i in range(len(eventsAndDate)/2,len(eventsAndDate)-1):
		# print(i-(len(eventsAndDate)/2))
		date_event[i-(len(eventsAndDate)/2)] = eventsAndDate[i]
	# print(events,date_event)
	for i in range(0,len(events)):
		f = open('C:\\Users\\Samrat\\Desktop\\IOTProject\\smart_notifier\\static\\data\\'+date_event[i]+'.txt','w')
		f.write(events[i]+'\n')
	date = datetime.datetime.now().date();
	time = datetime.datetime.now().time();
	return render(request, 'calender/calender.html',{'date':date,'time':time , 'content':content})