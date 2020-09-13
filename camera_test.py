# Author : nadavschwalb@mail.tau.ac.il
#test pi camera - saves a 3 second video and a picture to the puzzlebox_data/captures folder 
#with time stamp and video test lable
from picamera import PiCamera
import time
import os
user = os.environ["USER"]
#instantiate camera object 
camera = PiCamera()
camera.resolution = (1024,768)
time.sleep(0.2)
#preview cannot be seen when SSHing into pi
camera.start_preview()
time.sleep(0.5)
# you can use a relative path instead of an absoult path 
capture_directory = "/home/"+ user + "/puzzlebox_data/captures" 
timeStamp = +time.strftime("%a %d-%m-%y %H:%M:%S",time.localtime()) 
save_str = capture_directory +"/"+ "cam-test " + timeStamp + ".jpg"
camera.capture(save_str)
save_str =capture_directory +"/" + "video test "+ timeStamp + ".h264"
# .h264 is the standard raspi camera file type, you can choose to convert it before saving
# but to save the pi proccessing power I would convert them server side
camera.start_recording(save_str)
time.sleep(3)
camera.stop_recording()
camera.stop_preview()
camera.close()
