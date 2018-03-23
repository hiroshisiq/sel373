# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 20:38:44 2018

@author: Paulo Augusto
"""

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

BELL    =   11
PORTAO  =   12


def on_connect(client, userdata, flags,rc):
    
#    print("Connect " + str(rc))
    client.subscribe("TeleScope") 

def on_message(client, userdata, msg):
#    print "Topic : ", msg.topic
    if(msg.payload=="BOTAO"):
        GPIO.output(BELL,GPIO.HIGH)
        time.sleep(2)
        GPIO.output(BELL,GPIO.LOW)
    if(msg.payload=="PORTAO"):
        GPIO.output(PORTAO,GPIO.HIGH)
        time.sleep(2)
        GPIO.output(PORTAO,GPIO.LOW)
#    f = open('image.bmp', 'w+')
#    f.write(msg.payload)
#    f.close()
  
    
GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)
GPIO.setup(PORTAO, GPIO.OUT)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


client.connect("143.107.235.44", 1883, 60)



client.loop_forever()