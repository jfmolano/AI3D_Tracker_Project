import socket
import time

UDP_IP = "157.253.213.109"
UDP_PORT = 8080
MESSAGE = "10"

#print "UDP target IP:", UDP_IP
#print "UDP target port:", UDP_PORT
#print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
delay = 0.1

while True:
	sock.sendto(raw_input('Input '), (UDP_IP, UDP_PORT))
	time.sleep(delay)
	print("done")
