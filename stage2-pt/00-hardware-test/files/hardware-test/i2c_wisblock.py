#!/usr/bin/env python3
"""
Blinks an LED at 1Hz for 5 seconds, using the RAK13003 module
"""
__copyright__ = "Copyright 2022, RAKwireless"
__license__ = "GPL"
__version__ = "1.0.0"
__status__ = "Production"
__maintainer__ = "rakwireless.com"

import time
import board
import busio
import digitalio
from adafruit_mcp230xx.mcp23017 import MCP23017
import gpiod

reset_pin_slot1 = 4
reset_pin_slot2 = 12

chip = gpiod.chip(3)
line1 = chip.get_line(reset_pin_slot1)
line2 = chip.get_line(reset_pin_slot2)
config = gpiod.line_request()
config.request_type = gpiod.line_request.DIRECTION_OUTPUT

line1.request(config)
line1.set_value(1)
time.sleep(0.1)
line1.set_value(0)
time.sleep(0.1)
line1.set_value(1)
time.sleep(0.1)

line2.request(config)
line2.set_value(1)
time.sleep(0.1)
line2.set_value(0)
time.sleep(0.1)
line2.set_value(1)
time.sleep(0.1)

i2c = busio.I2C(board.SCL, board.SDA)
mcp = MCP23017(i2c, address=0x24, reset=True)

for i in range(0, 10):
    pin = mcp.get_pin(i)
    pin.switch_to_output(value=True)
    pin.value = True
    time.sleep(0.5)
    pin.value = False
    time.sleep(0.5)

mcp = MCP23017(i2c, address=0x24, reset=True)

