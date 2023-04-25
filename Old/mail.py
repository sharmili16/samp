#import RPi.GPIO as GPIO
import smtplib
import time
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart



def send_mail(gmail_user ,gmail_pwd,TO,message="python test",path="img.jpg"):
        FROM= gmail_user
        time.sleep(1)
        msg = MIMEMultipart()
        time.sleep(1)
        msg['Subject'] =message
        time.sleep(1)
        fp = open(path, 'rb')
        time.sleep(1)
        img = MIMEImage(fp.read())
        time.sleep(1)
        fp.close()
        time.sleep(1)
        msg.attach(img)
        time.sleep(1)
        i=1
        while i:
                
                server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
                print("smtp.gmail")
                server.ehlo()
                print("ehlo")
                server.starttls()
                print ("starttls")
                server.login(gmail_user,gmail_pwd)
                print("reading mail & password")
                server.sendmail(FROM, TO, msg.as_string())
                print("from")
                server.close()
                i=0
                print ('successfully sent the mail')
##        except:
##                print("failed to send mail")


##if __name__=="__main__":
##        send_mail("raghurraghu33@gmail.com","9789175342","raghurraghu33@gmail.com",message="Your OTP :")
        
