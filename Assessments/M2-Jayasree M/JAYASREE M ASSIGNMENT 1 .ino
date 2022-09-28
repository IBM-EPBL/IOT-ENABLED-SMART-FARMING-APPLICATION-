// C++ code
//
#define led 9
#define buzzer 10
#define Idr A1
#define temp A0
void setup()
{
  pinMode(led, OUTPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(temp, INPUT);
  pinMode(Idr, INPUT);
    
  
}

void loop()
{ 
  int
 tempval=analogRead(A0);
  int Idrval=analogRead(A1);
   float v=(tempval/1024.0)*5000;
   float cel=v/10;
   //float farh=(cel*9)/5+32;
  Serial.print(cel);
  Serial.println("Cel");
  if(cel>40){
    digitalWrite(buzzer, HIGH);
 }
  else{
    digitalWrite(buzzer, LOW);
  }
  if(Idrval<300){
    //digitalWrite(led, HIGH);
    led1();
  }
  else{
    digitalWrite(led, LOW);
  }
}
void led1(){
 
  digitalWrite(led, HIGH);
  delay(200); 
  digitalWrite(led,LOW );
  delay(200);
}