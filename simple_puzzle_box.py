from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import time
import RPi.GPIO as IO
from picamera import PiCamera
from datetime import datetime

#setup
red = 25
blue =24
step_number =40
close_delay =1
IO.setwarnings(False)
IO.setmode (IO.BCM)
IO.setup(red,IO.IN,pull_up_down=IO.PUD_DOWN) #GPIO 23 -> IR sensor as input
IO.setup(blue,IO.IN,pull_up_down=IO.PUD_DOWN) #GPIO 24 -> IR sensor as input


#object instantiation
kit = MotorKit()
camera = PiCamera()
kit.stepper1.release()

#main loop
with open("Puzzle_Data.csv", 'a') as puzzle_data:
    
    while True:
        if IO.input(red) == True:
            print("red")
            puzzle_data.write("{},red".format(datetime.now()))
            time.sleep(close_delay)
            for i in range(step_number):
                kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
                time.sleep(0.08)
            for i in range(round(step_number/2)):
                kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
            kit.stepper1.release()
        elif IO.input(blue) == True:
            puzzle_data.write("{},blue".format(datetime.now()))
            print("blue")
            time.sleep(close_delay)
            for i in range(step_number):
                kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
                time.sleep(0.08)
            for i in range(round(step_number/2)):
                kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
            kit.stepper1.release()
        else:
            print("unresolved")
        time.sleep(0.1)
