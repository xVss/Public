#!/bin/python3
import requests

user = 'natas12'
password = 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'

url = 'http://%s.natas.labs.overthewire.org/' % user
#obj = {'secret': 'oubWYf2kBq', 'submit': 'submit'}

post = requests.post(url + '/index.php', auth=(user, password))

print(post.text)

# /etc/natas_webpass/natas13
