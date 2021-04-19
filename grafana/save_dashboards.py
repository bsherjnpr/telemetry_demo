#!/usr/bin/python


import requests
import json

server = "https://127.0.0.1:3000/grafana"

# Example 1: Get default Home dashboard:
url = server + "/api/dashboards/home"
# To get the dashboard by uid
# url = server + "/api/dashboards/uid/" + uid

headers = {"Authorization":"Bearer eyJrIjoiWnVjWGpscjVhTGQzamRva1RySmVoZU1uZlZFbVd4U28iLCJuIjoicXFxIiwiaWQiOjF9"}
r = requests.get(url = url, headers = headers, verify=False)

print(r.json())
