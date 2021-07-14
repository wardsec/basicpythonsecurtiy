import hashlib
import ctypes
import itertools
import re
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import phonenumbers
from phonenumbers import geocoder

menu = int(input (''' #####  TOOLKIT TEXT #####
               
 ██████ ██░ ██ ██▓██▀███  ▒█████  
▒██    ▒▓██░ ██▓██▓██ ▒ ██▒██▒  ██▒
░ ▓██▄  ▒██▀▀██▒██▓██ ░▄█ ▒██░  ██▒
  ▒   ██░▓█ ░██░██▒██▀▀█▄ ▒██   ██░
▒██████▒░▓█▒░██░██░██▓ ▒██░ ████▓▒░
▒ ▒▓▒ ▒ ░▒ ░░▒░░▓ ░ ▒▓ ░▒▓░ ▒░▒░▒░ 
░ ░▒  ░ ░▒ ░▒░ ░▒ ░ ░▒ ░ ▒░ ░ ▒ ▒░ 
░  ░  ░  ░  ░░ ░▒ ░ ░░   ░░ ░ ░ ▒  
      ░  ░  ░  ░░    ░        ░ ░  
O Que deseja fazer? Selecione:   
    1)  Gerar Wordlist
    2)  Gerar MD5
    3)  Gerar SHA1
    4)  Gerar SHA256 
    5)  Gerar SHA521 
    6)  Web Scraping  
     >>>>>>>>>>> Digite a opção e confirme <<<<<<<<<<<<<<
   '''))

if menu == 1:
    string = input("Insira o os caracteres : ")
    resultado = itertools.permutations(string, len(string))
    for c in resultado:
        print(''.join(c))
        
elif menu == 2:
    string = input("Digite o texto a ser gerado o Hash: ")
    resultado = hashlib.md5(string.encode('utf-8'))
    print('A hash md5 da string : ',string, 'é: ', resultado.hexdigest())
    
elif menu == 3:
    string = input("Digite o texto a ser gerado o Hash: ")
    resultado = hashlib.sha1(string.encode('utf-8'))
    print('A hash sha1 da string : ',string, 'é: ', resultado.hexdigest())
    
elif menu == 4:
    string = input("Digite o texto a ser gerado o Hash: ")
    resultado = hashlib.sha256(string.encode('utf-8'))
    print('A hash sha256 da string : ',string, 'é: ', resultado.hexdigest())
    
elif menu == 5:
    string = input("Digite o texto a ser gerado o Hash: ")
    resultado = hashlib.sha512(string.encode('utf-8'))
    print('A hash sha512 da string : ',string, 'é: ', resultado.hexdigest())
    
elif menu == 6:
    site =  requests.get(input('Insira o endereço do site Exemplo: https://www.linkedin.com: ')).content
    soup = BeautifulSoup(site, 'html.parser')
    print(soup.prettify)

