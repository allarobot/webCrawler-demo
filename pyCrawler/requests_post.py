# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 00:09:17 2017

@author: Administrator
"""
import requests
payload = {"key1":"value1","key2":"value22"}
r = requests.post("http://httpbin.org/post",data= payload)
print("After post")
print(r.text)

r = requests.put("http://httpbin.org/put",data= "ABC")
print("After put")
print(r.text)

r = requests.request("OPTIONS","http://httpbin.org/put")
print("OPTIONS")
print(r.text)