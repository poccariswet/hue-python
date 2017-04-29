#!/usr/bin/python
# coding: utf-8
from phue import Bridge
#電源OFF
b = Bridge('192.168.2.2')

# If the app is not registered and the button is not pressed,
# press the button and call connect() (this only needs to be run a single time)
b.connect()

# Turn lamps off
b.set_light([1,2,3], 'on', False)
