import urllib.request, urllib.parse, urllib.error

url = input('Enter URL: ')

try:
    handle = urllib.request.urlopen(url)
except:
    print("Invalid URL")
    quit()

cnt = 0
for char in handle.read().decode():
    cnt += 1
    if cnt <= 3000:
        print(char, end = '')

print('\n', cnt, sep = '')
