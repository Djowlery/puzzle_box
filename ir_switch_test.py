import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.IN)

while True:
    if GPIO.input(25):
        print("blocked")
    else:
        print("open")
    sleep(0.1)
    
GPIO.cleanup()