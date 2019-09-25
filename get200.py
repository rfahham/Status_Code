# !/usr/bin/env python
# -- coding: utf-8 --


# $ sudo -H pip install requests
# $ sudo -H pip install urllib3
# $ sudo -H pip install certifi

# OU

# pip install -r requirements.txt


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



# Docs

# instalar o pip => sudo easy_install pip
# instalar o request sudo pip install requests => http://requests-docs-pt.readthedocs.io/pt_BR/latest/user/quickstart.html
# http://docs.python-requests.org/en/master/user/quickstart/#make-a-request
# http://docs.python-requests.org/en/latest/user/advanced/#ssl-cert-verification
# https://docs.python.org/2/howto/urllib2.html
# https://urllib3.readthedocs.io/en/latest/user-guide.html#ssl

# https://www.tutorialspoint.com/python/python_if_else.htm
# https://forum.gamemods.com.br/threads/python-07-estrutura-de-repeticao.36655/
# https://stackoverflow.com/questions/27981545/suppress-insecurerequestwarning-unverified-https-request-is-being-made-in-pytho
