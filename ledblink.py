import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
print "All Set in Python! Let's Blink"
for i in range(1, 1000):
	GPIO.output(17, GPIO.HIGH)
	sleep(0.1)
	GPIO.output(17, GPIO.LOW)
	sleep(0.1)
GPIO.cleanup()
