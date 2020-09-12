#!/bin/python3

# DEvo vedere come funziona il metodo post di requests
import requests
import re

user = 'natas6'
password = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'

url = 'http://%s.natas.labs.overthewire.org' % user
obj = {'secret': 'FOEIUWGHFEEUHOFUOIU', 'submit': 'submit'}

post = requests.post(url + '/index.php', data=obj, auth=(user, password))

testo = post.text

print(testo)

re = re.findall('natas7 is (.*)', testo)
print('Password:')
print(re[0])
