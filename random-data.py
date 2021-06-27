import random

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
#elif metricType == 'NoiseLevel':
else:
  value = random.randint(6,7)  

print(collectorValue + ' ' + metricType + ' ' + str(value) )
