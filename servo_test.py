import RPi.GPIO as GPIO
from RpiMotorLib import rpiservolib
feeder_servo = rpiservolib.SG90servo("feeder")
feeder_servo.servo_sweep(17)

GPIO.cleanup()