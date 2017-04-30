#!/usr/bin/python
# coding: utf-8
import lxml.html
import requests

target_url = 'http://www.tenki.jp/indexes/uv_index_ranking/2/10/3630.html'
target_html = requests.get(target_url).text
root = lxml.html.fromstring(target_html)
#text_content()メソッドはそのタグ以下にあるすべてのテキストを取得する
t = root.cssselect('#container > #bd > #bd-main > div > #exponentLarge > #exponentLargeLeft > dd > span')#.text_content()
print t
