import requests
import os

payload = {'collector': 'raspberry-kw02','metricType': 'Humidity','value': '40.0'}
#r = requests.post( url = 'http://192.168.0.101:8080/metrics', json = payload)
r = requests.post( url = os.environ['ENDPOINT'], json = payload)
print (r.content)
