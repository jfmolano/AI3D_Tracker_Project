import serial

<<<<<<< HEAD
with serial.Serial('/dev/rfcomm0', 9600, timeout=10) as ser:	
	x = ser.read()          # read one byte
	s = ser.read(10)        # read up to ten bytes (timeout)
	while True:
		line = ser.readline()   # read a '\n' terminated line
		print line
=======
with serial.Serial('/dev/rfcomm0', 9600, timeout=10) as ser:
	x = ser.read()          # read one byte
	s = ser.read(10)        # read up to ten bytes (timeout)
	line = ser.readline()   # read a '\n' terminated line
	print line
>>>>>>> a8103a95d4802cf6e3355a27f43d440ba6b8a517
