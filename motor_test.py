#Author: nadavschwalb@mail.tau.ac.il
#test motor 1/4 rotation and outputs to terminal when test is finished
#I used the 28BYJ unipolar stepper motor with the ULN2003 driver board
#if you choose to use a diffrent stepper motor please make sure to use the correct method in RpiMotorLib
#GpioPins are numbered by BCM layout
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
from time import sleep
print("test started")
GpioPins = [4, 17 ,23, 24]
fullRotation = 512
motor = RpiMotorLib.BYJMotor("TestMotor", "28BYJ")
motor.motor_run(GpioPins,0.001,fullRotation/4,False,False,"half",.001)
sleep(0.5)
motor.motor_run(GpioPins,0.001,fullRotation/4,True, False,"half",.001)
print("test finished")


