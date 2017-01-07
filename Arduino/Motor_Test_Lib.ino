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


void loop() 
{
  }
