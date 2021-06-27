import schedule
import time
import random
import requests 
import os

def generate_random_metric():
    collectorString = ['raspberry-kw01', 'raspberry-kw02'] 
    collectorValue = random.choice(collectorString)

    metricTypeString = ['Luminosity','Temperature','Humidity','NoiseLevel']
    metricType = random.choice(metricTypeString)

    if metricType == 'Luminosity':
        value = random.randint(0,1)
    elif metricType == 'Temperature':
        value = random.randint(2,3)
    elif metricType == 'Humidity':
        value = random.randint(4,5)
    else:
        value = random.randint(6,7)
    payload = {'collector': collectorValue,'metricType': metricType,'value': str(value)}
    return payload      

def send_metric():
    payload = generate_random_metric()
    #r = requests.post( url = 'http://192.168.0.101:8080/metrics', json = payload)
    r = requests.post( url = os.environ['ENDPOINT'], json = payload)
    print (r.content)

schedule.every(10).seconds.do(send_metric)

while True:
        schedule.run_pending()
