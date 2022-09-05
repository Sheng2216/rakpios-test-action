#!/usr/bin/env python3
import serial
import time
from random import Random


def random_str(randomlength=32):
    str = ''

    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'

    length = len(chars) - 1

    random = Random()

    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


ser_slot1 = serial.Serial("/dev/ttyUSB0", 115200, timeout=1)
ser_slot2 = serial.Serial("/dev/ttyUSB1", 115200, timeout=1)

while True:
    # receive data
    data_slot2 = ser_slot2.read(128).decode('utf-8')
    if len(data_slot2) > 0:
        print("receive:%s" % data_slot2)
        ser_slot2.write(data_slot2.encode('utf-8'))
        time.sleep(1)
    print(" ")

    # send data
    buf = random_str()
    ser_slot1.write(buf.encode('utf-8'))
    print("send   :%s" % buf)
    time.sleep(1)
