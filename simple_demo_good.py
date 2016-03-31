# import GPIO
import RPi.GPIO as GPIO
from time import sleep

# Delay time
testInt = 0.25

# First light
firstLightGreen = 4
firstLightYellow = 17
firstLightRed = 22

# Second light
secondLightGreen = 5
secondLightYellow = 13
secondLightRed = 26

GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom
GPIO.setwarnings(False)

# set up light 1
GPIO.setup(firstLightGreen, GPIO.OUT)     # set up pin 4 / green
GPIO.setup(firstLightYellow, GPIO.OUT)    # set up pin 17 / yellow
GPIO.setup(firstLightRed, GPIO.OUT)    # set up pin 22 / red

# set up light 2
GPIO.setup(secondLightGreen, GPIO.OUT)     # set up pin 5 / green
GPIO.setup(secondLightYellow, GPIO.OUT)    # set up pin 13 / yellow
GPIO.setup(secondLightRed, GPIO.OUT)    # set up pin 24 / red


# Test Pattern
try:
    while True:
        # Cycle greens
        GPIO.output(firstLightGreen, GPIO.HIGH)
        GPIO.output(secondLightGreen, GPIO.HIGH)
        sleep(testInt)
        GPIO.output(firstLightGreen, GPIO.LOW)
        GPIO.output(secondLightGreen, GPIO.LOW)
        sleep(testInt)

        # Cycle yellows
        GPIO.output(firstLightYellow, GPIO.HIGH)
        GPIO.output(secondLightYellow, GPIO.HIGH)
        sleep(testInt)
        GPIO.output(firstLightYellow, GPIO.LOW)
        GPIO.output(secondLightYellow, GPIO.LOW)
        sleep(testInt)

        # Cycle reds
        GPIO.output(firstLightRed, GPIO.HIGH)
        GPIO.output(secondLightRed, GPIO.HIGH)
        sleep(testInt)
        GPIO.output(firstLightRed, GPIO.LOW)
        GPIO.output(secondLightRed, GPIO.LOW)
        sleep(testInt)
except KeyboardInterrupt:
    # Resets all pins (AKA: turns of the blinky things)
    GPIO.cleanup()
