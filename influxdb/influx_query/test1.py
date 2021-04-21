from influxdb import InfluxDBClient
import json

client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('telegraf')
results = client.query('select "/interfaces/interface[if_name=\'et-0/0/51\']/state/counters/if_in_octets" from "interfaces" where "device" = \'10.48.188.97\' and time >= now() - 10m')

#print (results.raw)
#print (json.dumps(results.raw,indent=4))

points = results.get_points()

data =[]
for point in points:
   #print("Time: %s, value: %i" % (point['time'], point['/interfaces/interface[if_name=\'et-0/0/51\']/state/counters/if_in_octets']))
   data.append(point['/interfaces/interface[if_name=\'et-0/0/51\']/state/counters/if_in_octets'])

#print (data)
for x in range(len(data)-1):
   #print (x,data[x])
   print ((data[x+1] - data[x])/60)

