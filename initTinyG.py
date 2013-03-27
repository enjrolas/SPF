#!/usr/bin/python
# -*_ coding: utf-8 -*-

import MySQLdb as mdb
import sys
import urllib2
import serial

config = open('config.spf', 'r')
config_remote = config.read().split('=')
if config_remote[1] == 'true\n':
    url = "http://internal.solarpocketfactory.com/startup/"
elif config_remote[1] == 'false\n':
    url = "http://solarpocketfactory.com:80/startup/"
else:
    print "invalid value for \'remote\' in config.spf"
    sys.exit()

print "url = %s" %url

cmd = ""
ser = None
port = "/dev/ttyUSB0"
for tries in range(1,5):
    try:
        print("Attempting to connect to the TinyG via " + port)
        ser = serial.Serial(port, 115200)
    except:
        pass

if ser is None:
    print("no TinyG found. exiting..")
    sys.exit()
else:
    print("Connection successful!")

def paramUpdate():
    req = urllib2.Request(url)
    urldata = urllib2.urlopen(req)
    response = urldata.read()
    print response
    payload = response.split()
    for cmd in payload:
        print("Setting parameter : %s ...") %cmd
        cmd = cmd + chr(13)
        ser.write(cmd)
        clearRXbuffer()

    print("TinyG successfully initialized!")

def clearRXbuffer():
    while(True):
        bytes_in_use = ser.inWaiting()
        if(bytes_in_use == 0):
            break
        ser.read(bytes_in_use)  

paramUpdate()
