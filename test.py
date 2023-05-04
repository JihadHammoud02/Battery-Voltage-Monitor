import requests
import json
import urllib
import time



def dataAnalyze():
  url="https://api.thingspeak.com/channels/2092123/fields/1.json?api_key=4QZG4S439LLU2ZS5&results=5000"
  request2=requests.get(url).content
  jsonFile=json.loads(request2)
  average_consumption=0
  consumption=[]
  for feed in jsonFile['feeds'][50:100]:
    if feed['field1']!=-1:
        consumption.append({feed['created_at']:feed['field1']})
        average_consumption+=int(feed['field1'])
  print(average_consumption)
  average_consumption=average_consumption/50
  print(consumption)
  print(average_consumption)
    

dataAnalyze()
