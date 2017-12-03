# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 21:04:41 2017

@author: Administrator
"""
import requests
from bs4 import BeautifulSoup
import re
url = "https://python123.io/ws/demo.html"
r = requests.get(url)
txt = r.text
print(txt)
#soup = BeautifulSoup(txt,'lxml')
soup = BeautifulSoup(txt,'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))
    
print(soup.find_all('p','course'))
print(soup.find_all(text=re.compile("Python")))