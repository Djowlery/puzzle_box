#Author: nadavschwalb@mail.tau.ac.il
#test ir limit switches

import RPi.GPIO as GPIO
from time import sleep
#make sure you set the pins correctly using the BCM number and not the pin number
GPIO.setmode(GPIO.BCM)
IRL_pin = 21
GPIO.setup(IRL_pin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
IRR_pin = 26
GPIO.setup(IRR_pin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# ininite loop that ouputs the state of the door
while True:
    if GPIO.input(IRL_pin):
        print("left")
    elif GPIO.input(IRR_pin):
        print("right")
    else:
        print("open")
    sleep(0.3)
    
GPIO.cleanup()