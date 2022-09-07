#!/usr/bin/env python3
from optparse import OptionParser
import argparse
import time
import Adafruit_ADS1x15
import sys

gain_ref_dict = {0: 6.144, 1: 4.096, 2: 2.048, 3: 1.024, 4: 0.512, 5: 0.256}

usage = "./test_ads1115 [options] [port]"
parser = OptionParser(usage=usage)

parser.add_option("-a", "--address", type="int", action="store", dest="address", default=0x4b,
                  help="Address of the ADS1115 in the bus (defaults to 0x4b)")
parser.add_option("-b", "--bus", type="int", action="store", dest="bus", default=1,
                  help="I2C channel (0 or 1,defaults to 1)")
# parser.add_option("-c", "--count", type="int", action="store", dest="count", default=5,
#                   help="How many times to query the ADS1115 (any natural number, defaults to 5, 0 means forever until "
#                        "keyboard break)")
parser.add_option("-d", "--delay", type="int", action="store", dest="delay", default=200,
                  help="How often to query the ADC in ms (100 to 10000, defaults to 1000)")
parser.add_option("-g", "--gain", type="int", action="store", dest="gain", default=0,
                  help=" Gain (value from 0 to 5, defaults to 0)")

(options, args) = parser.parse_args()

# Create an ADS1115 ADC (16-bit) instance.
addr = options.address
bus = options.bus

adc = Adafruit_ADS1x15.ADS1115(address=addr, busnum=bus)
# if len(args) == 0:
#     print("argument 'port' is mandatory")
#     sys.exit()

# port = int(args[0])
# if port in range(0, 4):
#     pass
# else:
#     print("Error: port must be in the range 0 to 3")
#     sys.exit()

if options.gain in range(0, 6):
    pass
else:
    print("Error: gain must be in the range 0 to 5")
    sys.exit()

gain_map = {0: 2 / 3, 1: 1, 2: 2, 3: 4, 4: 8, 5: 16}
GAIN = gain_map.get(options.gain)

'''
set a gain of 1 for reading voltages from 0 to 4.09V.
Or pick a different gain to change the range of voltages that are read:
  - 2/3 = +/-6.144V
  -   1 = +/-4.096V
  -   2 = +/-2.048V
  -   4 = +/-1.024V
  -   8 = +/-0.512V
  -   16 = +/-0.256V
'''
gain_ref_dict = {2 / 3: 6.144, 1: 4.096, 2: 2.048, 4: 1.024, 8: 0.512, 16: 0.256}
volt_ref = gain_ref_dict.get(GAIN)

count = 5
for i in range(1, count + 1):
    print("ADC Test", i, " result, should all be close to 3.3V")
    for port in range(0, 4):
        value = adc.read_adc(port, gain=GAIN)
        # print(value)
        volt = value * volt_ref / 32767
        print("ADC_IN", port, " reading: {:.2f}V".format(volt))
        time.sleep(int(options.delay) / 1000)
    print(" ")
