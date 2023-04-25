import RPi.GPIO as GPIO
import serial,time,os

def sms(msg):
    SERIAL_PORT = "/dev/ttyAMA0"
    ser=serial.Serial(SERIAL_PORT, baudrate=9600, timeout=5)
    ser.write("AT+CMGF=1\r")
    print("Text mode enabled...")
    time.sleep(3)
    #ser.write('AT+CMGS="+918098437664"\r')
    number=8610613386
    ser.write('AT+CMGS="+91'+str(number)+'"\r')
    print ("Sending message...")
    time.sleep(3)
    ser.write(str(989)+chr(26))
    time.sleep(3)
    print ('Message sent.')
def call(number):
    SERIAL_PORT = "/dev/ttyAMA0"
    ser=serial.Serial(SERIAL_PORT, baudrate=9600, timeout=5)
    ser.write("AT\r")
    time.sleep(3)
    message='ATD'+str(number)+';\r'
    print message
    ser.write(message)
    time.sleep(30)
    ser.write("ATH\r")
    time.sleep(3)
    #ser.write("ATDL=1\r")
    #time.sleep(3)

#call(8122220022)

