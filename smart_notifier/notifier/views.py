from django.shortcuts import render
from django.http import Http404
import json
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
import datetime
import os.path

def index(request,date):
	if os.path.isfile('C:\\Users\\Samrat\\Desktop\\IOTProject\\smart_notifier\\static\\Entered_Data\\'+date+'.txt'):
		content = open('C:\\Users\\Samrat\\Desktop\\IOTProject\\smart_notifier\\static\\Entered_Data\\'+date+'.txt').read()
	# print(content)
	else:
		content=""
	events = content.split('\n')
	del(events[len(events)-1])
	# print(events)
	dict = {}
	for event in events:
		data =  event.split(',')
		time = data[2].split('-')[0]
		if int(time[1])%2 != 0:
			s = list(time)
			s[1] = str(int(time[1])-1)
			time = "".join(s)
			# print(time)
		if time not in dict:
			dict[time] = [data]
		else:
			dict[time] = dict[time] + [data]
		# print(dict)
	# print('----',dict)
	return render(request,'time_wise/index.html',{'date':date,'events':dict})

def calender(request):
	content = open('C:\Users\Samrat\Desktop\IOTProject\smart_notifier\static\scraped_data.txt').read()
	print(content)
	date = datetime.datetime.now().date();
	time = datetime.datetime.now().time();
	return render(request, 'calender/calender.html',{'date':date,'time':time , 'content':content})

def writedata(request,date):
	# print('Hi')
	final_string = request.GET['data']
	content = open('C:\\Users\\Samrat\\Desktop\\IOTProject\\smart_notifier\\static\\Entered_Data\\'+date+'.txt',"a+")
	content.write(final_string+'\n')
	date= final_string.split(",")[0]
	print(final_string)
	return render(request,'time_wise/index.html',{'date':date})