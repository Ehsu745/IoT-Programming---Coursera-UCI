import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
GPIO.setwarnings(False)
pwm = GPIO.PWM(13, 50)
pwm.start(0)

while True:
    for i in xrange(1, 101, 2):
        pwm.ChangeDutyCycle(i)
        time.sleep(0.03)
    for i in xrange(100 , 1, -2):
        pwm.ChangeDutyCycle(i)
        time.sleep(0.03)
    
