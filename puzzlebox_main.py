# Author : nadavschwalb@mail.tau.ac.il
# main scrip running the puzzlebox 
# tests camera and motor on startup
# creates session log file
# apon door opening the door closes after the delay set in door_delay
# captures a video untill the door is closed and saves the video with a timestamp

#imports
from picamera import PiCamera
import time
import os
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
import threading
import sys
import asyncio

#functions
async def arrived(delay, timestamp):
    await capture(timestamp,delay)
    print("departed")
    

async def close_door(delay):
    await asyncio.sleep(delay)
    doorMotor.motor_run(DM_Pins,0.001,fullRotation/4,False,False,"half",.001)
    time.sleep(0.5)
    doorMotor.motor_run(DM_Pins,0.001,fullRotation/4,True, False,"half",.001)
    print("door closed")
    
async def capture(timestamp,delay):
    print("capture started")
    camera.start_recording(capture_dir+"/"+timestamp+".h264",format='h264')
    count = 0
    await close_door(delay)
    while GPIO.input(IR_L_pin) or GPIO.input(IR_R_pin) or count > 50:
        time.sleep(0.3)
        count += 1
    time.sleep(1)
    camera.stop_recording()
    print("capture finnished")
    
    

#objects
user = os.environ["USER"]
camera = PiCamera()
doorMotor = RpiMotorLib.BYJMotor("TestMotor", "28BYJ")
capture_dir = "/home/"+ user + "/puzzlebox_data/captures"
timeStamp = time.strftime("%a-%d-%m-%y-%H-%M-%S",time.localtime())
log_dir = "/home/" + user + "/puzzlebox_data/log"
IR_L_pin = 21
IR_R_pin = 26
door_delay  = 3

#objects setups
camera.resolution = (1024,768)
logFileName = log_dir+"/"+"log-file "+timeStamp+".txt"
logFile = open(logFileName,'w')
DM_Pins = [4, 17 ,23, 24]
fullRotation = 512
GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_L_pin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(IR_R_pin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#log file
logFile.write("log session started at "+ timeStamp +"\n")


#test camera
camera.start_preview()
time.sleep(0.5)
save_str = capture_dir +"/"+"cam-test "+timeStamp+".jpg"
camera.capture(save_str)
camera.stop_preview()
logFile.write("camera test finished\n")


#test mototrs
doorMotor.motor_run(DM_Pins,0.001,fullRotation/4,False,False,"half",.001)
time.sleep(0.5)
doorMotor.motor_run(DM_Pins,0.001,fullRotation/4,True, False,"half",.001)
logFile.write("motor test finished\n")


#main loop
try:
    loop = asyncio.get_event_loop()
    print("loop started")
    while True:
        if GPIO.input(IR_R_pin):
            print("right")
            timeStamp = timeStamp = time.strftime("%a-%d-%m-%y-%H-%M-%S",time.localtime())
            logFile.write("opened right " + timeStamp +"\n")
            loop.run_until_complete(arrived(door_delay,timeStamp))
        

        elif GPIO.input(IR_L_pin):
            print("left")
            timeStamp = timeStamp = time.strftime("%a-%d-%m-%y-%H-%M-%S",time.localtime())
            logFile.write("opened left " + timeStamp+"\n")
            loop.run_until_complete(arrived(door_delay,timeStamp))
         
        else:
            pass
except KeyboardInterrupt:
    print("keyboard interrupt caught")
                
#cleanup
    logFile.write("log session closed")
    logFile.close()
    GPIO.cleanup()
        
    

