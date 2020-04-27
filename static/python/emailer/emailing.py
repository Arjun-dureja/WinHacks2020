#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import smtplib
import getpass
import sys
import time
import random
from colorama import init, Style, Back, Fore

def BomEmail():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

f = open("./static/python/emailer/emails").read().splitlines()
user = random.choice(f)

password = open("./static/python/emailer/password", "r")
passwd = password.read()

to = "arjun.dureja1000@gmail.com"
#to = "uzairmahmed@gmail.com"
eSubject = 'Help Canada combat Coronavirus disease (COVID-19)'

body = "Hello, this message is sent on behalf of CoronaBase in hopes of obtaining help in the battle against COVID-19. We are seeking products and services that can aid in the relief of COVID-19. If interested please provide us with your information so that we will be able to contact you. If you already have submitted a form and want to make changes please include “AMENDED FORM” as part of your subject.\n\nYour name: \nCompany name: \nPhone number: \nEmail: \nCountry: \nAddress (where the items will be supplied from): \nWill a government official be able to visit the location the items will be supplied from? (Yes/No) \nIndicate what type of product(s) you are able to supply in support of Canada's initiative against COVID-19. \nExamples of products we are seeking include disposable N95 masks, disposable surgical masks, nitrile gloves, vinyl gloves, COVID-19 testing kits, flock swabs, and ventilation systems/components. \nInclude the quantity of the items as well as the availability of the supply beside the type of item. \nExample: N95 Masks:500, E700 Series Ventilation System: 70 \n\nIndicate what type of service(s) you are able to supply in support of Canada's initiative against COVID-19. \nExamples of services we are seeking include guarding/security services, nursing services, food services, laundry services, accommodation maintenance services, personal services, and IT Support services. \nInclude the quantity of personnel as well as the availability of the supply beside the type of service. \nExample: Nurses: 30, Security Guards: 40 \n\nIf you have any other product(s)/service(s) you can provide that is not mentioned in the list above, include them alongside the quantity and availability of supply in the same format."
total = 1

smtp_server = 'smtp.gmail.com'
port = 587


print ('')

try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user,passwd)
    for i in range(1, total+1):
        subject = eSubject
        msg = ('From: ' + user + '\nSubject: ' + subject + '\n' + body).encode("utf-8")
        server.sendmail(user,to,msg)
        print ("\rE-mails Sent: %i" % i)
        sys.stdout.flush()
    server.quit()
    print ('\nDone! Sent ' + str(total) + ' emails to ' + to +'\n')
except KeyboardInterrupt:
    print ('Canceled')
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print ('\n[!] You must allow access to less secure apps on your gmail account. https://www.google.com/settings/security/lesssecureapps')
    sys.exit()
