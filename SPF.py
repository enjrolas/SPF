#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import sys
import serial
import time
import re
import RPi.GPIO as GPIO
import sys, traceback

E_STOP=3
BACKINGS_SOLDERER=15


VACUUM_GENERATOR=7
SOLDERING_STATION=8
TEST_STATION=10
TEST_LIGHTS=11
TABBING_CUTTER=19
SOLDERING_POWER=21
SOLDERING_ENABLE=23
PICK_HEAD=24

GPIO.setmode(GPIO.BOARD)
#Sensors
GPIO.setup(E_STOP, GPIO.IN, pull_up_down=GPIO.PUD_UP) # E-stop
GPIO.setup(BACKINGS_SOLDERER, GPIO.IN, pull_up_down=GPIO.PUD_UP) # backings solderer logic

#Solenoids and switches
GPIO.setup(VACUUM_GENERATOR, GPIO.OUT) # vacuum generator solenoid
GPIO.setup(SOLDERING_STATION, GPIO.OUT) # soldering station solenoid
GPIO.setup(TEST_STATION, GPIO.OUT) # test station solenoid
GPIO.setup(TEST_LIGHTS, GPIO.OUT) # test station lights
GPIO.setup(TABBING_CUTTER, GPIO.OUT) # tabbing cutter solenoid
GPIO.setup(SOLDERING_POWER, GPIO.OUT) # soldering power
GPIO.setup(SOLDERING_ENABLE, GPIO.OUT) # soldering enable
GPIO.setup(PICK_HEAD, GPIO.OUT) # pick head solenoid


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

print("connecting to database....")
spfdb = MySQLdb.connect(host="106.187.94.198",port=3306,user="haddock-SPF",passwd="fnnAdGVRQPTDxSEY",db="djangoSPF")
print("connected!  Having a look around..")
cur = spfdb.cursor()
cur.execute("show tables")
results=cur.fetchall()
for table in results:
    print table

def moveConveyor(length):  #keeps track of where the pusher's stroke is
    if(length>0):
        print "yup, moving forwards"
        with spfdb:
            cur = spfdb.cursor()
            cur.execute("select * from panel_panel")
            try:
                row = fetchoneDict(cur)
                currentStroke=float(row['strokePosition'])
                panelLength=float(row['length'])
                strokeLead=float(row['stroke_lead'])
                strokeEnd=float(row['stroke_end'])
                fullStroke=panelLength+strokeLead+strokeEnd
                print "current stroke position: %f" % currentStroke
                if(currentStroke+length)<fullStroke:   #  if we can perform this motion just by pushing the current panel, just do it
                    print "we can do this just by pushing the current backing"
                    if(currentStroke<strokeLead):
                        advance=strokeLead-currentStroke
                        cmd="G0X"+str(advance)+chr(13)
                        ser.write(cmd)
                        flushReceiveBuffer()
                        currentStroke=strokeLead
                        
                    cmd="G0X"+str(length)+chr(13)
                    ser.write(cmd)
                    flushReceiveBuffer()
                    currentStroke=currentStroke+length
                    mysqlString="UPDATE panel_panel set strokePosition=\"%f\" where id='1'" % currentStroke
                    print mysqlString
                    cur.execute(mysqlString) 
                else:
                    while(currentStroke+length)>fullStroke:
                        print "we need to push at least two different backings to move this far"
                        remaining=fullStroke-currentStroke
                        cmd="G0X"+str(remaining)+chr(13)   #push what you can with the current panel
                        ser.write(cmd)
                        flushReceiveBuffer()
                        length=length-remaining
                        print cmd
                        
                        cmd="G0X-"+str(fullStroke)+chr(13)  #retract the pusher all the way
                        ser.write(cmd)
                        flushReceiveBuffer()
                        print cmd
                        
                        
                        cmd="G0X"+str(strokeLead+strokeEnd)+chr(13)  #advance the pusher until it's contacting the next panel
                        ser.write(cmd)
                        flushReceiveBuffer()
                        print cmd
                        currentStroke=strokeLead+strokeEnd
                    #now we've pushed all the full panels we need to push, and we just finish the last panel
                    cmd="G0X"+str(length)+chr(13)  #push the remaining distance
                    ser.write(cmd)
                    flushReceiveBuffer()
                    currentStroke=currentStroke+length
                    mysqlString="UPDATE panel_panel set strokePosition=\"%f\" where id='1'" % currentStroke
                    print mysqlString
                    cur.execute(mysqlString) 
                    
            except:
                traceback.print_exc(file=sys.stdout)            
                print "trouble getting the panel info from the database"
                pass
    else:
        cmd="G0X"+str(length)+chr(13)  #advance the pusher until it's contacting the next panel
        print cmd
        ser.write(cmd)
        flushReceiveBuffer()        

