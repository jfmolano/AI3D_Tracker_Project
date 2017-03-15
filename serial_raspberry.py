import serial

with serial.Serial('/dev/rfcomm0', 9600, timeout=10) as ser:	
	x = ser.read()          # read one byte
	s = ser.read(10)        # read up to ten bytes (timeout)
	while True:
		line = ser.readline()   # read a '\n' terminated line
		print line
