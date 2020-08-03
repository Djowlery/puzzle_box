import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

GpioPins = [18, 23 ,24, 25]
motor = RpiMotorLib.BYJMotor("TestMotor", "28BYJ")
motor.motor_run(GpioPins,0.001,512,False,False,"half",.001)

