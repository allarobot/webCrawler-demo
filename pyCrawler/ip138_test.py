# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 01:46:41 2017

@author: Administrator
"""

import requests
url = "http://www.ip138.com/ips138.asp"
keyword = "202.204.80.112"
kv ={"ip":keyword}
r = requests.get(url,params=kv)
r.encoding = r.apparent_encoding
print(r.status_code)
print(r.url)
print(r.text[7200:7500])