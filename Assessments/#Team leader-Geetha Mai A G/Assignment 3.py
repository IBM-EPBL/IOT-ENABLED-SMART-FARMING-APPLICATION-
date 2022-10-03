import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

red=7
yellow=11
green=13

GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

while True:
        GPIO.output(red, True)
        print("RED is ON")
        time.sleep(3)
        GPIO.output(red,False)

        GPIO.output(yellow, True)
        print("YELLOW is ON")
        time.sleep(3)
        GPIO.output(yellow,False)

        GPIO.output(green, True)
        print("GREEN is ON")
        time.sleep(3)
        GPIO.output(green,False)

GPIO.cleanup()
