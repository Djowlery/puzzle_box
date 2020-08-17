import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
from time import sleep
print("test started")
GpioPins = [4, 23 ,24, 25]
fullRotation = 512
motor = RpiMotorLib.BYJMotor("TestMotor", "28BYJ")
while True:
    command = input()
    if command == 'pull':
        rotation = input("enter a number to pull back from 0 - 1:")
        rotation = round(float(rotation)*fullRotation)
        motor.motor_run(GpioPins,0.001,rotation,False,False,"half",.001)
        sleep(0.5)
    elif command == 'center':
        motor.motor_run(GpioPins,0.001,rotation,True, False,"half",.001)
    elif command == 'quit':
        print("calibration complete")
        break
        



print("test finished")


