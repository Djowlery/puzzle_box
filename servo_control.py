#Author: nadavschwalb@mail.tau.ac.il
#control feeder servo, if you are using a stepper motor this script is easy to modify
# the commands are 'full' - 90 deg open, 'half' - 45 deg open, 'quick' - short delay time , 'close' and 'quit'
import RPi.GPIO as GPIO
from RpiMotorLib import rpiservolib
import time
servoPin = 17
servoStart = 1
movePull = 7
holdTime = 0.4
servoDelay = 0.3
feeder_servo = rpiservolib.SG90servo("feeder")
feeder_servo.servo_move(servoPin,servoStart)

move = ''
while True:
    move = input()
    if move == 'full':
        feeder_servo.servo_move(servoPin,movePull,servoDelay)
        time.sleep(holdTime)
        feeder_servo.servo_move(servoPin,servoStart,servoDelay)
    elif move == 'half':
        feeder_servo.servo_move(servoPin,3.6,servoDelay)
        time.sleep(holdTime)
        feeder_servo.servo_move(servoPin,servoStart,servoDelay)
    elif move == 'quick':
        feeder_servo.servo_move(servoPin,movePull,servoDelay)
        feeder_servo.servo_move(servoPin,servoStart,servoDelay)
    elif move == 'open':
        feeder_servo.servo_move(servoPin,movePull,servoDelay)
        
    elif move == "close":
        feeder_servo.servo_move(servoPin,servoStart,servoDelay)
    elif move == 'quit':
        feeder_servo.servo_move(servoPin,servoStart,servoDelay)
        break
    else:
        continue
print("servo test terminated")


  
   



