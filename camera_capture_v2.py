##----------------------------------------------------------------------------------------
##  Camera Capture Program v2.00
##----------------------------------------------------------------------------------------
##  Written by Pacess HO
##  Copyright Pacess Studio, 2020.  All rights reserved.
##----------------------------------------------------------------------------------------

from picamera import PiCamera
from time import sleep
import shutil
import os

##----------------------------------------------------------------------------------------
##  Variables
fullPath = '/home/pi/Pictures/capture/'

timestampFilePath = fullPath+'capture.timestamp'
try:
	with open(timestampFilePath, 'r') as filehandler:
		counter = int(filehandler.read())
		filehandler.close()

except IOError:
	counter = 1

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

imageFile = str(counter)+'.jpg'
filePath = fullPath+imageFile
camera.capture(filePath)

##----------------------------------------------------------------------------------------
##  Adjust counter
counter = counter+1
if (counter > 1000):
	counter = 1

try:
	with open(timestampFilePath, 'w') as filehandler:
		filehandler.write(str(counter))
		filehandler.close()

except IOError:
	counter = 1
