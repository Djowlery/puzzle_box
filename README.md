# puzzle_box
repository for puzzle box TAU zoological center
Author: nadavschwalb@mail.tau.ac.il

1) when first cloning this repository to a new rasperry pi run the setup script
by running 'bash setup.sh' in the puzzle_box directory, this will install the needed dependencies and setup the filesystem for logging and image capture

2) the repository contains test scripts for the door motor, IR limit switches, feeder servo and camera

3) puzzlebox_main.py is the main script that will run the puzzle box. in order to run the script automaticly when the raspberry pi boots run the command
'sudo echo "sudo python3 /home/$USER/(path to repository)/puzzlebox_main.py &" | tee - a /etc/rc.local'
