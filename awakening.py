#!/usr/bin/python
# coding: utf-8
from phue import Bridge
import time
#電源オン
b = Bridge('192.168.2.2')

# If the app is not registered and the button is not pressed,
# press the button and call connect() (this only needs to be run a single time)
b.connect()

# Turn lamps on
# b.set_light([1,2], 'on', True)
# b.set_light([1,2], 'bri', 10)

lights = b.get_light_objects()
b.set_light([1,2], 'bri', 10)
lights[2].xy = [0.5, 0.5]
for i in range(5):
    lights[0].xy = [1, 1]
    lights[1].xy = [1, 1]
    time.sleep(0.5)
    lights[0].xy = [0.0, 0.0]
    lights[1].xy = [0.0, 0.0]
    time.sleep(0.5)


b.set_light([1,2,3], 'on', False)
time.sleep(3.0)
b.set_light([1,2], 'on', True)
lights[0].xy = [1, 0]
lights[1].xy = [1, 0]
b.set_light([1,2], 'bri', 254)
