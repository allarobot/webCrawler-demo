# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 01:27:28 2017

@author: Administrator
"""

import requests
url = "http://www.baidu.com/s"
keyword = "Python"
try:
    kv ={"wd":keyword}
    r = requests.get(url,params=kv)
    print(r.url)
    r.raise_for_status
    print(len(r.text))
except:
    print("Error")