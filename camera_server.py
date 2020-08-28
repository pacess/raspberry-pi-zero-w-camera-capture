##----------------------------------------------------------------------------------------
##  Camera Capture Server v1.00
##----------------------------------------------------------------------------------------
##  Written by Pacess HO
##  Copyright Pacess Studio, 2020.  All rights reserved.
##----------------------------------------------------------------------------------------

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
@_app.route("/api/capture", methods=["GET"])
def apiCapture():
	
	camera = PiCamera()
	#camera.resolution = (2592, 1944)
	camera.resolution = (1296, 972)

	##  Camera warm-up time
	camera.start_preview()
	sleep(2)

	now = datetime.now()
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
_app.run(host="0.0.0.0", port=80)
