from digitalio import *
from board import *
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

# Encoder button is a digital input with pullup on D2
button = DigitalInOut(D0)
button.direction = Direction.INPUT
button.pull = Pull.UP

last_button = button.value
cc = ConsumerControl()
while True:
     # Button was 'just pressed'
    if (not button.value) and last_button:
        print("Button pressed!")
        cc.send(ConsumerControlCode.VOLUME_INCREMENT)
    elif button.value and (not last_button):
        print("Button Released!")
    last_button = button.value
