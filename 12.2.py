import socket

url = input('enter url')
try:
    host_name = url.split("/")[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host_name, 80))
    s = 'GET '+url+' HTTP/1.0\r\n\r\n'
    cmd = s.encode()
    mysock.send(cmd)
except:
    print('enter a valid url')
    quit()
count = 0
while True:
    data = mysock.recv(512)
    for s in data:
        count += 1
    if count > 3000 or len(data) < 1:
        break
print(count)
mysock.close()

