
# Reading an analogue sensor with
# a single GPIO pin

# Author : Matt Hawkins
# Distribution : Raspbian
# Python : 2.7
# UPDATED TO 3
# GPIO   : RPi.GPIO v3.1.0a

import RPi.GPIO as GPIO
import time

# Define function to measure charge time
def RC_time (pin):
    measurement = 0
    # Discharge capacitor
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(pin, GPIO.IN)
    # Count loops until voltage across
    # capacitor reads high on GPIO
    # Unreliable, but perhaps better than enforcing delays
    while (GPIO.input(pin) == GPIO.LOW):
        measurement += 1

    return measurement
