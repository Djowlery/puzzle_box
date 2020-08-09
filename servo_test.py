import RPi.GPIO as GPIO
from RpiMotorLib import rpiservolib
import time
servoPin = 17
servoStart = 1
movePull = 6
holdTime = 1
servoDelay = 1
feeder_servo = rpiservolib.SG90servo("feeder")
feeder_servo.servo_move(servoPin,servoStart)

move = ''
while True:
    move = input()
    if move == 'm':
        feeder_servo.servo_move(servoPin,movePull,servoDelay)
        time.sleep(holdTime)
        feeder_servo.servo_move(servoPin,servoStart,servoDelay)
    else:
        continue

  
   



