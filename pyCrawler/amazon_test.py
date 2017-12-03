# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 01:06:46 2017

@author: Administrator
"""
import requests
url = "https://www.amazon.cn/dp/B003LBSRDM/ref=cngwdyfloorv2_recs_0?pf_rd_p=05f2b7d6-37ec-49bf-8fcf-5d2fec23a061&pf_rd_s=desktop-2&pf_rd_t=36701&pf_rd_i=desktop&pf_rd_m=A1AJ19PSB66TGU&pf_rd_r=4S8Y4BH77X7F0ZMMGTT2&pf_rd_r=4S8Y4BH77X7F0ZMMGTT2&pf_rd_p=05f2b7d6-37ec-49bf-8fcf-5d2fec23a061"
kv = {'user-agent':'Mozilla/5.0'}
try:
    #r = requests.get(url)
    r = requests.get(url,headers=kv)
    r.raise_for_status
    r.encoding = r.apparent_encoding
    print(r.status_code)
    print(r.text[1000:2000])
except:
    print("Error")