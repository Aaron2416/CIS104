
import urllib
import urllib.request

url = input('enter a url')
furl = urllib.request.urlopen(url)
count = 0
for line in furl:
    if count >= 3000: break
count += len(line.decode())
print(count)
        
