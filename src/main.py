import time
from digitalio import *
from board import *
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

# Rotary encoder inputs with pullup on D3 & D4
rot_a = DigitalInOut(D3)
rot_a.direction = Direction.INPUT
rot_a.pull = Pull.UP
rot_b = DigitalInOut(D2)
rot_b.direction = Direction.INPUT
rot_b.pull = Pull.UP

# Used to do HID output for volume knob
cc = ConsumerControl()

# constants to help us track what edge is what
A_POSITION = 0
B_POSITION = 1
UNKNOWN_POSITION = -1  # initial state so we know if something went wrong

rotary_prev_state = [rot_a.value, rot_b.value]

while True:
  
