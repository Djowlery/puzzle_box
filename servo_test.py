import RPi.GPIO as GPIO
from RpiMotorLib import rpiservolib
import time
servoPin = 17
feeder_servo = rpiservolib.SG90servo("feeder")

while True:
    feeder_servo.servo_move(servoPin,12)
    time.sleep(0.5)
    feeder_servo.servo_move(servoPin,2)

except KeyboardInterrupt:
    print("servo test terminated")
    GPIO.cleanup()