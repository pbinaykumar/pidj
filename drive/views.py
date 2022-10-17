from django.shortcuts import render, HttpResponse
from .pigpio import forwordMotion,backwordMotion,leftMotion,rightMotion,stopVehicle

def vehicleMotion(command):
    print(command,'commmmmm')
    if command == 'f':
        data = forwordMotion()
    elif command == 'b':
        data = backwordMotion()
    elif command == 'l':
        data = leftMotion()
    elif command == 'r':
        data = rightMotion()
    else:
        data = backwordMotion()

    return data


def forWard(request):
    return HttpResponse('forward')



