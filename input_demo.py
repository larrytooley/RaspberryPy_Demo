# import GPIO
import RPi.GPIO as GPIO
from time import sleep


# light
secondLightRed = 26

# Input
pinIn = 18

GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom
GPIO.setwarnings(False)

# Set up light
GPIO.setup(secondLightRed, GPIO.OUT)    # set up pin 26 / red

# Set up input
GPIO.setup(pinIn, GPIO.IN)


# Test Pattern
try:
    while True:
        # Check to see if button is pushed
        if GPIO.input(pinIn):
            print "The switch is on."
            GPIO.output(secondLightRed, GPIO.HIGH)
        else:
            print "The switch is off."
            GPIO.output(secondLightRed, GPIO.LOW)
        sleep(0.1)

except KeyboardInterrupt:
    # Resets all pins (AKA: turns off the blinky things)
    GPIO.cleanup()
