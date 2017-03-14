#include "DigiKeyboard.h"

void setup(){
  pinMode(2, INPUT_PULLUP);
}
void loop(){
  DigiKeyboard.sendKeyStroke(0);
  if(digitalRead(2) == 0){
      DigiKeyboard.sendKeyStroke(KEY_S);
      DigiKeyboard.delay(1000);
  }
}
