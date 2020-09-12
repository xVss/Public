#!/bin/python3
import requests
import re

user = 'natas0'
password = 'natas0'

url = 'http://%s.natas.labs.overthewire.org' % user

risposta = requests.get(url, auth=(user, password))
testo = risposta.text

print(testo)

re = re.findall('natas1 is (.*) -->', testo)
print('Password:')
print(re[0])
