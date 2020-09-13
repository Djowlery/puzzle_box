#!/bin/bash
cd ~
#create data directories
mkdir /home/$USER/puzzlebox_data
mkdir /home/$USER/puzzlebox_data/captures
mkdir /home/$USER/puzzlebox_data/log

#run update
sudo apt-get update

#install python dependencies
sudo pip3 install Rpi.GPIO
sudo pip3 install rpimotorlib
sudo pip3 install picamera

echo "setup complete"



