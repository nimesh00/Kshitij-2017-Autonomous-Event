//MOTOR L - mot_pin1,mot_pin2
//MOTOR R - mot_pin3,mot_pin4
int inByte; // Stores incoming command
int mot_pin1 = 3;
int mot_pin2 = 4;
int mot_pin3 = 5;
int mot_pin4 = 6;
int led_pin = 53;
float spd = 80; 
void setup() {
Serial.begin(9600);

//MOTOR L

pinMode(mot_pin1, OUTPUT);
pinMode(mot_pin2, OUTPUT);

//MOTOR R

pinMode(mot_pin3, OUTPUT);
pinMode(mot_pin4, OUTPUT);
pinMode(led_pin, OUTPUT);
analogWrite(mot_pin1, spd);
analogWrite(mot_pin2, 0);
analogWrite(mot_pin3, spd);
analogWrite(mot_pin4, 0);
delay(250);
analogWrite(mot_pin1, 0);
analogWrite(mot_pin2, 0);
analogWrite(mot_pin3, 0);
analogWrite(mot_pin4, 0);
delay(300);
analogWrite(mot_pin1, spd);
analogWrite(mot_pin2, 0);
analogWrite(mot_pin3, 0);
analogWrite(mot_pin4, spd);
delay(250);
analogWrite(mot_pin1, 0);
analogWrite(mot_pin2, 0);
analogWrite(mot_pin3, 0);
analogWrite(mot_pin4, 0);
delay(300);
analogWrite(mot_pin1, 0);
analogWrite(mot_pin2, spd);
analogWrite(mot_pin3, spd);
analogWrite(mot_pin4, 0);
delay(250);
analogWrite(mot_pin1, 0);
analogWrite(mot_pin2, 0);
analogWrite(mot_pin3, 0);
analogWrite(mot_pin4, 0);
delay(300);
analogWrite(mot_pin1, 0);
analogWrite(mot_pin2, spd);
analogWrite(mot_pin3, 0);
analogWrite(mot_pin4, spd);
delay(250);
analogWrite(mot_pin1, 0);
analogWrite(mot_pin2, 0);
analogWrite(mot_pin3, 0);
analogWrite(mot_pin4, 0);
delay(300);
analogWrite(mot_pin1, 0);
analogWrite(mot_pin2, 0);
analogWrite(mot_pin3, 0);
analogWrite(mot_pin4, 0);
delay(250);
analogWrite(mot_pin1, 0);
analogWrite(mot_pin2, 0);
analogWrite(mot_pin3, 0);
analogWrite(mot_pin4, 0);

analogWrite(led_pin, 255);
delay(300);
analogWrite(led_pin, 0);

Serial.println("Ready"); // Ready to receive commands
}

void loop() 

{
if(Serial.available() > 0) { // A byte is ready to receive
inByte = Serial.read();
if(inByte == 'f')
{ //declare a as the serial out in python
analogWrite(mot_pin1, spd);
analogWrite(mot_pin2, 0);
analogWrite(mot_pin3, spd);
analogWrite(mot_pin4, 0);

}
else if(inByte =='b') 
{
analogWrite(mot_pin1, 0);
analogWrite(mot_pin2, spd);
analogWrite(mot_pin3, 0);
analogWrite(mot_pin4, spd);

}
else if(inByte =='o') 
{
analogWrite(led_pin, 255);
delay(300);
analogWrite(led_pin, 0);

}
else if(inByte =='r') 
{
analogWrite(mot_pin1, spd);
analogWrite(mot_pin2, 0);
analogWrite(mot_pin3, 0);
analogWrite(mot_pin4, spd);

}
else if(inByte =='l') 
{
analogWrite(mot_pin1, 0);
analogWrite(mot_pin2, spd);
analogWrite(mot_pin3, spd);
analogWrite(mot_pin4, 0);

}
else if(inByte =='s') 
{
analogWrite(mot_pin1, 0);
analogWrite(mot_pin2, 0);
analogWrite(mot_pin3, 0);
analogWrite(mot_pin4, 0);

}
else
{analogWrite(mot_pin1, 0);
analogWrite(mot_pin2, 0);
analogWrite(mot_pin3, 0);
analogWrite(mot_pin4, 0);
}
  
} 
delay(30);
/*analogWrite(mot_pin1, 0);
analogWrite(mot_pin2, 0);
analogWrite(mot_pin3, 0);
analogWrite(mot_pin4, 0);*/
}
