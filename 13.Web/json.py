#Extracting Data from JSON

import urllib.parse, urllib.error, urllib.request
import json

url = input('Enter location: ')

try:
    handle = urllib.request.urlopen(url)
except:
    print('Invalid URL.')
    quit()

print('Retrieving', url)

data = handle.read().decode()

print('Retrieved', len(data), 'characters')

js = json.loads(data)

print('Count:', len(js['comments']))

s = 0

for comm in js['comments']:
    s += int(comm['count'])

print('Sum', s)
