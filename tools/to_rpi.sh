#!/bin/bash

echo "beginning upload of code to target : rpi ..."

scp -r ../rpi_python_opencv/ pi@192.168.0.197:/home/pi/Project/IDAE_Workshop/

