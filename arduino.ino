
//This is what I wrote on the arduino software
//It is used to turn on the Arduino LED When you press 1
//And turn it off when you press 0

int datafromUser=0;


void setup() {
  // put your setup code here, to run once:
  pinMode (LED_BUILTIN, OUTPUT),
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
if(Serial.available() > 0)
{
  datafromUser=Serial.read();
}


if(datafromUser == '1')
{
  digitalWrite(LED_BUILTIN , HIGH);
  }

else if (datafromUser == 'O')
{
  digitalWrite(LED_BUILTIN, LOW);
  }

}