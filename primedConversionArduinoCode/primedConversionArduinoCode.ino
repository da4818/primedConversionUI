/*This arduino code needs to be running before you start the python code*/
int greenLED = 4;
int redLED = 12;
int val = 0;
/*Val corresponds with the input value in python*/
void setup() {
  Serial.begin(9600);
  Serial.flush();
  pinMode(greenLED, OUTPUT);
  pinMode(redLED, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    int val = char(Serial.read()) - '0';
    /*If 1 is read as the input value, the LED will turn on for 2 seconds */
    if (val == 1) {
      Serial.write("ON\n");
      digitalWrite(greenLED, HIGH);
      delay(2000); 
      digitalWrite(greenLED, LOW);
    }
    
    if (val == 3) {
      Serial.write("ON\n");
      digitalWrite(redLED, HIGH);
      delay(20r00); 
      digitalWrite(redLED, LOW);
    }


  }
}
