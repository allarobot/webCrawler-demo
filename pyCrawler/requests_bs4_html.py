# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
import os
from bs4 import BeautifulSoup
root = "c:\html"
file ="index.html"
path = os.path.join(root,file)
url = "https://python123.io/ws/demo.html"
if not os.path.exists(root):
    os.mkdir(root)
    
with open(path,'w') as fp:
    r = requests.get(url)
    print(r.status_code)
    demo = r.text
    fp.write(demo)
    fp.close()
    print("Saved")
    
soup = BeautifulSoup(demo,"html.parser")
print(soup.prettify())
    


