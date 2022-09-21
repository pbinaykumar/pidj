import RPi.GPIO as GPIO
from time import sleep

lmin1 = 14
lmin2 = 15
lmen = 18
rmin1 = 23
rmin2 = 24
rmen = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(lmin1, GPIO.OUT)
GPIO.setup(lmin2, GPIO.OUT)
GPIO.setup(lmen, GPIO.OUT)
GPIO.setup(rmin1, GPIO.OUT)
GPIO.setup(rmin2, GPIO.OUT)
GPIO.setup(rmen, GPIO.OUT)
GPIO.output(lmin1, GPIO.LOW)
GPIO.output(lmin2, GPIO.LOW)
GPIO.output(rmin1, GPIO.LOW)
GPIO.output(rmin2, GPIO.LOW)
l = GPIO.PWM(lmen, 2000)
l.start(90)
r = GPIO.PWM(rmen, 2000)
r.start(90)


def forwordMotion():
    GPIO.output(lmin1, GPIO.HIGH)
    GPIO.output(lmin2, GPIO.LOW)
    GPIO.output(rmin1, GPIO.HIGH)
    GPIO.output(rmin2, GPIO.LOW)
    return 0


def backwordMotion():
    GPIO.output(lmin1, GPIO.LOW)
    GPIO.output(lmin2, GPIO.HIGH)
    GPIO.output(rmin1, GPIO.LOW)
    GPIO.output(rmin2, GPIO.HIGH)
    return 0

def leftMotion():
    GPIO.output(lmin1, GPIO.LOW)
    GPIO.output(lmin2, GPIO.HIGH)
    GPIO.output(rmin1, GPIO.HIGH)
    GPIO.output(rmin2, GPIO.LOW)
    return 0
def rightMotion():
    GPIO.output(lmin1, GPIO.HIGH)
    GPIO.output(lmin2, GPIO.LOW)
    GPIO.output(rmin1, GPIO.LOW)
    GPIO.output(rmin2, GPIO.HIGH)
    return 0





def stopVehicle():
    GPIO.output(lmin1, GPIO.LOW)
    GPIO.output(lmin2, GPIO.LOW)
    GPIO.output(rmin1, GPIO.LOW)
    GPIO.output(rmin2, GPIO.LOW)
    return 0
