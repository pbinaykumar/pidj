from django.shortcuts import render, HttpResponse
from .pigpio import forwordMotion,backwordMotion,leftMotion,rightMotion,stopVehicle

def vehicleMotion(command):
    if command == 'f':
        forwordMotion()
    elif command == 'b':
        backwordMotion()
    elif command == 'l':
        leftMotion()
    elif command == 'r':
        rightMotion()
    else:
        stopVehicle()

    return 0


def forWard(request):
    return HttpResponse('forward')



