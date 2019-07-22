#import the required modules
import RPi.GPIO as GPIO
import time

# set the pins numbering mode
# But don't because that's done elsewhere
#GPIO.setmode(GPIO.BOARD)

control_pins = [11, 15, 16, 13]

# Select the GPIO pins used for the encoder K0-K3 data inputs	
for pin in control_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)	

# Select the signal used to select ASK/FSK
GPIO.setup(18, GPIO.OUT) 
# Set the modulator to ASK for On Off Keying 
GPIO.output(18, False)

# Select the signal used to enable/disable the monitor	
GPIO.setup(22, GPIO.OUT)
# Disable the modulator by setting CE pin lo
GPIO.output (22, False)

setup = {
            "ALL": [1,1,0],
            "1":   [1,1,1],
            "2":   [0,1,1],
            "3":   [1,0,1],
            "4":   [0,0,1],
        }


def reset():
    set_off("ALL")
    for pin in control_pins:
        GPIO.output(pin, False)

def set_on(plug):
    for pin in range(0, 2):
        GPIO.output(control_pins[pin], setup[plug.upper()][pin])
    GPIO.output(13, 1)
    time.sleep(0.1)
    GPIO.output(22, True)
    time.sleep(0.25)
    GPIO.output(22, False)

def set_off(plug):
    for pin in range(0, 2):
        GPIO.output(control_pins[pin], setup[plug.upper()][pin])
    GPIO.output(13, 0)
    time.sleep(0.1)
    GPIO.output(22, True)
    time.sleep(0.25)
    GPIO.output(22, False)
