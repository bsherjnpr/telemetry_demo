#!/usr/bin/python3


import requests
import json

bearer = "eyJrIjoiWnVjWGpscjVhTGQzamRva1RySmVoZU1uZlZFbVd4U28iLCJuIjoicXFxIiwiaWQiOjF9"
server = "http://127.0.0.1:3000"

# Example 1: Get default Home dashboard:
url = server + "/api/dashboards/home"
# To get the dashboard by uid
# url = server + "/api/dashboards/uid/" + uid

headers = {"Authorization":"Bearer " + bearer}
r = requests.get(url = url, headers = headers, verify=False)
#r = requests.get(url = url, headers = headers)
#
print(r.json())
print(r)

print("====================")

url = server + "/api/search?query=%"
headers = {
    "Authorization":"Bearer " + bearer,
    "Content-Type":"application/json",
    "Accept": "application/json"
}
r = requests.get(url = url, headers = headers, verify=False)
for item in r.json():
    if item['type'] == 'dash-db':
        print(item) 
        url = server + "/api/dashboards/uid/" + item['uid']
        r = requests.get(url = url, headers = headers, verify=False)
        print (r.json())


