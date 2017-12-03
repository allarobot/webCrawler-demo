# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 01:37:18 2017

@author: Administrator
"""

import requests
import os
url ="https://images-cn.ssl-images-amazon.com/images/I/51l5InFD7RL._SX380_BO1,204,203,200_.jpg"
root = "c://data"
path = os.path.join(root,url.split("/")[-1])
try:
    
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("Saved")
except:
    print("Error")