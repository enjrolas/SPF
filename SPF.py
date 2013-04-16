#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import sys
import serial
import time
import re
import sys, traceback
from hardware import *
import pickle
import urllib, urllib2


points=[] #  

### safe the solderer, for safety's safe
solderingStationOff()
solderingStationUp()
ser = None
port = "/dev/ttyUSB0"
if  __debug__:
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
spfdb = MySQLdb.connect(host="106.187.94.198",port=3306,user="haddock-SPF",passwd="fnnAdGVRQPTDxSEY",db="SPF-testing")
print("connected!")


def getRemainingStroke():
    with spfdb:
        cur = spfdb.cursor()
        cur.execute("select * from panel_panel")
        try:
            print "pulling motion parameters from the database"
            row = fetchoneDict(cur)
            currentStroke=float(row['strokePosition'])
            panelLength=float(row['length'])
            strokeLead=float(row['stroke_lead'])
            strokeEnd=float(row['stroke_end'])
            fullStroke=panelLength+strokeLead+strokeEnd
            if currentStroke>strokeLead:   #we're already into a stroke, we'll have to push out this panel before we get to the next one
                return fullStroke-currentStroke
            else:
                return 0
        except Exception as e:
            print e
            print "ruh roh.  Something went wrong"
            return 0


def moveConveyor(length):  
    """moveConveyor() takes in a desired distance to advance the conveyor, then generates the gcode commands to move the pusher back and forth, advancing all the panels that distance"""
    with spfdb:
        cur = spfdb.cursor()
        cur.execute("select * from panel_panel")
        try:
            print "pulling motion parameters from the database"
            row = fetchoneDict(cur)
            currentStroke=float(row['strokePosition'])
            panelLength=float(row['length'])
            strokeLead=float(row['stroke_lead'])
            strokeEnd=float(row['stroke_end'])
            fullStroke=panelLength+strokeLead+strokeEnd
            print "current stroke position: %f" % currentStroke
            if(length>0):                
                if(currentStroke+length)<fullStroke:   #  if we can perform this motion just by pushing the current panel, just do it
                    print "we can do this just by pushing the current backing"
                    if(currentStroke<strokeLead):
                        advance=strokeLead-currentStroke
                        cmd="G0X"+str(advance)+chr(13)
                        if __debug__:
                            ser.write(cmd)
                            flushReceiveBuffer()
                        currentStroke=strokeLead
                        
                    cmd="G0X"+str(length)+chr(13)
                    if __debug__:
                        ser.write(cmd)
                        flushReceiveBuffer()
                    currentStroke=currentStroke+length
                    incrementPoints(length)
                    mysqlString="UPDATE panel_panel set strokePosition=\"%f\" where id='1'" % currentStroke
                    print mysqlString
                    cur.execute(mysqlString) 
                else:
                    while(currentStroke+length)>=fullStroke:
                        print "we need to push at least two different backings to move this far"
                        remaining=fullStroke-currentStroke
                        cmd="G0X"+str(remaining)+chr(13)   #push what you can with the current panel
                        if  __debug__:
                            ser.write(cmd)
                            flushReceiveBuffer()
                        length=length-remaining
                        print cmd
                        incrementPoints(remaining)

                        cmd="G0X-"+str(fullStroke)+chr(13)  #retract the pusher all the way
                        if  __debug__:
                            ser.write(cmd)
                            flushReceiveBuffer()
                        print cmd
 
                        cmd="G0X"+str(strokeLead+strokeEnd)+chr(13)  #advance the pusher until it's contacting the next panel
                        if  __debug__:
                            ser.write(cmd)
                            flushReceiveBuffer()

                        print cmd
                        currentStroke=strokeLead+strokeEnd
                    #now we've pushed all the full panels we need to push, and we just finish the last panel
                    cmd="G0X"+str(length)+chr(13)  #push the remaining distance
                    if  __debug__:
                        ser.write(cmd)
                        flushReceiveBuffer()
                    currentStroke+=length
                    incrementPoints(length)
                    mysqlString="UPDATE panel_panel set strokePosition=\"%f\" where id='1'" % currentStroke
                    print mysqlString
                    cur.execute(mysqlString) 
            else:
                cmd="G0X"+str(length)+chr(13)  #advance the pusher until it's contacting the next panel
                print cmd
                if __debug__:
                    ser.write(cmd)
                    flushReceiveBuffer()
                currentStroke+=length
                mysqlString="UPDATE panel_panel set strokePosition=\"%f\" where id='1'" % currentStroke
                cur.execute(mysqlString) 
        except:
            traceback.print_exc(file=sys.stdout)            
            print "trouble getting the panel info from the database"
            pass

