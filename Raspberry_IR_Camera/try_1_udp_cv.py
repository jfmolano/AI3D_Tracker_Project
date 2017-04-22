# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import imutils
import cv2
import socket

UDP_IP = "157.253.213.109"
UDP_PORT = 8080

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
 
# allow the camera to warmup
time.sleep(0.1)
 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array

	gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	ret,thresh1 = cv2.threshold(gray_image,127,255,cv2.THRESH_BINARY)

	cnts = cv2.findContours(thresh1.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0] if imutils.is_cv2() else cnts[1]

	for c in cnts:
		# compute the center of the contour
		M = cv2.moments(c)
		try:
                	cX = int(M["m10"] / M["m00"])
                	cY = int(M["m01"] / M["m00"])
		except:
                	cX = 0
                	cY = 0
	 
		# draw the contour and center of the shape on the image
		cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
		cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
		cv2.putText(image, "center", (cX - 20, cY - 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
		x_real = (cX - 100.0)*12.0/(300.0)-5.0
		print("x: " + str(cX) + " " + "y: " + str(cY) + "x_real: " + str(x_real))
		sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
		sock.sendto(bytes(str(x_real) + ";0","UTF-8"), (UDP_IP, UDP_PORT)) 
	# show the frame
	cv2.imshow("Frame", image)
	key = cv2.waitKey(1) & 0xFF
 
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
