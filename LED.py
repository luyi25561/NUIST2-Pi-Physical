import RPi.GPIO as GPIO
import time

#Set GPIO mode to BCM numbering
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18,GPIO.OUT)

print("LED on")
GPIO.output(18,GPIO.HIGH)

GPIO.setup(18,GPIO.OUT)
time.sleep(1)

print("LED off")
GPIO.output(18,GPIO.LOW)

