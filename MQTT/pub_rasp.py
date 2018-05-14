# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 20:38:18 2018

@author: Paulo Augusto
"""

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

BOTAO = 12

def on_publish(mosq, userdata, mid):
    mosq.disconnect()

client = mqtt.Client()
client.on_publish = on_publish
GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)
GPIO.setup(BOTAO, GPIO.IN)

while True:
    if(GPIO.input(BOTAO)):
        client.connect("143.107.235.44", 1883, 60)
        client.publish("TeleScope","BOTAO")
        time.sleep(1)

#im=open("nova.bmp", "rb") #3.7kiB in same folder
#fileContent = im.read()
#byteArr = bytearray(fileContent)
#
#
#client.publish("image","Hello",0)

client.loop_forever()
