##----------------------------------------------------------------------------------------
##  Camera Capture Server v1.00
##----------------------------------------------------------------------------------------
##  Platform: Raspberry Pi Zero W + Python 3.7
##  Written by Pacess HO
##  Copyright Pacess Studio, 2020.  All rights reserved.
##----------------------------------------------------------------------------------------

from gpiozero import CPUTemperature
from picamera import PiCamera
from datetime import datetime
from flask import send_file
from time import sleep
import shutil
import flask
import os

##----------------------------------------------------------------------------------------
##  Global variables
_folder = "/home/pi/Pictures/capture-server/"

_app = flask.Flask(__name__)
_app.config["DEBUG"] = True

##----------------------------------------------------------------------------------------
##  Take a picture
@_app.route("/api/capture", methods=["GET"])
def apiCapture():
	
	camera = PiCamera()
	#camera.resolution = (2592, 1944)
	camera.resolution = (1296, 972)
	camera.iso = 400

	##  Camera warm-up time
	camera.start_preview()
	sleep(2)

	now = datetime.now()
	hour = int(now.strftime("%H"))

	if (hour >= 7 and hour <= 15):
		camera.iso = 100

	if (hour >= 16 and hour <= 18):
		camera.iso = 200

	timestamp = now.strftime("%Y%m%d_%H%M%S")
	folder = _folder+now.strftime("%Y%m")
	if not os.path.exists(folder):
		os.mkdir(folder)

	imageFile = timestamp+'.jpg'
	filePath = folder+"/"+imageFile
	camera.capture(filePath)
	camera.close()

	return send_file(filePath, mimetype="image/jpeg")

##----------------------------------------------------------------------------------------
##  Show CPU temperature
@_app.route("/api/temperature", methods=["GET"])
def apiCPUTemperature():
	cpu = CPUTemperature()
	return str(cpu.temperature)

##----------------------------------------------------------------------------------------
_app.run(host="0.0.0.0", port=80)
