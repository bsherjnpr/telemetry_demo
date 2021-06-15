#!/usr/bin/python3

import argparse
from jinja2 import Template

def get_influxdb_token():
    token_file = args.influxdb_token_file
    token = token_file.readline().strip()
    #print("token =",token)
    return token


def generate_template():   

   template = """
apiVersion: 1

datasources:

  - name: influxdb2
    type: influxdb
    access: proxy
    url: http://localhost:8086
    user: grafana
    secureJsonData:
      token: {{ token }}
    jsonData:
      version: Flux
      organization: netmon
      defaultBucket: bucket1
    isDefault: true

"""

   data = {
       "token": get_influxdb_token()
   }

   j2_template = Template(template)

   print(j2_template.render(data))


def main():

   pass

if __name__ == "__main__":
   global args
   parser = argparse.ArgumentParser(description='Process some integers.')
   parser.add_argument('--influxdb_token_file', type=argparse.FileType('r')) 
   args = parser.parse_args()

   generate_template()



   



