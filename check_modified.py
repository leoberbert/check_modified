#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: Mon Jun  7 12:59:31 -03 2021
# Autor: Leonardo Berbert

import os.path as path
import time
import requests
import os
import sys

threshold = 1 #In hour
scriptname = sys.argv[0].split('/')[-1].split('.')[0]   

try:
    file = sys.argv[1]
    app = sys.argv[2]
except IndexError as e:
    print("")
    print("Usage: ./" + scriptname + ".py" " /tmp/application.log my_application_name")
    print("")
    exit(1)

myhost = os.uname()[1]

def check_older(file): 
    file_time = path.getmtime(file) 
    return ((time.time() - file_time) / 3600)

def notify(app,myhost):
    endpoint='http://10.168.10.10' + ':4000/notify'
    headers={'Content-Type': 'application/json'}
    alertMessage = 'URGENTE - Aplicacao ' + app + ' na maquina ' + myhost + " sem incrementar o log " + file + " a mais de "  + str(threshold) + "h."
    json_data='''{"message": "''' + alertMessage + '''"}'''
    try:
        response=requests.post(url=endpoint, data=json_data, headers=headers)
    except requests.exceptions.RequestException as e:
        print('Ocurred the following error on request: ' + str(e))

    
stat_file = round(check_older(file))

if stat_file > threshold:
    notify(app,myhost)
