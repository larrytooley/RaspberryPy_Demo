# import GPIO
import RPi.GPIO as GPIO
import time.sleep as sleep

# Delay time
testInt = 500

# First light
firstLightGreen = 4
firstLightYellow = 17
firstLightRed = 22

# Second light
secondLightGreen = 5
secondLightYellow = 13
secondLightRed = 24

# Setup Group
allLights = [firstLightGreen, firstLightYellow, firstLightRed,
             secondLightGreen, secondLightYellow, secondLightRed]

# Color Groups
allRed = [firstLightRed, secondLightRed]
allYellow = [firstLightYellow, secondLightYellow]
allGreen = [firstLightGreen, secondLightGreen]
colors = [allGreen, allYellow, allRed]

GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom

# set up light 1
GPIO.setup(allLights, GPIO.OUT)     # set up all pins


# Test Pattern
while True:
    for color in colors:
        # Cycle colors
        GPIO.output(color, GPIO.HIGH)
        sleep(testInt)
        GPIO.output(color, GPIO.LOW)
        sleep(testInt)
