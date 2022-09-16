int moisture_data=0;
void setup()
{
  pinMode(A0,INPUT);
  Serial.begin(9600);
  pinMode(13,OUTPUT);
  pinMode(7,OUTPUT);
}

void loop()
{
  moisture_data=analogRead(A0);
  Serial.println(moisture_data);
  if(moisture_data<22){
   digitalWrite(13, HIGH);
   digitalWrite(7, HIGH);
  }
  else{
    digitalWrite(13, LOW);
    digitalWrite(7, HIGH);
  }
  delay(5);
}