# import GPIO
import RPi.GPIO as GPIO
import time.sleep as sleep


firstLightGreen = 4
firstLightYellow = 17
firstLightRed = 22
secondLightGreen = 5
secondLightYellow = 13
secondLightRed = 26

pinIn = 18

GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom
GPIO.setwarnings(False)

# set up light 1
GPIO.setup(firstLightGreen, GPIO.OUT)     # set up pin 4 / green
GPIO.setup(firstLightYellow, GPIO.OUT)    # set up pin 17 / yellow
GPIO.setup(firstLightRed, GPIO.OUT)    # set up pin 22 / red

# set up light 2
GPIO.setup(secondLightGreen, GPIO.OUT)     # set up pin 5 / green
GPIO.setup(secondLightYellow, GPIO.OUT)    # set up pin 13 / yellow
GPIO.setup(secondLightRed, GPIO.OUT)    # set up pin 26 / red

# set up input
GPIO.setup(pinIn, GPIO.IN)

try:
    while True:
        if GPIO.input(pinIn):
            sleep(5)

            # first light yellow pattern
            GPIO.output([firstLightRed, secondLightYellow], GPIO.HIGH)
            GPIO.output([firstLightGreen, firstLightYellow,
                         secondLightGreen, secondLightRed], GPIO.LOW)
            sleep(4)

            # first light red pattern
            GPIO.output([firstLightRed, secondLightRed], GPIO.HIGH)
            GPIO.output([firstLightGreen, firstLightYellow,
                         secondLightGreen, secondLightYellow], GPIO.HIGH)
            sleep(2)

            # second light green pattern
            GPIO.output([firstLightRed, secondLightGreen], GPIO.HIGH)
            GPIO.output([firstLightGreen, firstLightYellow,
                         secondLightYellow, secondLightRed], GPIO.LOW)
            sleep(10)

            # second light yellow pattern
            GPIO.output([firstLightRed, secondLightYellow], GPIO.HIGH)
            GPIO.output([firstLightYellow, firstLightGreen,
                         secondLightGreen, secondLightRed], GPIO.LOW)
            sleep(4)

            # second light red pattern
            GPIO.output([firstLightRed, secondLightRed], GPIO.HIGH)
            GPIO.output([firstLightYellow, firstLightGreen,
                         secondLightYellow, secondLightGreen], GPIO.LOW)
            sleep(2)
        else:
            # default pattern
            GPIO.output([firstLightGreen, secondLightRed], GPIO.HIGH)
            GPIO.output([firstLightYellow, firstLightRed,
                         secondLightGreen, secondLightYellow], GPIO.LOW)

except KeyboardInterrupt:
    GPIO.cleanup()
