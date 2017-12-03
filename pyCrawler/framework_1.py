# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 23:43:49 2017

@author: Administrator
"""
import requests

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Error Responsed"

if __name__ =="__main__":
    url = "http://www.baidu.com"
    res = getHTMLText(url)
    print(res)