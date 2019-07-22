import time
import datetime
import RPi.GPIO as GPIO
import controller
import analogue_in
from datetime import datetime


# Configure GPIO to use labels on header
GPIO.setmode(GPIO.BOARD)
# Disable warnings from multiple GPIO users
GPIO.setwarnings(False)
# Channels for external sensors
MOIST_CHAN = 1
TEMP_CHAN = 1
LIGHT_CHAN = 1
# No need to set up pins - this is handled by analogue_in as there is much
# switching of modes
# Thresholds for outputs
PUMP_THRES = 2
LIGHT_THRES = 2
# Plug numbers for outputs
PUMP_NO = "1"
LIGHT_NO = "2"


# Doesn't use a database because I'm too lazy to set one up
pump_data = []
moist_data = []
times = []

def backend_main():
    while True:
        try:
            t0 = time.time()
            # Get readings from hardware
            moist = analogue_in.RC_time(MOIST_CHAN)
            temp = analogue_in.RC_time(TEMP_CHAN)
            light = analogue_in.RC_time(LIGHT_CHAN)  
            print("M", moist, "T", temp, "L", light)
            moist_data.append(moist)
            t = datetime.now()
            ts = str(t.year) + "-" + str(t.month) + "-" + str(t.day) + " " + str(t.hour) + ":" + str(t.minute) 
            times.append(ts)

            # Determine whether or not to activate pump and light
            # Moisture sensors tend to acquire LESSER resistance with lost
            # moisture, so capacitor charge time will DECREASE
            # NOTE: Not necessarily correct. Verify with physical sensor to be sure
            print(PUMP_THRES)
            if moist < PUMP_THRES:
                print("ON")
                p_on = True
                controller.set_on(PUMP_NO)
                pump_data.append(1)
            else:
                print("OFF")
                p_on = False
                controller.set_off(PUMP_NO)
                pump_data.append(0)

            # Sleep for the remainder of 30 seconds
            # NOTE: Should be 30
            time.sleep(3 - time.time() + t0)

        except BaseException:
            # Exit gracefully if interrupted
            print("Graceful exit commencing")
            controller.reset()
            GPIO.cleanup()
            break

