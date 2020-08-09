import RPi.GPIO as GPIO
from RpiMotorLib import rpiservolib
import time
servoPin = 17
feeder_servo = rpiservolib.SG90servo("feeder")
feeder_servo.servo_move(servoPin,1)
move = 0
while move !=-1:
    move = float(input())
    feeder_servo.servo_move(servoPin,move)
    print(move)
    time.sleep(1)
    feeder_servo.servo_move(servoPin,1)
  
   



