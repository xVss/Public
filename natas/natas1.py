#!/bin/python3
import requests
import re

user = 'natas1'
password = 'gtVrDuiDfck831PqWsLEZy5gyDz1clto'

url = 'http://%s.natas.labs.overthewire.org' % user

risposta = requests.get(url, auth=(user, password))
testo = risposta.text

print(testo)

re = re.findall('natas2 is (.*) -->', testo)
print('Password')
print(re[0])
