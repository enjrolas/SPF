#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import sys
import serial
import time
import re
import sys, traceback
from factory import Point, Panel
from hardware import *
import pickle
import urllib, urllib2


points=[] #  

### safe the solderer, for safety's safe
solderingStationOff()
solderingStationUp()
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
            conveyorHeadPosition=float(row['conveyorHeadPosition'])
            print "current stroke position: %f" % currentStroke
            print "conveyor head position: %f" % conveyorHeadPosition
            if(length>0):                
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
                    incrementPoints(length)
                    mysqlString="UPDATE panel_panel set strokePosition=\"%f\", conveyorHeadPosition=\"%f\" where id='1'" % (currentStroke, conveyorHeadPosition)
                    print mysqlString
                    cur.execute(mysqlString) 
                else:
                    while(currentStroke+length)>=fullStroke:
                        print "we need to push at least two different backings to move this far"
                        remaining=fullStroke-currentStroke
                        cmd="G0X"+str(remaining)+chr(13)   #push what you can with the current panel
                        ser.write(cmd)
                        flushReceiveBuffer()
                        length=length-remaining
                        print cmd
                        incrementPoints(remaining)

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
                    currentStroke+=length
                    incrementPoints(length)
                    mysqlString="UPDATE panel_panel set strokePosition=\"%f\", conveyorHeadPosition=\"%f\" where id='1'" % (currentStroke, conveyorHeadPosition)
                    print mysqlString
                    cur.execute(mysqlString) 
                    print "conveyor head position: %f" % conveyorHeadPosition                    
            else:
                cmd="G0X"+str(length)+chr(13)  #advance the pusher until it's contacting the next panel
                print cmd
                ser.write(cmd)
                flushReceiveBuffer()        
                currentStroke+=length
                conveyorHeadPosition+=length
                mysqlString="UPDATE panel_panel set strokePosition=\"%f\", conveyorHeadPosition=\"%f\" where id='1'" % (currentStroke, conveyorHeadPosition)
                cur.execute(mysqlString) 
        except:
            traceback.print_exc(file=sys.stdout)            
            print "trouble getting the panel info from the database"
            pass

def startup():
    """called on startup to pull all the init commands for the tinyG from the server and send them to the G"""
    url = "http://internal.solarpocketfactory.com/startup/"
    req = urllib2.Request(url)
    urldata = urllib2.urlopen(req)
    GCode = urldata.read()
    executeCommand(GCode)
                         
def incrementPoints(length):
    """called after every conveyor motion to keep track of where all the points moved to"""
    for point in points:
        point.position+=length
        point.remainingDistance-=length
    sortPoints()

def sortPoints():  
    """keep track of which points are still active and keep the list sorted by remaining distance"""
#    points[:]=[point for point in points if point.remainingDistance>0] #get rid of points that have dropped off the edge of the earth/conveyor
    points.sort(key=lambda point: point.remainingDistance)  #sort the list, closest objects first


def executeAll():
    while len(points)>0:
        pointAction()

def pointAction():   
    """move to next point in list and do something there"""
    if len(points)>0:
        currentPoint=points.pop(0)
        if currentPoint.pointType!="start" and currentPoint.pointType!="end":
            moveConveyor(currentPoint.remainingDistance)
            executeCommand(currentPoint.code)


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
            executeCommand(GCode)
            str = "UPDATE command_command set status=\"executed\" where id='%s'" % id
            print str
            cur.execute(str)
        except Exception as e:   # no waiting commands
            print "no pending commands"
            for point in points:
                print point

def addPoint(cmd):
    print "adding a point of interest"
    if(cmd.find(":")!=-1):
        parts=cmd.split(":")
        print parts
        point=Point()
        point.pointType=parts[1]
        params={'actionType':point.pointType}
        print params
        print point
        url="http://internal.solarpocketfactory.com/renderAction/"
        data=urllib.urlencode(params)
            # create your HTTP request                                                      
        headers = { 'User-Agent' : 'solarPocketFactory',
                    'Content-Type':'text/html; charset=utf-8',
                    }
        html=""
        try:
            req = urllib2.Request(url, data, headers)
            print "submitting request"
            response = urllib2.urlopen(req)
            html = response.read()
            print html
            print "that's my HTML and I'm sticking to it"
        except:
            print "Unexpected error:", sys.exc_info()[0]
        point.code=html
        positionPoints=sorted(points, key=lambda point:point.position)
        print "positionPoints:"
        for aPoint in positionPoints:
            print aPoint
        print "there are "+str(len(positionPoints)) + " position points"
        if len(positionPoints)>0:
            print "got some points!"
            lastPoint=positionPoints[0]
            print lastPoint.position
            print parts[2]
            point.position=lastPoint.position+float(parts[2])
        else:
            point.position=float(parts[2])
            if point.pointType=="start":
                print "remaining stroke is: "+str(getRemainingStroke())
                point.position-=getRemainingStroke()           

            
        #delete this hardcoded bullshit later and put in something better
        if(point.pointType=="start"):
            point.remainingDistance=655-point.position
        elif(point.pointType=="solder"):
            point.remainingDistance=443-point.position
        elif(point.pointType=="tab"):
            point.remainingDistance=311-point.position
        elif(point.pointType=="placeSolette"):
            point.remainingDistance=316-point.position
        elif(point.pointType=="test"):
            point.remainingDistance=527-point.position
        elif(point.pointType=="end"):
            point.remainingDistance=655-point.position
        points.append(point)
        sortPoints()
        print "point appended"
        for aPoint in points:
            print aPoint
        print "done!"

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
        elif(cmd.find("point")!=-1):
            addPoint(cmd)
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
    startup()
    print("initialized and ready to go")
    while(True):
        pullCommands()
        time.sleep(1)

except KeyboardInterrupt:
    hardwareCleanup()
