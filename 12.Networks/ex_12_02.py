import socket, re

url = input('Enter URL: ')
try:
    tmp = url.split('/')
    host = tmp[2]
except:
    print('Invalid URL')
    quit()

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try: mysock.connect((host, 80))
except:
    print('Invalid URL')
    quit()

cmd = ('GET ' + url + ' HTTP/1.0\r\n\r\n').encode()
mysock.send(cmd)

cnt = 0
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    for ltr in data.decode():
        cnt += 1
        if cnt <= 3000: 
            print(ltr, end = '')
mysock.close()

print('\n', cnt, sep='')