def startup():
    """called on startup to pull all the init commands for the tinyG from the server and send them to the G"""
    url = "http://testing.solarpocketfactory.com/startup/"
    req = urllib2.Request(url)
    urldata = urllib2.urlopen(req)
    GCode = urldata.read()
    executeCommand(GCode)
                         
def incrementPoints(length):
    """called after every conveyor motion to keep track of where all the points moved to"""
    with spfdb:
        cur = spfdb.cursor()
        points=cur.execute("select * from point_point")
        for row in cur:
            try:
                point = fetchoneDict(cur)
                print point
                id=point['id']
                position=float(point['position'])
                remainingDistance=float(point['remainingDistance'])
                position+=length
                remainingDistance-=length
                str = "UPDATE point_point set position='%f',remainingDistance='%f' where id='%s'" % (position, remainingDistance, id)
                update=spfdb.cursor()
                print str
                update.execute(str)
            except Exception as e:   # no waiting commands
                print e

def executeAll():
    with spfdb:
        cur = spfdb.cursor()
        result=cur.execute("select * from point_point")
        for point in cur:
            pointAction()


def pointAction():   
    """move to next point in list and do something there"""
    with spfdb:
        cur = spfdb.cursor()
        cur.execute("select * from point_point order by remainingDistance ASC")
        try:
            point = fetchoneDict(cur)
            print point
            if point['pointType']!="start" and point['pointType']!="end":
                moveConveyor(float(point['remainingDistance']))
            executeCommand(point['code'])
            cur.execute("delete from point_point where id='%s'" % point['id'])
        except:
            print "no points in queue"
            

def pullCommands():
    print("checking database")
    with spfdb:
        cur = spfdb.cursor()
        cur.execute("select * from command_command where status=\"queued\"")
        try:
            row = fetchoneDict(cur)
            print row
            id=row['id']
            GCode = row['json']
            str = "UPDATE command_command set status=\"executed\" where id='%s'" % id
            if GCode.find("update")==-1:
                executeCommand(GCode)
                print str
                cur.execute(str)
            else:
                print str
                cur.execute(str)
                update()

        except Exception as e:   # no waiting commands
            print "no pending commands"
            for point in points:
                print point

def executeCommand(GCode):
    print("json code:  " + GCode)
    print GCode.split()
    for cmd in GCode.split():
        print "executing command:  %s" % cmd
        cmd=cmd.replace("_", " ") #if we need a command with a space, use an underscore in the templates
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
            elif(substr == '19'):
                lightsOn()
            elif(substr == '20'):
                lightsOff()
        elif(cmd.find("executeAll")!=-1):
            executeAll()
        elif(cmd.find("execute")!=-1):
            pointAction()

            
        elif(cmd[0]=='M'):  #conveyor command
            length=cmd[1:]  # the rest of the command is the distance that the conveyor should move
            moveConveyor(float(length))
        elif(cmd[0]=='P'):  #soldering power command
            power=cmd[1:]  # the rest of the command is the soldering power, from 0-100
            setSolderingPower(int(power))
        elif(cmd[:3]=="G4P"):   #  intercept a sleep GCode command and run it on the pi rather than the G
            delay=float(cmd[3:])/1000
            print delay
            time.sleep(delay)
        elif(cmd == 'g28.1'):
            cmd = parsable + chr(13)
            print cmd
            if __debug__:
                ser.write(cmd)
                flushReceiveBuffer()
            break
        else:
            cmd = cmd + chr(13)
            print cmd
            if __debug__:
                ser.write(cmd)
                flushReceiveBuffer()

def restart():
    command = "/usr/bin/sudo /sbin/shutdown -r now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print output

def update():    
    req = urllib2("https://raw.github.com/enjrolas/SPF/testing/SPF.py")
    try:
        response = urlopen(req)
    except HTTPError as e:
        print 'The server couldn\'t fulfill the request.'
        print 'Error code: ', e.code
    except URLError as e:
        print 'We failed to reach a server.'
        print 'Reason: ', e.reason
    else:
        SPF=open('SPF.py','w')
        SPF.write(response.read())
        SPF.close()
        restart()

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

try:
    print("pulling startup script to init tinyG")
    if __debug__:
        startup()
    print("initialized and ready to go")
    while(True):
        pullCommands()
        time.sleep(1)

except KeyboardInterrupt:
    hardwareCleanup()