def doWonders():
    print("checking database")
    with spfdb:
        cur = spfdb.cursor()
        cur.execute("select * from command_command where status=\"queued\"")
        try:
            row = fetchoneDict(cur)
            print row
            id=row['id']
            parsable = row['json']
            print("json code:  " + parsable)
            for cmd in parsable.split():
                if(cmd[0] == '!'):
                    substr = cmd[1:]
                    if(substr == '1'):
                        tabbingCutterUp()
                    elif(substr == '2'):
                        tabbingCutterDown()
                    elif(substr == '3'):
                        pickHeadUp()
                    elif(substr == '4'):
                        pickHeadDown()
                    elif(substr == '7'):
                        vacuumGeneratorOn()
                    elif(substr == '8'):
                        vacuumGeneratorOff()
                    elif(substr == '9'):
                        compressorOn()
                    elif(substr == '10'):
                        compressorOff()
                    elif(substr == '13'):
                        testStationUp()
                    elif(substr == '14'):
                        testStationDown()
                    elif(substr == '15'):
                        solderingStationUp()
                    elif(substr == '16'):
                        solderingStationDown()
                    elif(substr == '17'):
                        solderingStationOn()
                    elif(substr == '18'):
                        solderingStationOff()
                        
                elif(cmd[0]=='M'):  #conveyor command
                    length=cmd[1:]  # the rest of the command is the distance that the conveyor should move
                    moveConveyor(float(length))
                elif(cmd[:3]=="G4P"):   #  intercept a sleep GCode command and run it on the pi rather than the G
                    delay=float(cmd[3:])/1000
                    time.sleep(delay)
                elif(cmd == 'g28.1'):
                    cmd = parsable + chr(13)
                    print cmd
                    ser.write(cmd)
                    flushReceiveBuffer()
                    break
                else:
                    cmd = cmd + chr(13)
                    print cmd
                    ser.write(cmd)
                    #we need to block until the serial RX buffer is 
                    #empty as this will indicate that the tinyG 
                    #is done with the motion     
                    flushReceiveBuffer()

            str = "UPDATE command_command set status=\"executed\" where id='%s'" % id
            print str
            cur.execute(str)
        except:
            traceback.print_exc(file=sys.stdout)            
            print "something didn't work out"
            pass

def fetchoneDict(cursor):
    row = cursor.fetchone()
    if row is None: return None
    cols = [ d[0] for d in cursor.description ]
    return dict(zip(cols, row))

def flushReceiveBuffer():
    while(True):
        time.sleep(.1)
        bytes_in_buffer = ser.inWaiting()
        if(bytes_in_buffer == 0):
            break
        print(ser.read(bytes_in_buffer))

def tabbingCutterDown():
    print("tabbingCutterUp()")
    GPIO.output(TABBING_CUTTER, False)

def tabbingCutterUp():
    print("tabbingCutterDown()")
    GPIO.output(TABBING_CUTTER, True)

def pickHeadDown():
    print("pickHeadUp()")
    GPIO.output(PICK_HEAD, False)

def pickHeadUp():
    print("pickHeadDown()")
    GPIO.output(PICK_HEAD, True)

def vacuumGeneratorOn():
    print("suctionSolenoidOn()")
    GPIO.output(VACUUM_GENERATOR, True)

def vacuumGeneratorOff():
    print("suctionSolenoidOff()")
    GPIO.output(VACUUM_GENERATOR, False)

def solderingStationUp():
    print("solderingStationUp()")
    GPIO.output(SOLDERING_STATION, False)

def solderingStationDown():
    print("solderingStationDown()")
    GPIO.output(SOLDERING_STATION, True)

def testStationUp():
    print("testStationUp()")
    GPIO.output(TEST_STATION, False)

def testStationDown():
    print("testStationDown()")
    GPIO.output(TEST_STATION, True)



try:
    while(True):
        doWonders()
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()