//MOTOR L - 44,45
//MOTOR R - 46,47

void setup() 

{

//MOTOR L

pinMode(44, OUTPUT);
pinMode(45, OUTPUT);

//MOTOR R

pinMode(46, OUTPUT);
pinMode(47, OUTPUT);

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

{}




