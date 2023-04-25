import serial
import time
port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=3.0)
i=1
while 1:
        i=0
        rcv = port.readline()
        print(rcv)
        
               
	
                
                
	

