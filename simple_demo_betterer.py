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

# Setup Group
allLights = [firstLightGreen, firstLightYellow, firstLightRed,
             secondLightGreen, secondLightYellow, secondLightRed]

# Color Groups
allRed = [firstLightRed, secondLightRed]
allYellow = [firstLightYellow, secondLightYellow]
allGreen = [firstLightGreen, secondLightGreen]
colors = [allGreen, allYellow, allRed]

GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom
GPIO.setwarnings(False)

# set up light 1
GPIO.setup(allLights, GPIO.OUT)     # set up all pins


# Test Pattern
try:
    while True:
        for color in colors:
            # Cycle colors
            GPIO.output(color, GPIO.HIGH)
            sleep(testInt)
            GPIO.output(color, GPIO.LOW)
            sleep(testInt)
except KeyboardInterrupt:
    GPIO.cleanup()
