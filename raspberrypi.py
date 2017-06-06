#!/usr/bin/env python
from gpiozero import MotionSensor
from picamera import Picamera
from datetime import datetime

pir = MotionSensor(4)
camera = PiCamera()

while True:
    pir.wait_for_motion()
    filename = datetime.now().strftime("%Y-%m-%d_%H.%M.%S.h264")
    camera.start_recording(filename)
    pir.wait_for_no_motion()
    camera.stop_recording()

    
