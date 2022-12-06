import socket
import urllib.request

url = input('Enter Url ')
url = urllib.request.urlopen(url)

try:
	host_name = url.split('/')
	mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mysock.connect(('host_name', 80))
	mysock.send('GET ' + url + '  HTTP/1.0\r\n\r\n').encode()
except:
	print('improperly formatted or non-existent URL')
	exit()

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()