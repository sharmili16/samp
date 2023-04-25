int led=4;
int buzzer = 5;
void setup() 
{
  Serial.begin(9600);                             
  pinMode(led, OUTPUT);
  pinMode(buzzer, OUTPUT);
}

void loop()
{
    if (Serial.available()) 
      {
         String data=Serial.readString();
         data.trim();
         Serial.println(data);
            if(data=="a")
              {
                digitalWrite(led, HIGH);
                delay(5000);
                digitalWrite(led, LOW);
                Serial.println("Authorized person");
              }
            if(data=="b")
              {                
                 Serial.println("AT+CMGF=1");
                 delay(1000);  
                 Serial.println("AT+CMGS=\"+919791700883\"\r");
                 delay(1000);
                 Serial.println(" Alert! Unknown Person Entered !");
                 delay(100);
                 Serial.println((char)26);
                 delay(1000); 

                 digitalWrite(buzzer, HIGH);
                 delay(2000);
                 digitalWrite(buzzer, LOW);
              }
              
     }
}
