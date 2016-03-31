# import GPIO
import RPi.GPIO as GPIO
import time.sleep as sleep


testInt = 500

# First light
firstLightGreen = 4
firstLightYellow = 17
firstLightRed = 22

# Second light
secondLightGreen = 5
secondLightYellow = 13
secondLightRed = 24

GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom

# set up light 1
GPIO.setup(firstLightGreen, GPIO.OUT)     # set up pin 4 / green
GPIO.setup(firstLightYellow, GPIO.OUT)    # set up pin 17 / yellow
GPIO.setup(firstLightRed, GPIO.OUT)    # set up pin 22 / red

# set up light 2
GPIO.setup(secondLightGreen, GPIO.OUT)     # set up pin 5 / green
GPIO.setup(secondLightYellow, GPIO.OUT)    # set up pin 13 / yellow
GPIO.setup(secondLightRed, GPIO.OUT)    # set up pin 24 / red


# Test Pattern
while True:
    GPIO.output(firstLightGreen, 1)
    GPIO.output(secondLightGreen, 1)
    sleep(testInt)
    GPIO.output(firstLightGreen, 0)
    GPIO.output(secondLightGreen, 0)
    sleep(testInt)

    GPIO.output(firstLightYellow, 1)
    GPIO.output(secondLightYellow, 1)
    sleep(testInt)
    GPIO.output(firstLightYellow, 0)
    GPIO.output(secondLightYellow, 0)
    sleep(testInt)

    GPIO.output(firstLightRed, 1)
    GPIO.output(secondLightRed, 1)
    sleep(testInt)
    GPIO.output(firstLightRed, 0)
    GPIO.output(secondLightRed, 0)
    sleep(testInt)
