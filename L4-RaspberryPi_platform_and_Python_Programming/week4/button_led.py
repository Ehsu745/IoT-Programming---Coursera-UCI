import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(11, GPIO.IN)

while True:
    value = GPIO.input(11)
    if (value == 0):
        GPIO.output(13, True)
        time.sleep(0.5)
        GPIO.output(13, False)
        time.sleep(0.5)
    else:
        GPIO.output(13, True)
