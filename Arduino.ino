//This is what should be on the arduino software
//See motor_rp.py to read more about the issues faced.


#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards


    // variable to store the servo position



void setup() {

 myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  int i=0;
   for (i = 0; i <= 180; i += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(i);              // tell servo to go to position in variable 'pos'

   }
}

void loop() {



}