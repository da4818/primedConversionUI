/*This arduino code needs to be running before you start the python code*/
int greenLED = 8;
int redLED = 13;
int blueLED = 12;
int yellowLED = 7;
int val = 0;
/*Val corresponds with the input value in python*/
void setup() {
  Serial.begin(9600);
  Serial.flush();
  pinMode(greenLED, OUTPUT);
  pinMode(redLED, OUTPUT);
  pinMode(blueLED, OUTPUT);
  pinMode(yellowLED, OUTPUT);
}
/* 1 = yellow (UV), 2 = red & blue (PC), 3 = blue (green excitation), 4 = green (red excitation)*/
void loop() {
  if (Serial.available() > 0) {
    int val = char(Serial.read()) - '0';
    /*If 1 is read as the input value, the LED will turn on for 2 seconds */
    if (val == 1) {
      Serial.write("ON\n");
      digitalWrite(yellowLED, HIGH);
      delay(2000); 
      digitalWrite(yellowLED, LOW);
    }
    else if (val == 2){
        Serial.write("ON\n");
        digitalWrite(redLED, HIGH);
        digitalWrite(blueLED, HIGH);
        delay(2000);
        digitalWrite(redLED, LOW);
        digitalWrite(blueLED, LOW);
    }
    else if (val == 3) {
      Serial.write("ON\n");
      digitalWrite(blueLED, HIGH);
      delay(2000);
      digitalWrite(blueLED, LOW);
    }
    else if (val == 4) {
      Serial.write("ON\n");
      digitalWrite(greenLED, HIGH);
      delay(2000);
      digitalWrite(greenLED, LOW);
    }
  }

}
