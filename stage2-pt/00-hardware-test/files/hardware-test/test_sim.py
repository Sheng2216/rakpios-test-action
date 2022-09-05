#!/usr/bin/env python3
import serial
import time
import sys

device = "/dev/ttyUSB4"
try:
	ser = serial.Serial(device,115200,timeout=1)
except Exception as e:
	print("ERROR: could not find the module.")
	sys.exit()
#buf="ate0\r\n"
#ser.write(buf.encode())
buf="at+cimi\r\n"
ser.write(buf.encode())
print("send   :%s"%buf)
data = ser.read(size=128).decode()
if "OK" in data:
	data=data.replace('OK','')
	imsi=data.replace('\r\n','')
	print("IMSI :%s"%imsi)
else:
	print("ERROR: could not read imsi data.")

