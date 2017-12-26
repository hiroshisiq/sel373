import RPi.GPIO as GPIO
import time

class GPIOControl():

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.OUT)

    def openDoor(self):
        GPIO.output(11,GPIO.HIGH)
        time.sleep(2)
        GPIO.output(11,GPIO.LOW)
	return
