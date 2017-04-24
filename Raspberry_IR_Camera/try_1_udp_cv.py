# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import imutils
import cv2
import socket
import threading
import serial
import codecs

UDP_IP = "157.253.213.109"
UDP_PORT = 8080

#Example line: b'ypr\t56.41\t-16.97\t42.21\r\n'
def get_acc():
	global y
	global p
	global r
	y = 0
	p = 0
	r = 0
	with serial.Serial('/dev/rfcomm0', 9600, timeout=10) as ser:
		x = ser.read()          # read one byte
		s = ser.read(10)        # read up to ten bytes (timeout)
		while True:
			line = ser.readline()   # read a '\n' terminated line
			if line.startswith(bytes("ypr","UTF-8")):
				#print(type(str(line,'utf-8')))
				#print(str(line,'utf-8'))
				str_line = str(line,'utf-8')
				new_line = str_line.replace("\t",";").replace("\r\n",";").replace("ypr","")
				#print(new_line.split(";"))
				arr = new_line.split(";")
				y = float(arr[1])
				p = float(arr[2])
				r = float(arr[3])
				#print((y, p, r))
				#new_line = codecs.decode(str(line,"utf-8"),"unicode_escape").replace(bytes("ypr","UTF-8"),bytes("","UTF-8")).replace(bytes("/r/n","UTF-8"),bytes("","UTF-8"))
				#print(new_line)
			#print(line)

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
 
# allow the camera to warmup
time.sleep(0.1)

t = threading.Thread(target=get_acc)
t.daemon = True
t.start()
 
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
		y_real = (cY - 100.0)*12.0/(300.0)-5.0
		print("x: " + str(cX) + " " + "y: " + str(cY) + " y: " + str(y) + " p: " + str(p) + " r: " + str(r))
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
