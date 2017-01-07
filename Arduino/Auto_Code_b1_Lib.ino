//Libraries
#include <DCMotorBot.h> //Library That Drives the Bot. Modify the library if necessary as it uses PWM.
//Hogaya Kaam

//MOTOR L - 44,45
//MOTOR R - 46,47
int inByte;

DCMotorBot bot;

void setup() 
{     
    bot.setControlPins(44, 45, 46, 47); //L-->R in Sequence.
    Serial.begin(9600);
    pinMode(13, OUTPUT);
        }


void loop() {
 
if(Serial.available() > 0) { // A byte is ready to receive
inByte = Serial.read();

//Acts upon Pyserial Commands.
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
