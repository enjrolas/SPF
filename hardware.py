"""  
This file defines all the helper functions to interface
between the raspberry pi and the solar pocket factory
The functions control the solenoids and the solderer
"""

import RPi.GPIO as GPIO
from pizypwm import *

""" pin definitions on the raspberry pi"""
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

#set up the soldering power PWM output
solderingPower = PiZyPwm(100, SOLDERING_POWER, GPIO.BOARD)
solderingPower.start(100)


def solderingStationOn():
    print("solderingStationOn()")
    GPIO.output(SOLDERING_ENABLE, True)

def solderingStationOff():
    print("solderingStationOff()")
    GPIO.output(SOLDERING_ENABLE, False)

def setSolderingPower(power):
    print "setting soldering power to %d" % power
    solderingPower.changeDutyCycle(100-power)

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

def lightsOn():
    print("lightsOn()")
    GPIO.output(TEST_LIGHTS, True)

def lightsOff():
    print("lightsOff()")
    GPIO.output(TEST_LIGHTS, False)

def hardwareCleanup():
    GPIO.cleanup()
