/*
 * AerE 160 LTA Test appratus
 * Matthew E. Nelson
 */

// Includes
#include <IRremote.h>

int RECV_PIN = 11;

IRrecv irrecv(RECV_PIN);

decode_results results;

// Defines

IRsend irsend;

#define IR_ONE 0x1CE3A857
#define IR_TWO 0x1CE6897
#define IR_THREE 0x1CE3E817
#define IR_FOUR 0x1CE39867
#define IR_FIVE 0x1CE358A7
#define IR_SIX 0x1CE3D827
#define LED_ONE 2
#define LED_TWO 3
#define LED_THREE 4
#define LED_FOUR 5
#define LED_FIVE 6
#define LED_SIX 7


void setup() {
  Serial.begin(9600);
  //Start the receiver
  irrecv.enableIRIn();

}

void loop() {
  // Send a "1" to fix Window 1
  if (irrecv.decode(&results)) {
    Serial.println(results.value, HEX);
    switch (results.value) {
      case IR_ONE:
        Serial.println("A one was sent.");
        digitalWrite(LED_ONE, HIGH);
        delay(1000);
        digitalWrite(LED_ONE, LOW);
        break;
      case IR_TWO:
        Serial.println("A two was sent.");
        digitalWrite(LED_TWO, HIGH);
        delay(1000);
        digitalWrite(LED_TWO, LOW);
        break;
      case IR_THREE:
        Serial.println("A three was sent.");
        digitalWrite(LED_THREE, HIGH);
        delay(1000);
        digitalWrite(LED_THREE, LOW);
        break;
      case IR_FOUR:
        Serial.println("A four was sent.");
        digitalWrite(LED_FOUR, HIGH);
        delay(1000);
        digitalWrite(LED_FOUR, LOW);
        break;
      case IR_FIVE:
        Serial.println("A five was sent.");
        digitalWrite(LED_FIVE, HIGH);
        delay(1000);
        digitalWrite(LED_FIVE, LOW);
        break;
      case IR_SIX:
        Serial.println("A six was sent.");
        digitalWrite(LED_SIX, HIGH);
        delay(1000);
        digitalWrite(LED_SIX, LOW);
        break;
      default:
        Serial.println("The signal sent was not 1-6 or could not be decoded");
      break;
      
    }
  }
  delay(100);
}
