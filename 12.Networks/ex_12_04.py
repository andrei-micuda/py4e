import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter URL: ')

try:
    html = urllib.request.urlopen(url).read()
except:
    print('Invalid URL')
    quit()

soup = BeautifulSoup(html, 'html.parser')

pars = soup('p')

print(len(pars))
