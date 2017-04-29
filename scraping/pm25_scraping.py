#!/usr/bin/python
# coding: utf-8
import urllib2
from bs4 import BeautifulSoup
#pm2.5(会津若松)の今日の値
# アクセスするURL
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
