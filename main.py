#!/usr/bin/python
# -*- coding: utf8 -*-import sys
import Tkinter
from phue import Bridge
import random
import json, urllib2
import time
import urllib2
from bs4 import BeautifulSoup


b = Bridge('192.168.2.2')
b.connect()

root = Tkinter.Tk()
root.title(u"Software Title")
root.geometry("400x300")

def Tenki(event):
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=070030'
    try:
        r = urllib2.urlopen(url)
        root = json.loads(r.read())
        print 'title=' + root['title']
        description = root['description']
        print 'publicTime=' + description['publicTime']

        forecasts = root['forecasts']
        print '    dateLabel=' + forecasts[0]['dateLabel'] + ',telop=' + forecasts[0]['telop'] + ',date=' + forecasts[0]['date']
        if forecasts[0]['telop']==u'晴れ':
            b.set_light([1,2,3], 'on', True)
            b.set_light([1,2], 'bri', 80)
            lights = b.get_light_objects()
            lights[2].xy = [0, 0.7]
            lights[0].xy = [0.9, 0]
            lights[1].xy = [0.9, 0]

        elif forecasts[0]['telop']==u'雨':
            b.set_light([1,2,3], 'on', True)
            b.set_light([1,2], 'bri', 80)
            lights = b.get_light_objects()
            lights[2].xy = [0, 0.7]
            lights[0].xy = [0, 0]
            lights[1].xy = [0, 0]

        elif forecasts[0]['telop']==u'曇り':
            b.set_light([1,2,3], 'on', True)
            b.set_light([1,2], 'bri', 80)
            lights = b.get_light_objects()
            lights[2].xy = [0, 0.7]
            lights[0].xy = [0.3, 0.3]
            lights[1].xy = [0.3, 0.3]

        elif forecasts[0]['telop']==u'晴時々曇':
            b.set_light([1,2,3], 'on', True)
            b.set_light([1,2,3], 'bri', 80)
            lights = b.get_light_objects()
            lights[2].xy = [0, 0.7]
            for i in range(10):
                lights[0].xy = [1, 1]
                lights[1].xy = [1, 1]
                time.sleep(0.6)
                lights[0].xy = [0.3, 0.3]
                lights[1].xy = [0.3, 0.3]
                time.sleep(0.6)
            lights[0].xy = [1, 1]
            lights[1].xy = [1, 1]

        elif forecasts[0]['telop']==u'晴時々雨':
            b.set_light([1,2,3], 'on', True)
            b.set_light([1,2,3], 'bri', 80)
            lights = b.get_light_objects()
            lights[2].xy = [0, 0.7]
            for i in range(10):
                lights[0].xy = [1, 1]
                lights[1].xy = [1, 1]
                time.sleep(0.6)
                lights[0].xy = [0, 0]
                lights[1].xy = [0, 0]
                time.sleep(0.6)
            lights[0].xy = [1, 1]
            lights[1].xy = [1, 1]

        elif forecasts[0]['telop']==u'曇時々晴':
            b.set_light([1,2,3], 'on', True)
            b.set_light([1,2,3], 'bri', 80)
            lights = b.get_light_objects()
            lights[2].xy = [0, 0.7]
            for i in range(10):
                lights[0].xy = [0.3, 0.3]
                lights[1].xy = [0.3, 0.3]
                time.sleep(0.6)
                lights[0].xy = [1, 1]
                lights[1].xy = [1, 1]
                time.sleep(0.6)
            lights[0].xy = [0.3, 0.3]
            lights[1].xy = [0.3, 0.3]

        elif forecasts[0]['telop']==u'曇時々雨':
            b.set_light([1,2,3], 'on', True)
            b.set_light([1,2,3], 'bri', 80)
            lights = b.get_light_objects()
            lights[2].xy = [0, 0.7]
            for i in range(10):
                lights[0].xy = [0.3, 0.3]
                lights[1].xy = [0.3, 0.3]
                time.sleep(0.6)
                lights[0].xy = [0, 0]
                lights[1].xy = [0, 0]
                time.sleep(0.6)
            lights[0].xy = [0.3, 0.3]
            lights[1].xy = [0.3, 0.3]

        elif forecasts[0]['telop']==u'雨時々晴':
            b.set_light([1,2,3], 'on', True)
            b.set_light([1,2,3], 'bri', 80)
            lights = b.get_light_objects()
            lights[2].xy = [0, 0.7]
            for i in range(10):
                lights[0].xy = [0, 0]
                lights[1].xy = [0, 0]
                time.sleep(0.6)
                lights[0].xy = [1, 1]
                lights[1].xy = [1, 1]
                time.sleep(0.6)
            lights[0].xy = [0, 0]
            lights[1].xy = [0, 0]

        elif forecasts[0]['telop']==u'雨時々曇':
            b.set_light([1,2,3], 'on', True)
            b.set_light([1,2,3], 'bri', 80)
            lights = b.get_light_objects()
            lights[2].xy = [0, 0.7]
            for i in range(10):
                lights[0].xy = [0, 0]
                lights[1].xy = [0, 0]
                time.sleep(0.6)
                lights[0].xy = [0.3, 0.3]
                lights[1].xy = [0.3, 0.3]
                time.sleep(0.6)
            lights[0].xy = [0, 0]
            lights[1].xy = [0, 0]

        elif forecasts[0]['telop']==u'晴のち曇':
            b.set_light([1,2,3], 'on', True)
            b.set_light([1,2], 'bri', 80)
            lights = b.get_light_objects()
            lights[2].xy = [0, 0.7]
            lights[0].xy = [1, 1]
            lights[1].xy = [0.3, 0.3]

        elif forecasts[0]['telop']==u'晴のち雨':
            b.set_light([1,2,3], 'on', True)
            b.set_light([1,2], 'bri', 80)
            lights = b.get_light_objects()
            lights[2].xy = [0, 0.7]
            lights[0].xy = [1, 1]
            lights[1].xy = [0, 0]

        elif forecasts[0]['telop']==u'曇のち晴':
            b.set_light([1,2,3], 'on', True)
            b.set_light([1,2], 'bri', 80)
            lights = b.get_light_objects()
            lights[2].xy = [0, 0.7]
            lights[0].xy = [0.3, 0.3]
            lights[1].xy = [1, 1]

        elif forecasts[0]['telop']==u'曇のち雨':
            b.set_light([1,2,3], 'on', True)
            b.set_light([1,2], 'bri', 80)
            lights = b.get_light_objects()
            lights[2].xy = [0, 0.7]
            lights[0].xy = [0.3, 0.3]
            lights[1].xy = [0, 0]

        elif forecasts[0]['telop']==u'雨のち晴':
            b.set_light([1,2,3], 'on', True)
            b.set_light([1,2], 'bri', 80)
            lights = b.get_light_objects()
            lights[2].xy = [0, 0.7]
            lights[0].xy = [0, 0]
            lights[1].xy = [1, 1]

        elif forecasts[0]['telop']==u'雨のち曇':
            b.set_light([1,2,3], 'on', True)
            b.set_light([1,2], 'bri', 80)
            lights = b.get_light_objects()
            lights[2].xy = [0, 0.7]
            lights[0].xy = [0, 0]
            lights[1].xy = [0.3, 0.3]

    finally:
        r.close()

