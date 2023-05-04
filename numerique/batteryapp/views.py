import requests
import json
import urllib
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
import time


buffer=[]
last_updates_index=0

def show_perc(request):
  url="https://api.thingspeak.com/channels/2092123/fields/1.json?api_key=4QZG4S439LLU2ZS5&results=200"
  request2=requests.get(url).content
  jsonFile=json.loads(request2)
  percentage=jsonFile['feeds'][-1]['field1']
  print(jsonFile)
  return render(request, 'batteryapp\dashboard.html', {'value': percentage})


def getThreshold(request):

  threshold=request.POST.get('threshold')
  
  url='https://api.thingspeak.com/update?api_key=K2H3AN59ZTH5KC3H&field1='+threshold
  post_request=urllib.request.urlopen(url)
  print(post_request.getcode())
  print(threshold)
  return HttpResponseRedirect("/")



def dataAnalyze():
  url="https://api.thingspeak.com/channels/2092123/fields/1.json?api_key=4QZG4S439LLU2ZS5&results=200"


def index(request):
  return HttpResponse("Hello, you're at the sensors4G index!")