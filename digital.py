#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

TEST_LIGHTS=11
GPIO.setup(TEST_LIGHTS, GPIO.OUT) # test station lights

GPIO.output(TEST_LIGHTS, False)
