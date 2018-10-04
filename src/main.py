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
