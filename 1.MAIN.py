#-----------MODULES IMPORT--------------------------------------
from tkinter import *
from tkinter import ttk
import pymsgbox
import pyttsx3
##eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
import time
import datetime
import face_recognize
import serial
engine = pyttsx3.init()
arduino = serial.Serial('COM5', 9600, timeout=3)

#---------------MAIN LOOP--------------------------
  
while 1:
        biker= face_recognize.recognition()
        print(biker)
        if biker != "":
                    if ((biker =='Shar')):
                        pymsgbox.alert(timeout=1000,text="Thank You", title="Sucess!!")
                        arduino.write(str.encode('a'))
                        print ("Authorized Person")
                        engine.say("Sharmili Daughter")
                        engine.runAndWait()
                        time.sleep(2)
                                        
                    elif ((biker =='Sibi')):
                        pymsgbox.alert(timeout=1000,text="Thank You", title="Sucess!!")
                        arduino.write(str.encode('a'))
                        print ("Authorized Person")
                        engine.say("Sibi Friend")
                        engine.runAndWait()
                        time.sleep(2)
                    else:
                        print ("Un Authorized Person")
                        arduino.write(str.encode('b'))
##                        arduino.write(str.encode('c'))
                        engine.say("Un Authorized Person")
                        engine.runAndWait()
                        time.sleep(2)
                    
