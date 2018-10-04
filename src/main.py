import time
from digitalio import *
from board import *
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

# Rotary encoder inputs with pullup on D3 & D4
pin_clk = DigitalInOut(D3)
pin_clk.direction = Direction.INPUT
pin_clk.pull = Pull.UP
pin_dt = DigitalInOut(D2)
pin_dt.direction = Direction.INPUT
pin_dt.pull = Pull.UP

# Used to do HID output for volume knob
cc = ConsumerControl()

# constants to help us track what edge is what
A_POSITION = 0
B_POSITION = 1
UNKNOWN_POSITION = -1  # initial state so we know if something went wrong

falling_edge = 0
rising_edge = 0
encoder_counter = 0
encoder_direction = 0

rotary_prev_state = [pin_clk.value, pin_dt.value]

while True:
    # reset encoder and wait for the next turn
    encoder_direction = 0
 
    # take a 'snapshot' of the rotary encoder state at this time
    rotary_curr_state = [pin_clk.value, pin_dt.value]
    if rotary_curr_state != rotary_prev_state:
    #     #print("Changed")
        if rotary_prev_state == [True, True]:
    #         # we caught the first falling edge!
            if not rotary_curr_state[A_POSITION]:
                print("Falling A")
                falling_edge = A_POSITION
            elif not rotary_curr_state[B_POSITION]:
                print("Falling B")
                falling_edge = B_POSITION
            else:
                # uhh something went deeply wrong, lets start over
                continue
 
        if rotary_curr_state == [True, True]:
    #         # Ok we hit the final rising edge
            if not rotary_prev_state[B_POSITION]:
                rising_edge = B_POSITION
                # print("Rising B")
            elif not rotary_prev_state[A_POSITION]:
                rising_edge = A_POSITION
                # print("Rising A")
            else:
                # uhh something went deeply wrong, lets start over
                continue
 
            # check first and last edge
            if (rising_edge == A_POSITION) and (falling_edge == B_POSITION):
                encoder_counter -= 1
                encoder_direction = -1
                print("%d dec" % encoder_counter)
            elif (rising_edge == B_POSITION) and (falling_edge == A_POSITION):
                encoder_counter += 1
                encoder_direction = 1
                print("%d inc" % encoder_counter)
            else:
                # (shrug) something didn't work out, oh well!
                encoder_direction = 0
 
            # reset our edge tracking
            rising_edge = falling_edge = UNKNOWN_POSITION
 
    rotary_prev_state = rotary_curr_state
    rotary_prev_state = rotary_curr_state
    # Check if rotary encoder went up
    if encoder_direction == 1:
        cc.send(ConsumerControlCode.VOLUME_INCREMENT)
    if encoder_direction == -1:
        cc.send(ConsumerControlCode.VOLUME_DECREMENT)
