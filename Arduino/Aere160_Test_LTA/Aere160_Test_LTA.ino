/*
 * AerE 160 LTA Test Code
 * For this code, each "window" has a number code 1 through 6
 * This code rotates between each code to test the Raspberry PI 
 * receiving the code.  This code is also used as a starting point
 * for the students to use in their design.
 * 
 * Hardware Setup
 * IR LED positive pin (long one) Must be on pin D3
 * Short leg should be connected to GND
 */

//Includes
#include <IRremote.h>

//Uncomment the following line to disable serial debug statements
//#define SERIAL_DEBUG false
#include <SerialDebug.h>

// Define Items

IRsend irsend;

#define IR_ONE 0x1CE3A857
#define IR_TWO 0x1CE6897
#define IR_THREE 0x1CE3E817
#define IR_FOUR 0x1CE39867
#define IR_FIVE 0x1CE358A7
#define IR_SIX 0x1CE3D827
#define IR_SEVEN 0x1CE3B847
#define IR_EIGHT 0x1CE37887
#define IR_NINE 0x1CE3F807
#define IR_ZERO 0x1CE3827D
#define IR_PWR 0x1CE3807F
#define IR_UP 0x1CE3D02F
#define IR_DOWN 0x1CE3F00F
#define IR_LEFT 0x1CE352AD
#define IR_RIGHT 0x1CE3926D


void setup() {
  //
  SERIAL_DEBUG_SETUP(9600); 
  DEBUG("Starting up Arduino...Free RAM: %u", FREE_RAM);
}
void loop() {
  //Cycle through each number 1 through 6, remote us a NEC remote
  DEBUG("Sending a 1");
  irsend.sendNEC(IR_ONE,32);
  delay(2000);
  DEBUG("Sending a 2");
  irsend.sendNEC(IR_TWO,32);
  delay(2000);
  DEBUG("Sending a 3");
  irsend.sendNEC(IR_THREE,32);
  delay(2000);
  DEBUG("Sending a 4");
  irsend.sendNEC(IR_FOUR,32);
  delay(2000);
  DEBUG("Sending a 5");
  irsend.sendNEC(IR_FIVE,32);
  delay(2000);
  DEBUG("Sending a 6");
  irsend.sendNEC(IR_SIX,32);
  delay(2000);
}
