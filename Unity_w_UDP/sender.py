import socket
import time

UDP_IP = "157.253.204.75"
UDP_PORT = 8080
MESSAGE = "10"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
delay = 0.5

while True:
	sock.sendto("1", (UDP_IP, UDP_PORT))
	time.sleep(delay)
	sock.sendto("2", (UDP_IP, UDP_PORT))
	time.sleep(delay)
	sock.sendto("3", (UDP_IP, UDP_PORT))
	time.sleep(delay)
	sock.sendto("4", (UDP_IP, UDP_PORT))
	time.sleep(delay)
	sock.sendto("3", (UDP_IP, UDP_PORT))
	time.sleep(delay)
	sock.sendto("2", (UDP_IP, UDP_PORT))
	time.sleep(delay)
	sock.sendto("1", (UDP_IP, UDP_PORT))
	time.sleep(delay)
	sock.sendto("-1", (UDP_IP, UDP_PORT))
	time.sleep(delay)
	print "done"