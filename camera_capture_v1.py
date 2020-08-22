##----------------------------------------------------------------------------------------
##  Camera Capture Program v1.00
##----------------------------------------------------------------------------------------
##  Written by Pacess HO
##  Copyright Pacess Studio, 2020.  All rights reserved.
##----------------------------------------------------------------------------------------

from picamera import PiCamera
from datetime import datetime
from time import sleep
import shutil
import os

##----------------------------------------------------------------------------------------
##  Variables
today = datetime.now()
folder = today.strftime('%Y%m%d')
fullPath = '/home/pi/Pictures/'+folder+'/'

##----------------------------------------------------------------------------------------
##  Check if enough space, keep at least 500MB
total, used, free = shutil.disk_usage('/')
if (total < 500000000):
	exit()

##----------------------------------------------------------------------------------------
##  Create folder
if (os.path.isdir(fullPath) == False):
	os.mkdir(fullPath)

##----------------------------------------------------------------------------------------
##  Capture process
camera = PiCamera()
camera.resolution = (2592, 1944)

##  Camera warm-up time
camera.start_preview()
sleep(2)

filename = today.strftime('%H%M%S')+'.jpg'
filePath = fullPath+filename
camera.capture(filePath)

