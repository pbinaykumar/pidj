import RPi.GPIO as GPIO
from time import sleep

lmin1 = 24
lmin2 = 23
lmen = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(lmin1, GPIO.OUT)
GPIO.setup(lmin2, GPIO.OUT)
GPIO.setup(lmen, GPIO.OUT)
GPIO.output(lmin1, GPIO.LOW)
GPIO.output(lmin2, GPIO.LOW)
p = GPIO.PWM(lmen, 2000)
p.start(90)


def forwordMotion():
    GPIO.output(lmin1, GPIO.HIGH)
    GPIO.output(lmin2, GPIO.LOW)
    return 0


def backwordMotion():
    GPIO.output(lmin1, GPIO.LOW)
    GPIO.output(lmin2, GPIO.HIGH)
    return 0


def leftMotion():
    return 0


def rightMotion():
    return 0


def stopVehicle():
    return 0
