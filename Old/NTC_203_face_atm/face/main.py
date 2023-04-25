import serial
import random,gsm
import time,face_recognize

import pymsgbox,mail
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(12,GPIO.IN)
port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=3.0)
GPIO.output(20,1)
try:
     while 1:
##          pymsgbox.alert(timeout=10000,text="Please insert Your Card", title='Starting......!')
          
##          if(GPIO.input(12)==0):
##               GPIO.output(21,1)
##               gsm.sms("Theft Detection",8610613386)
##          else:
##               GPIO.output(21,0)
          rcv=port.readline()
          print(rcv)
          if rcv!="":
               pymsgbox.alert(text="Shall I Start Face Recognition", title='Starting......!')
               name=face_recognize.recognition()
               print "Face data: ",name
               if(name=="sujith" and "250089BC8D9D" in rcv):
                         pymsgbox.alert(timeout=10000,text="Thank You " +str(name), title=" Your transaction Started")
                         GPIO.output(20,0)
                         time.sleep(2)
                         GPIO.output(20,1)
               elif(name=="askar" and "26005F818078" in rcv):
                         pymsgbox.alert(timeout=1000,text="Thank You " +str(name), title=" Your transaction Started")
                         GPIO.output(20,0)
                         time.sleep(2)
                         GPIO.output(20,1)
               else:
                         otp=random.randint(1000,9999)
                         print(otp)
                         if ("250089BC8D9D" in rcv):
                              mail.send_mail("pantech.demo19@gmail.com","novitech@2019","nandhinibalan01@gmail.com",message="Your OTP is:"+str(otp))
                              print "OTP was Sent to Sujith"
                         elif ("26005F818078" in rcv):
                              mail.send_mail("kabileshwarang@gmail.com","k9894555925","kabileshwarang@gmail.com",message="Your OTP is:"+str(otp))
                              print "OTP was Sent to Kabileshwaran"
                         Your_otp=pymsgbox.prompt(text="Enter your otp", title="OTP!")
                         if(str(otp)==str(Your_otp)):
                              pymsgbox.alert(timeout=10000,text="Thank You" , title=" Your transaction Started")
                              time.sleep(3)
                              GPIO.output(20,0)
                              time.sleep(3)
                              GPIO.output(20,1)
                         else:
                              GPIO.output(21,1)
                              pymsgbox.alert(timeout=10000,text="Sorry............" , title="Access Denied")
                              time.sleep(3)
                              GPIO.output(21,0)
               rcv=''    
except:
     print "System Close"
     KeyboardInterrupt()
     GPIO.cleanup()
     port.close()
