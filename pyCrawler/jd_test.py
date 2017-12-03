# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 00:40:28 2017

@author: Administrator
"""

import requests
try:
    r = requests.get("https://item.jd.com/2967929.html")
    r.status_code
    r.encoding
    print(r.text[:1000])
except:
    print("Error")