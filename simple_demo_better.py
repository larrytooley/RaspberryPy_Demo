# import GPIO
import RPi.GPIO as GPIO
from time import sleep

# Delay time
testInt = 0.5

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

GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom

# set up light 1
GPIO.setup(allLights, GPIO.OUT)     # set up all pins


# Test Pattern
while True:
    # Cycle greens
    GPIO.output(allGreen, GPIO.HIGH)
    sleep(testInt)
    GPIO.output(allGreen, GPIO.LOW)
    sleep(testInt)

    # Cycle yellows
    GPIO.output(allYellow, GPIO.HIGH)
    sleep(testInt)
    GPIO.output(allYellow, GPIO.LOW)
    sleep(testInt)

    # Cycle reds
    GPIO.output(allRed, GPIO.HIGH)
    sleep(testInt)
    GPIO.output(allRed, GPIO.LOW)
    sleep(testInt)
