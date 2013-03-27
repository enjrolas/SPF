#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import serial
import time
import re

ser = None
port = "/dev/ttyUSB0"
for tries in range(1,5):
    try:
        print("Establishing connection with TinyG through port " + port)
        ser = serial.Serial(port, 115200)
    except:
        pass
if ser is None:
        print("Cannot establish connection with TinyG. Exiting.")
        sys.exit()
print("TinyG found! Connection established.")

cmd = ['$s', '$m', '$n']
buffer = ['', '', '']
i = 0
for item in cmd:
    ser.write(item + chr(13))
    time.sleep(1)

    while(ser.inWaiting()):
        buffer[i] += ser.read()
    i +=1

expr = re.compile("^\[(.*?)\]")

for item in buffer:
    setting = item.split('\n')
    for parameter in setting:
        param_name = expr.match(parameter)
        if(param_name != None):
            param_val = parameter.split()[2]
            print "name = " + param_name.group(1) + " value = " + param_val
