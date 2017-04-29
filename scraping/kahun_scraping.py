#!/usr/bin/python
# coding: utf-8
import urllib2
from bs4 import BeautifulSoup
#花粉(会津若松)の今日の値
# アクセスするURL
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
