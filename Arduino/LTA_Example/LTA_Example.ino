/*
 * AerE 160 LTA Example Code
 * Matthew E. Nelson
 */

// Includes
#include <IRremote.h>

// Defines

IRsend irsend;

#define IR_ONE 0x1CE3A857
#define IR_TWO 0x1CE6897
#define IR_THREE 0x1CE3E817
#define IR_FOUR 0x1CE39867
#define IR_FIVE 0x1CE358A7
#define IR_SIX 0x1CE3D827

void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // Send a "1" to fix Window 1
  irsend.sendNEC(IR_ONE,32);
  delay(5000);
  
}
