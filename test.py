#!/usr/bin/python
# coding: utf-8
from phue import Bridge
import json, urllib2

b = Bridge('192.168.2.2')
b.connect()

url = 'http://dokusyodebokin.rulez.jp/earthquake/now/?prefecture=%E7%A6%8F%E5%B3%B6'
try:
    r = urllib2.urlopen(url)
    root = json.loads(r.read())

    # print root[0]['doserate'] #[doserate] ：空間線量率[nGy/h]
    t = root[0]['doserate']
    print t
finally:
    r.close()

if t >= 200:
    b.set_light([1,2,3], 'on', True)
    b.set_light([1,2], 'bri', 10)
    lights = b.get_light_objects()
    lights[2].xy = [0, 0.7]
    lights[0].xy = [0, 1]
    lights[1].xy = [0, 1]