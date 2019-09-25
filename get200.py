# !/usr/bin/env python
# -- coding: utf-8 --

import requests
import urllib3
import certifi
import time
import datetime

arq = open('lista.csv', 'r')
arq_200 = open('200.csv', 'w')
arq_404 = open('404.csv', 'w')
arq_405 = open('405.csv', 'w')
arq_500 = open('405.csv', 'w')

cont_200 = 0
cont_404 = 0
cont_405 = 0
cont_500 = 0

urllib3.disable_warnings()

while True:
    linha = arq.readline()
    if linha == "":
        break
    url = linha.strip()
    print url
    r = requests.get(url, verify=False)
    
    if (r.status_code == 200):
        print('\033[32mStatus Code 200\033[m')
        arq_200.write(linha)
        cont_200 += 1

    if (r.status_code == 405):
        print('\033[31mStatus Code 405\033[m')
        arq_405.write(linha)
        cont_405 += 1

    if (r.status_code == 404):
        print('\033[31mStatus Code 404\033[m')
        arq_404.write(linha)
        cont_404 += 1

    elif (r.status_code == 500):
        print('\033[31mStatus Code 500\033[m')
        arq_500.write(linha)
        cont_500 += 1

print
print '---------------------------'
print
print "Data: " , datetime.datetime.now().strftime("%d/%m/%y"), "- Hora: " , datetime.datetime.now().strftime("%H:%M")
print       
print 'Páginas com Status Code 200:', (cont_200)
print
print 'Páginas com Status Code 404:', (cont_404)
print
print 'Páginas com Status Code 405:', (cont_405)
print
print '---------------------------'
print


arq.close()
arq_200.close()
arq_404.close()
