from picamera import PiCamera
import time
import os

camera = PiCamera()
camera.resolution = (1024,768)
time.sleep(0.2)
#camera.start_preview()
time.sleep(0.5)
capture_directory = "/home/pi/puzzlebox_data/captures"
timeStamp = "cam-test "+time.strftime("%a %d-%m-%y %H:%M:%S",time.localtime()) 
save_str = capture_directory +"/"+timeStamp+".jpg"
camera.capture(save_str)
save_str =capture_directory +"/" + "video test "+timeStamp+".h264"
camera.start_recording(save_str)
time.sleep(3)
#camera.stop_recording()
camera.stop_preview()
camera.close()
