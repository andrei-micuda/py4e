#Extracting Data from XML

import urllib.parse, urllib.error, urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')

try:
    handle = urllib.request.urlopen(url)
except:
    print('Invalid URL.')
    quit()

print('Retrieving', url)

data = handle.read().decode()

print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)

comments = tree.findall('comments/comment')

print('Count:', len(comments))

s = 0

for comm in comments:
    s += int(comm.find('count').text)

print('Sum', s)
