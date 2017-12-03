# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 23:28:15 2017

@author: Administrator
"""
import requests
r = requests.get("http://www.baidu.com")
print(r.status_code)
print(r.text)

#export
print(r.encoding,r.apparent_encoding)
r.encoding = r.apparent_encoding
print(r.text)
