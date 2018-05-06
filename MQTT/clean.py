import RPi.GPIO as GPIO  

B1  = 11
B2  = 12

GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)
GPIO.setup(B1, GPIO.IN)
GPIO.setup(B2, GPIO.IN)




GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
           # clean up GPIO on normal exit 
