/**************************************************************************/
/*!
    @file     DMXInputTest.ino
    @author   Claude Heintz
    @license  BSD (see LXTeensy4DMX LICENSE)
    @copyright 2017-2020 by Claude Heintz

    Control brightness of LED on PWM_PIN with DMX address 1
    @section  HISTORY

    v1.00 - Modified for LXTeensy4DMX_Library
*/
/**************************************************************************/
#include <LXTeensy4DMX.h>

/* On a MAX485, the transmit enable and inverted receive enable
 * pins are tied together and connected to the direction pin.
 * For input, these pins on the MAX485 need to be held LOW.
 */
#define DIRECTION_PIN 3

#define PWM_PIN 6
int got_dmx = 0;

void setup() {
  pinMode(DIRECTION_PIN, OUTPUT);
  pinMode(PWM_PIN, OUTPUT);
  
  Teensy4DMX.setDirectionPin(DIRECTION_PIN);
  Teensy4DMX.setDataReceivedCallback(&gotDMXCallback);
  
  Teensy4DMX.startInput();
  Serial.begin(115200);
}


// ***************** input callback function *************

void gotDMXCallback(int slots) {
  got_dmx = slots;
}

/************************************************************************

  The main loop checks to see if dmx input is available (got_dmx>0)
  And then reads the level of dimmer 1 to set PWM level of LED
  
*************************************************************************/

void loop() {
  if ( got_dmx ) {
    analogWrite(PWM_PIN,Teensy4DMX.getSlot(1));
    Serial.println("---");
    Serial.println(Teensy4DMX.getSlot(1));
    Serial.println(Teensy4DMX.getSlot(2));
    Serial.println(Teensy4DMX.getSlot(3));
    Serial.println(Teensy4DMX.getSlot(4));
    Serial.println(got_dmx);
    got_dmx=0;
    Serial.println("___");
  }
}
