# CircuitPythonVolumeKnob
Volume Knob using a Trinket M0, a KY-040 and CircuitPython

# Requirements
Install the latest CircuitPython and its necessary adafruit_hid library onto your device

The needed minimal CircuitPython 3.1.1:

Circuit Python library: use latest revision:
* working : adafruit-circuitpython-bundle-3.x-mpy-20190106.zip

https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/latest
https://github.com/adafruit/circuitpython/releases/latest

# Install new CircuitPython

Just double click the button on the trinket m0. Remove the old .UF2 file and copy the new .UF2 file other. 
It will automatically restart with the new firmware.

# Setup Hardware

Connect the Pins in the following way

| KY-040 | Trinket M0 |
|--------|------------|
| CLK    | 2          |
| DT     | 3          |
| SW     | 0          |
| +      | 3V         |
| GND    | Gnd        |

# Setup Source Code

Only copy the needed libraries onto your device, else it won't fit onto your trinket.

Copy the contents of the src folder onto the trinket m0s memory.

