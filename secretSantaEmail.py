# coding: utf8
#! /usr/bin/python3
# Date: Tue 01 December 2020 12:36:18 CET
# Author: Nicolas Flandrois
# License: MIT License - Copyright (c) 2020 Nicolas Flandrois
# Version: v2

# Description: Sending `Secret Santa` assignement, automatically by email.
# cf secretsanta.py project for random assignment algorythm.
# This script uses GMAIL services.
# For other email services, please change your SMTP server.

import os
import smtplib
from email.message import EmailMessage
import random


def send_email(from_addr, gmail_key,
               to_addrs, subject,
               body_txt='DEFAULT - This is a plain text email',
               body_html=None, attached_file=None):
    try:
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = from_addr
        msg['To'] = to_addrs

        msg.set_content(body_txt)  # Body as text

        if body_html is not None:
            msg.add_alternative(body_html, subtype='html')  # Body as HTML

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(from_addr, gmail_key)
            smtp.send_message(msg)
            print('Email sent successfully')

    except Exception as e:
        print(e)
        print('\nEmail failed to send.')


##############################################################################


def secret_santa(santas_list):
    '''
    Taking a list of participants nested with dictionaries
    {"name":"Real name", "email":"His_email@naughty_or.nice"}
    This function will return a paired dictionary, for each email of a secret
    santa is associated the person he is associated with to give
    a secret gift to.
    '''
    random.shuffle(santas_list)
    pair = {}

    for n in santas_list:
        santa = n["email"]
        pair[santa] = santas_list[santas_list.index(n)-1]["name"]

    return pair

##############################################################################
# Variables
santas_list = [{"name":"Test1", "email":"Test1@naughty_or.nice"},
               {"name":"Test2", "email":"Test2@naughty_or.nice"},
               {"name":"Test3", "email":"Test3@naughty_or.nice"}]

from_addr = os.environ.get('EMAIL_USER')
gmail_key = os.environ.get('EMAIL_PASS')
subject = 'Secret Santa 2020'

##############################################################################
if __name__ == "__main__":
    print('Secret Santas distribution sent from: ', from_addr)
    secret_santas_list = secret_santa(santas_list)
    for to_email, name in secret_santas_list.items():
        msg = f"""This email has been sent by a Python Bot!
Secret Santa Project 2020.
You are {name}'s Secret Santa!
Please offer him a well suited gift this Year.
"""

        body_html = f"""<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">Secret Santa 2020</h1>
        <p>Tu es le 'Secret Santa' de {name}.</p>
        <h3>Naughty or Nice ?</h3>
        <p>Bla Bla Bla... Jingle Bells</p>
    </body>
</html>"""
        send_email(from_addr, gmail_key, to_email,
                  subject, msg, body_html)
