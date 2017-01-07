//Code that does not use the DCMotorBot Library

//MOTOR L - 44,45
//MOTOR R - 46,47

int inByte;

void setup() {

pinMode(13, OUTPUT);
pinMode(44, OUTPUT);
pinMode(45, OUTPUT);
pinMode(46, OUTPUT);
pinMode(47, OUTPUT);

  // Run a quick test of the motors.
  //Forward, Left, Right Reverse

//FORWARD

digitalWrite(44, HIGH);
digitalWrite(45, LOW);
digitalWrite(46, HIGH);
digitalWrite(47, LOW);
delay(800);

//LEFT (Non-Zero)

digitalWrite(44, LOW);
digitalWrite(45, LOW);
digitalWrite(46, HIGH);
digitalWrite(47, LOW);
delay(800);
digitalWrite(44, LOW);
digitalWrite(45, LOW);
digitalWrite(46, LOW);
digitalWrite(47, HIGH);
delay(800);

//RIGHT (Non-Zero)

digitalWrite(44, HIGH);
digitalWrite(45, LOW);
digitalWrite(46, LOW);
digitalWrite(47, LOW);
delay(800);
digitalWrite(44, LOW);
digitalWrite(45, HIGH);
digitalWrite(46, LOW);
digitalWrite(47, LOW);
delay(800);

//REVRSE

digitalWrite(44, LOW);
digitalWrite(45, HIGH);
digitalWrite(46, LOW);
digitalWrite(47, HIGH);
delay(800);


//STOP

digitalWrite(44, LOW);
digitalWrite(45, LOW);
digitalWrite(46, LOW);
digitalWrite(47, LOW);


}

void loop() 
{
//Act upon pyserial commands.

if(Serial.available() > 0) { // A byte is ready to receive
inByte = Serial.read();

if(inByte == 'f')

{

digitalWrite(44, HIGH);
digitalWrite(45, LOW);
digitalWrite(46, HIGH);
digitalWrite(47, LOW);
delay(10);

}

else if (inByte == 'r')

  {

  digitalWrite(44, LOW);
  digitalWrite(45, LOW);
  digitalWrite(46, HIGH);
  digitalWrite(47, LOW);
  delay(5);

  } 



else if (inByte == 'l')

  {

  digitalWrite(13, HIGH);
  delay(1000);
  digitalWrite(13,LOW);

}



else if (inByte == 'b')

{

digitalWrite(44, LOW);
digitalWrite(45, HIGH);
digitalWrite(46, LOW);
digitalWrite(47, HIGH);
delay(5);
 
}
}
}
