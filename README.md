# CircuitPythonVolumeKnob
Volume Knob using a Trinket M0, a KY-040 and CircuitPython

# Requirements
Install the latest CircuitPython and its necessary adafruit_hid library onto your device

Minimal CircuitPython and library revision: 3.0

https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/latest
https://github.com/adafruit/circuitpython/releases/latest

# Install new CircuitPython

Just double click the button on the trinket m0. Remove the old .UF2 file and copy the new .UF2 file other. 
It will automatically restart with the new firmware.

# Setup Hardware

Connect the Pins in the following way

| KY-040 | Trinket M0 |
|--------|------------|
| CLK    | 3          |
| DT     | 2          |
| SW     | 0          |
| +      | 3V         |
| GND    | Gnd        |

# Setup Source Code

Only copy the needed libraries onto your device, else it won't fit.

Copy the contents of the src folder onto the trinket m0s memory.

