# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 08:30:36 2018

@author: Paulo Augusto
"""

"""
USE SU TO RUN THIS SCRIPT
"""

import RPI.GPIO as GPIO

GPIO.setmode(GPIO.BCM) 
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(23, GPIO.FALLING, callback=my_callback, bouncetime=300)  

def my_callback(channel):  
    print "Got something"

RPIO.wait_for_interrupts(threaded=True)
while True:
    
GPIO.clean_up()