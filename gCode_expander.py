#!/usr/bin/python
# -*_ coding: utf-8 -*-

import MySQLdb as mdb
import sys
import time
import urllib2
from thread import start_new_thread
import re

config = open('config.spf', 'r')
config_remote = config.read().split('=')
if config_remote[1] == 'true\n':
    url = "http://internal.solarpocketfactory.com/newCommands/"
elif config_remote[1] == 'false\n':
    url = "http://solarpocketfactory.com:80/newCommands/"
else:
    print "invalid value for \'remote\' in config.spf"
    sys.exit()

print "url = %s" %url

#spfdb = mdb.connect('localhost', 'root', 'ms', 'spfdb')
spfdb = mdb.connect(host='localhost', user='root', passwd='ms')
with spfdb:
    cur = spfdb.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS spfdb")
    cur.execute("GRANT ALL ON spfdb.* TO tinyg@localhost IDENTIFIED BY \'ms\'")
    cur.execute("USE spfdb")
    cur.execute("CREATE TABLE IF NOT EXISTS \
                Jobs(JOB TEXT)")

def insertCommand(gCode):
    MYSQL_QUERY = "INSERT INTO Jobs(JOB) VALUES(\'%s\')" % gCode
    print MYSQL_QUERY
    cur.execute(MYSQL_QUERY)


def expandCmd():
    with spfdb:
        req = urllib2.Request(url)
        urldata = urllib2.urlopen(req)
        response = urldata.read()

        if(response != "queue_empty"):
            print response
            response=response.strip()
            response = re.sub("\n", " ", response)
            payload = response.split('<br/>')
            print payload
            print len(payload)
            for job in payload:
                if job!='':
                    field = job.split(',')
                    if(field[0] == "placePanel"):
                        voltage            = field[1]
                        quantity            = field[2]
                        panelBeginning      = field[5]
                        placeSolette        = field[6]
                        panelEnding         = field[7]
                        
                        qty = int(quantity)
                        volts = float(voltage)

                        for i in range(0,qty):
                            rawGcode = panelBeginning
                            for j in range(0,int(volts/0.5)):
                                rawGcode = rawGcode + placeSolette
                                rawGcode = rawGcode + panelEnding
                    elif(len(field) > 1):
                        rawGcode = field[5]

                    if(rawGcode.find('g28.1') < 0):
                        commands = rawGcode.split()
                        for command in commands:
                            insertCommand(command)

                    else:
                        insertCommand(rawGcode)

while(True):
#    start_new_thread(expandCmd, ())
    print "fetching command"
    expandCmd()
    time.sleep(1)

