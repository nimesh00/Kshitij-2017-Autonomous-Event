/**
    DCMotorBot - A simple library to control bots made using 2 simple DC Motors
    MODIFIED FOR NO PWN MOVEMENT FOR THE KTJ EVENT. USE THE DATA RATE SPECIFIED BY THE DELAY FUNCTION TO VARY THE SPEED OF THE MOTORS.
    REPLACE THE PRE EXISTING CPP FILE WITH THIS ONE FOR THE FUNCTIONS TO WORK. TESTED WITH THE L293D.
    */
#include "DCMotorBot.h"
/**
 * Full Constructor
 */
DCMotorBot::DCMotorBot(byte e1, byte e2, byte I1, byte I2, byte I3, byte I4, int delay) {
    setEnablePins(e1, e2);
    setControlPins(I1, I2, I3, I4);
    setDelay(delay);
}

/**
 * Default Constructor
 */
DCMotorBot::DCMotorBot() {
    setEnablePins(1, 2);
    setControlPins(3, 4, 5, 6);
    setDelay(10);
    setSpeed(255);
}

/**
 * Set Enable pins
 */
void DCMotorBot::setEnablePins(byte e1, byte e2) {
    mE1 = e1;
    mE2 = e2;

    pinMode(mE1, OUTPUT);
    pinMode(mE2, OUTPUT);
}

/**
 * Set Control pins
 */
void DCMotorBot::setControlPins(byte I1, byte I2, byte I3, byte I4) {
    mI1 = I1;
    mI2 = I2;
    mI3 = I3;
    mI4 = I4;

    pinMode(mI1, OUTPUT);
    pinMode(mI2, OUTPUT);
    pinMode(mI3, OUTPUT);
    pinMode(mI4, OUTPUT);
}

/**
 * Set delay value
 */
void DCMotorBot::setDelay(int delay) {
    mDelay = delay;
}

/**
 * Set PWM Speed
 */
void DCMotorBot::setSpeed(int speed) {
    mSpeed = speed;
}

/**
 * Start the bot and move forward
 */
void DCMotorBot::start() {
    moveForward();
}

/**
 * Move forward
 */
void DCMotorBot::moveForward() {
    analogWrite(mE1, mSpeed);
    analogWrite(mE2, mSpeed);

    delay(mDelay);

    digitalWrite(mI1, HIGH);
    digitalWrite(mI2, LOW);
    digitalWrite(mI3, HIGH);
    digitalWrite(mI4, LOW);
}

/**
 * Move backward
 */
void DCMotorBot::moveBackward() {
    analogWrite(mE1, mSpeed);
    analogWrite(mE2, mSpeed);

    delay(mDelay);

    digitalWrite(mI1, LOW);
    digitalWrite(mI2, HIGH);
    digitalWrite(mI3, LOW);
    digitalWrite(mI4, HIGH);

}

/**
 * Turn Left
 */
void DCMotorBot::turnLeft() {
    analogWrite(mE1, mSpeed);
    analogWrite(mE2, mSpeed);

    delay(mDelay);

    digitalWrite(mI1, LOW);
    digitalWrite(mI2, HIGH);
    digitalWrite(mI3, HIGH);
    digitalWrite(mI4, LOW);

}

/**
 * Turn Right
 */
void DCMotorBot::turnRight() {
    analogWrite(mE1, mSpeed);
    analogWrite(mE2, mSpeed);

    delay(mDelay);

    digitalWrite(mI1, HIGH);
    digitalWrite(mI2, LOW);
    digitalWrite(mI3, LOW);
    digitalWrite(mI4, HIGH);

}

/**
 * Stop Bot
 */
void DCMotorBot::stop() {
    digitalWrite(mI1, LOW);
    digitalWrite(mI2, LOW);
    digitalWrite(mI3, LOW);
    digitalWrite(mI4, LOW);
}

/**
 * Turn wheel left
 */
void DCMotorBot::steerLeft(){
    digitalWrite(mE2, LOW);

    delay(mDelay);

    digitalWrite(mE1, HIGH);

    digitalWrite(mI1, HIGH);
    digitalWrite(mI2, LOW);

}
 /**
 * Turn wheel right
 */
void DCMotorBot::steerRight(){
    digitalWrite(mE2, LOW);

    delay(mDelay);

    digitalWrite(mE1, HIGH);

    digitalWrite(mI1, LOW);
    digitalWrite(mI2, HIGH);

}
/**
 * move forward width one drive motor
 */
void DCMotorBot::goForward() {
    digitalWrite(mE1, LOW);

    delay(mDelay);

    analogWrite(mE2, mSpeed);

    digitalWrite(mI3, LOW);
    digitalWrite(mI4, HIGH);

}
/**
 * move backward width one drive motor
 */
void DCMotorBot::goBackward() {
    analogWrite(mE1, mSpeed);

    delay(mDelay);

    digitalWrite(mE2, HIGH);

    digitalWrite(mI3, HIGH);
    digitalWrite(mI4, LOW);

}