def PM(event):
    url = "http://china-pm25.com/area/fukushima/"
    #少ない, やや多い, 多い
    html = urllib2.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    th = soup.find_all("th")
    kazu = "失敗"

    for tag in th:
        try:

            string_ = tag.get("class").pop(0)

            if string_ in "color2":
                kazu = tag.string
                break
        except:
            pass
    print kazu
    if kazu == u'少ない':
        b.set_light([1,2,3], 'on', True)
        b.set_light([1,2], 'bri', 80)
        lights = b.get_light_objects()
        lights[2].xy = [0, 0.7]
        lights[0].xy = [0.1, 0.1]
        lights[1].xy = [0.1, 0.1]

    elif kazu ==u'やや多い':
        b.set_light([1,2,3], 'on', True)
        b.set_light([1,2], 'bri', 80)
        lights = b.get_light_objects()
        lights[2].xy = [0, 0.7]
        lights[0].xy = [0.6, 0.6]
        lights[1].xy = [0.6, 0.6]

    elif kazu == u'多い':
        b.set_light([1,2,3], 'on', True)
        b.set_light([1,2], 'bri', 80)
        lights = b.get_light_objects()
        lights[2].xy = [0, 0.7]
        lights[0].xy = [1, 1]
        lights[1].xy = [1, 1]


