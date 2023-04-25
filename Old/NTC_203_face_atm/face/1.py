import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setup(12,gpio.IN)
while 1:
    if(gpio.input(12)==1):
        print("hi")
    else:
        print("hello")
            
