#!/bin/python3
# Il problema e' stato trovare la chiave con cui vengono criptati i cookie
# Poiche' conoscevamo l'input e l'output e' bastato eseguire l'operazione di cript dello xor usando come chiave l'ouput
# Una volta conosciuta la chiave ci e' bastato criptare con essa i valori che ci richiedeva il livello
import requests

user = 'natas11'
password = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'

url = 'http://%s.natas.labs.overthewire.org' % user

post = requests.post(url + '/index.php', auth=(user, password), cookies={
    'data': 'ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK'})

print(post.text)

'''
#Cookie di default
# {"showpassword":"no","bgcolor":"#ffffff"} -->  ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D

#Cookie ricevuto inviando un diverso colore con il metodo post
# {"showpassword":"no","bgcolor":"#aaaaaa"} --> ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSFlkrEBZZaAw%3D

<?php
    //Sappiamo che questi sono i valori di default
    $text = json_encode(array("showpassword"=>"no","bgcolor"=>"#ffffff"));
    $risultato = base64_decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D");
    $outText = '';

    //Codice usato per trovare la chiave ripetuta
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $risultato[$i % strlen($risultato)];
    }
    
    print($outText);
'''
