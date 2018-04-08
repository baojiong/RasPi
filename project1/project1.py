import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
print "Measuring Distance"
print "Press ctrl+c to stop me"

GPIO.setup(23, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(24, GPIO.IN)
time.sleep(0.02)
GPIO.output(23, False)
print "Setting Trigger pin to zero by default"
time.sleep(1)

while True:
	GPIO.output(17, False)

	GPIO.output(23, True)
	time.sleep(0.00001)
	GPIO.output(23, False)

	while GPIO.input(24) == 0:
		start_time = time.time()

	while GPIO.input(24) == 1:
		end_time = time.time()

	total_time = end_time - start_time
	distance = 17510 * total_time

	print "Measured Distance is: %.1f " %distance, "cms"	

	if distance < 100 and distance > 30:
		print "Obatacle Detected"
		os.system('mpg321 buzz.mp3 &')
		GPIO.output(17, True)
		time.sleep(2)
GPIO.cleanup()
