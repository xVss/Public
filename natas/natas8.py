#!/bin/python3
# Basta eseguire le funzioni php inverse al segreto codificato che si trova in chiaro nl codice
import requests

user = 'natas8'
password = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'

url = 'http://%s.natas.labs.overthewire.org/' % user
obj = {'secret': 'oubWYf2kBq', 'submit': 'submit'}

post = requests.post(url + '/index.php', data=obj, auth=(user, password))

print(post.text)
