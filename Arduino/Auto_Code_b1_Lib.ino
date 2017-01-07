#include <DCMotorBot.h> //Library That Drives the Bot. Modify the library if necessary as it uses PWM.
int inByte; //Serial Data from Python
DCMotorBot bot;

//MOTOR L - 44,45
//MOTOR R - 46,47

void setup() 

{     
    bot.setControlPins(44, 45, 46, 47); //L-->R in Sequence.
    Serial.begin(9600);
    pinMode(13, OUTPUT); //Resource LED.
    
    //Run a quick test of the bot's motors.
        
    bot.moveForward();
    delay(800);
    bot.turnLeft();
    delay(800);
    bot.turnRight();
    delay(800);
    bot.moveBackward();
    delay(800);
    bot.stop();
        
}


void loop() {
 
if(Serial.available() > 0) { // A byte is ready to receive
inByte = Serial.read();

if(inByte == 'f')
{
  bot.moveForward();
  delay(5);
  bot.stop();
   }

  else if (inByte == 'r')
  {
  bot.turnRight();
  delay(5);
  bot.stop();
}

else if (inByte == 'l')
  {
  digitalWrite(13, HIGH);
  delay(1000);
  digitalWrite(13,LOW);
}

else if (inByte == 'b')
  {
  bot.moveBackward();
  delay(5);
  bot.stop();
}
}
}
