#!/usr/bin/python
# coding: utf-8
from phue import Bridge
import json, urllib2

b = Bridge('192.168.2.2')
b.connect()


b.set_light([1,2,3], 'on', True)
b.set_light([1,2,3], 'bri', 10)
lights = b.get_light_objects()
lights[0].xy = [1, 1]
lights[1].xy = [1, 1]
lights[2].xy = [0.3, 0.3]