def kahun(event):
    url = "https://tenki.jp/pollen/2/10/3630/7202/"
    #飛散開始前, 少ない, やや多い, 多い, 非常に多い, ほぼ終了
    html = urllib2.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    span = soup.find_all("span")
    kahun = ""

    for tag in span:
        try:
            string_ = tag.get("class").pop(0)

            if string_ in "pollen-telop":
                kahun = tag.string
                break
        except:
            pass

    print kahun
    if kahun == u'少ない':
        b.set_light([1,2,3], 'on', True)
        b.set_light([1,2], 'bri', 80)
        lights = b.get_light_objects()
        lights[2].xy = [0.2, 0.2]
        lights[0].xy = [0, 0.6]
        lights[1].xy = [0, 0.6]

    elif kahun == u'やや多い':
        b.set_light([1,2,3], 'on', True)
        b.set_light([1,2], 'bri', 80)
        lights = b.get_light_objects()
        lights[2].xy = [0.2, 0.2]
        lights[0].xy = [0, 0.8]
        lights[1].xy = [0, 0.8]

    elif kahun == u'多い':
        b.set_light([1,2,3], 'on', True)
        b.set_light([1,2], 'bri', 80)
        lights = b.get_light_objects()
        lights[2].xy = [0.2, 0.2]
        lights[0].xy = [0.970, 1]
        lights[1].xy = [0.970, 1]

    elif kahun == u'非常に多い':
        b.set_light([1,2,3], 'on', True)
        b.set_light([1,2], 'bri', 80)
        lights = b.get_light_objects()
        lights[2].xy = [0.2, 0.2]
        lights[0].xy = [0.534, 0.2]
        lights[1].xy = [0.534, 0.2]


    else :
        b.set_light([1,2,3], 'on', False)


def radiation(event):
    url = 'http://dokusyodebokin.rulez.jp/earthquake/now/?prefecture=%E7%A6%8F%E5%B3%B6'
    try:
        r = urllib2.urlopen(url)
        root = json.loads(r.read())
        # print root[0]['createtime']
        # print root[0]['place']
        # print root[0]['doserate'] #[doserate] ：空間線量率[nGy/h]
        t = root[0]['doserate']
    finally:
        r.close()

    if t >= 200:
        b.set_light([1,2,3], 'on', True)
        b.set_light([1,2], 'bri', 80)
        lights = b.get_light_objects()
        lights[2].xy = [0, 0.7]
        lights[0].xy = [0.4, 0.4]
        lights[1].xy = [0.4, 0.4]
        print '全然大丈夫'


    elif t >= 1000:
        b.set_light([1,2,3], 'on', True)
        b.set_light([1,2], 'bri', 80)
        lights = b.get_light_objects()
        lights[2].xy = [0, 0.7]
        lights[0].xy = [0, 1]
        lights[1].xy = [0, 1]
        print '結構多い'

    else :
        b.set_light([1,2,3], 'on', True)
        b.set_light([1,2], 'bri', 80)
        lights = b.get_light_objects()
        lights[2].xy = [0, 0.7]
        lights[0].xy = [0.5, 0.5]
        lights[1].xy = [0.5, 0.5]
        print '多分大丈夫'



Button = Tkinter.Button(text=u'天気', width=7)
Button.bind("<Button-1>",Tenki)
Button.place(x=40, y=100)
Button = Tkinter.Button(text=u'PM2.5', width=7)
Button.bind("<Button-1>",PM)
Button.place(x=150, y=100)
Button = Tkinter.Button(text=u'花粉', width=7)
Button.bind("<Button-1>",kahun)
Button.place(x=260, y=100)
Button = Tkinter.Button(text=u'放射線', width=7)
Button.bind("<Button-1>",radiation)
Button.place(x=40, y=200)
root.mainloop()
