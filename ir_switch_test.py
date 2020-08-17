import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
IRL_pin = 21
GPIO.setup(IRL_pin,GPIO.IN)

while True:
    if GPIO.input(IRL_pin):
        print("blocked")
    else:
        print("open")
    sleep(0.1)
    
GPIO.cleanup()