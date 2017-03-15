import serial
import socket

UDP_IP = "157.253.216.113"
UDP_PORT = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

with serial.Serial('/dev/rfcomm0', 9600, timeout=10) as ser:	
	x = ser.read()          # read one byte
	s = ser.read(10)        # read up to ten bytes (timeout)
	while True:
		line = ser.readline()   # read a '\n' terminated line
		sock.sendto(line, (UDP_IP, UDP_PORT))
		print line
