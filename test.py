#!/usr/bin/python
# -*- coding: utf-8 -*-
import serial
import time
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
print("TinyG found! Connection established.")


cmd = "$xfr=3000" + chr(13)
ser.write(cmd)
cmd = "$yfr=3000" + chr(13)
ser.write(cmd)
cmd = "$zfr=3000" + chr(13)
ser.write(cmd)
cmd = "$afr=3000" + chr(13)
ser.write(cmd)
cmd = "$x" + chr(13)
ser.write(cmd)
cmd = "G28.2X0"+chr(13)
ser.write(cmd)

while(True):
    time.sleep(.1)
    bytes_in_buffer = ser.inWaiting()
    if(bytes_in_buffer == 0):
        break
    print(ser.read(bytes_in_buffer))

