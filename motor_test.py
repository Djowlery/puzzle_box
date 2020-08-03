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
