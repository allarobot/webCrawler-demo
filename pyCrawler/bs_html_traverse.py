# -++++++++++++++
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
print("title",soup.title)
print(soup.a)    
print(soup.a.name,soup.a.parent.name)    
print(soup.a.attrs)

print("a.parents:")
for item in soup.a.parents:
    print(item)
    
print("a.next_siblings:")
for item in soup.a.next_siblings:
    print(item)
    
print("body.descendants:")   
for item in soup.body.descendants:
    print(item)









