#Using the GeoJSON API

import urllib.request, urllib.parse, urllib.error
import json

service_url = 'https://py4e-data.dr-chuck.net/json?'
api_key = 42

address = input('Enter location: ')

parms = dict()

parms['address'] = address
parms['key'] = api_key

url = service_url + urllib.parse.urlencode(parms)

try:
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    js = json.loads(data)

except:
    print('Invalid URL.')
    quit()

print('Retrieved', len(data), 'characters')

print('Place id', js['results'][0]['place_id'])
