#main scrip rumming the puzzlebox

#imports
from picamera import PiCamera
import time
import os
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

#objects
camera = PiCamera()
doorMotor = RpiMotorLib.BYJMotor("TestMotor", "28BYJ")
capture_dir = "/home/pi/puzzlebox_data/captures"
timeStamp = time.strftime("%a-%d-%m-%y-%H-%M-%S",time.localtime())
log_dir = "/home/pi/puzzlebox_data/log"
#object setups
camera.resolution = (1024,768)
logFileName = log_dir+"/"+"log-file "+timeStamp+".txt"
logFile = open(logFileName,'w')
DM_Pins = [4, 17 ,23, 24]
fullRotation = 512
#log file
logFile.write("log session started at "+ timeStamp +"\n")


#test camera
camera.start_preview()
time.sleep(0.5)
save_str = capture_dir +"/"+"cam-test "+timeStamp+".jpg"
camera.capture(save_str)
camera.close()
logFile.write("camera test finished\n")


#test mootrs
doorMotor.motor_run(DM_Pins,0.001,fullRotation/4,False,False,"half",.001)
time.sleep(0.5)
doorMotor.motor_run(DM_Pins,0.001,fullRotation/4,True, False,"half",.001)
logFile.write("motor test finished\n")

#main loop


logFile.write("log session closed\n")
logFile.close()
