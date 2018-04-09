import RPi.GPIO as GPIO
import time

class GPIOControl():
    BELL    =   11
    PORTAO  =   12

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(PORTAO, GPIO.OUT)

    def openDoor():
        GPIO.output(PORTAO,GPIO.HIGH)
        time.sleep(2)
        GPIO.output(PORTAO,GPIO.LOW)
