# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 20:38:18 2018

@author: Paulo Augusto
"""

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

CHAVE = 12


def on_publish(mosq, userdata, mid):
    mosq.disconnect()

def portao_callback(channel):
        client.publish("TeleScope","PORTAO")

def button_callback(channel):
        print("Button sent")
        client.publish("TeleScope","BOTAO")

client = mqtt.Client()
client.connect("143.107.235.44", 1883, 60)
client.on_publish = on_publish
GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)
GPIO.setup(CHAVE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

time.sleep(1)
#GPIO.add_event_detect(OTHER, GPIO.FALLING, callback=other_callback, bouncetime=300)
GPIO.add_event_detect(CHAVE, GPIO.FALLING, callback=button_callback) # bouncetime=1)


try:
	#time.sleep(6000)
	#GPIO.wait_for_edge(10,GPIO.RISING)
	while True:
		a=1
except KeyboardInterrupt:
	GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
#GPIO.cleanup()           # clean up GPIO on normal exit  
