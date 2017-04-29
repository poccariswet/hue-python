#!/usr/bin/python
# coding: utf-8
from phue import Bridge
# import random
import json, urllib2
import time


b = Bridge('192.168.2.2')

# If the app is not registered and the button is not pressed,
# press the button and call connect() (this only needs to be run a single time)
b.connect()

# b.set_light([1,2,3], 'on', False) #lights OFF!

#ここから！!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=070030'
try:
    r = urllib2.urlopen(url)
    root = json.loads(r.read())
    print 'title=' + root['title']
    description = root['description']
    print 'publicTime=' + description['publicTime']

    forecasts = root['forecasts']
    print '    dateLabel=' + forecasts[0]['dateLabel'] + ',telop=' + forecasts[0]['telop'] + ',date=' + forecasts[0]['date']
    if forecasts[0]['telop']==u'晴時々雨':
        b.set_light([1,2], 'on', True)
        b.set_light([1,2], 'bri', 10)
        # b.set_light([1,2,3] 'bri', 10)
        lights = b.get_light_objects()
        lights[0].xy = [1, 1]
        time.sleep(0.5)
        lights[0].xy = [0.1, 0]
        time.sleep(0.5)
        lights[0].xy = [1, 1]
        time.sleep(0.5)
        lights[0].xy = [0.1, 0]
        time.sleep(0.5)
        lights[0].xy = [1, 1]
        time.sleep(0.5)
        lights[0].xy = [0.1, 0]
        time.sleep(0.5)
        lights[0].xy = [1, 1]
        time.sleep(0.5)
        lights[0].xy = [0.1, 0]
        time.sleep(0.5)
        lights[0].xy = [1, 1]
        time.sleep(0.5)
        lights[0].xy = [0.1, 0]
        time.sleep(0.5)
        lights[0].xy = [1, 1]
        time.sleep(0.5)
        lights[0].xy = [0.1, 0]
finally:
    r.close()
#ここまで!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
