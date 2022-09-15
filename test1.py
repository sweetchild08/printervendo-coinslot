#!/usr/bin/env python

import argparse
import configparser
import board
import time
import digitalio
import os
import requests as req
from gpiozero import Button



coinslot = Button(16)
confirm = Button(2,bounce_time=5)
reset = Button(3,bounce_time=5)

config = configparser.ConfigParser()
config.read('config.ini')

controller = config.get('config', 'controller')
username = config.get('config', 'username')
password = config.get('config', 'password')
port = config.get('config', 'port')
version = config.get('config', 'version')
siteid = config.get('config', 'siteid')
nosslverify = config.get('config', 'nosslverify')
certificate = config.get('config', 'certificate')

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--controller', default=controller)
parser.add_argument('-u', '--username', default=username)
parser.add_argument('-p', '--password', default=password)
parser.add_argument('-b', '--port', default=port)
parser.add_argument('-v', '--version', default=version)
parser.add_argument('-s', '--siteid', default=siteid)
parser.add_argument('-V', '--no-ssl-verify', default=nosslverify, action='store_true')
parser.add_argument('-C', '--certificate', default=certificate)
args = parser.parse_args()


    
# https://stackoverflow.com/questions/52126586/python-scripting-for-coins-slot-raspberry-pi
re = req.get('http://localhost/addcoin.php')
# if(isReading=)
while True:
    total = 0
    state = True
    counter = 0
    print ('Insert coin and\npress confirm')
    while state:
        if coinslot.is_pressed:
            counter+=1
            time.sleep(.05)
            r = req.get('http://localhost/addcoin.php')
            print(r.text)
            if counter == 1:
                print('{} Peso\ninserted'.format(counter))
            else:
                print('{} Pesos\ninserted'.format(counter))

        # https://gist.github.com/alaudet/9e280d190bff83830dc7
        if reset.is_pressed:
            time.sleep(5)
            if reset.is_pressed:
                    lcd.message = "Shutting down"

                    cmd = "sudo shutdown -h now"
                    os.system(cmd)

        if confirm.is_pressed:
            state = False
            total = counter * 4 # 1 peso = 4 minutes

            if total == 0:
                lcd.message = 'No coin inserted\nplease wait'
                time.sleep(5)
                break

                # https://stackoverflow.com/a/18175488/10025507
                timeout = 90
                while timeout != 0:
                    if reset.is_pressed:
                        break
                
