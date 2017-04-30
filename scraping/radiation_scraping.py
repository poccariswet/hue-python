#!/usr/bin/python
#coding:utf-8
from phue import Bridge
import time
import json, urllib2

b = Bridge('192.168.2.2')
b.connect()

#!/usr/bin/python
# coding: utf-8
import urllib2
from bs4 import BeautifulSoup
#放射線(会津若松)の今日の値
# アクセスするURL
url = "http://radioactivity.nsr.go.jp/map/ja/area2.html"
#数値
html = urllib2.urlopen(url)
soup = BeautifulSoup(html, "html.parser")
span = soup.find_all("span")
kazu = "失敗"
# print span

for tag in span:
    try:

        string_ = tag.get("lastData").pop(0)
        print string_

        if string_ in "":
            kazu = tag.string
            break
    except:
        pass
print kazu
