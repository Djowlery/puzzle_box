#include <Stepper.h>

//global variables
const uint8_t IN1 = 8;
const uint8_t IN2 = 9;
const uint8_t IN3 = 10;
const uint8_t IN4 = 11;
const int stepsPerRev = 2048;
const int pullAngle = 90;
const int pullSteps = stepsPerRev/4;
const uint8_t BLUE = 6;
const uint8_t RED = 7;
bool blueActive , redActive;
// instanciate objects
Stepper pullStepper = Stepper(stepsPerRev,IN1,IN3,IN2,IN4);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pullStepper.setSpeed(12);
  pinMode(BLUE,INPUT);
  pinMode(RED,INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  blueActive = digitalRead(BLUE);
  redActive = digitalRead(RED);

  if(blueActive){
    Serial.println("Blue Active");
    Serial.println(pullSteps);
    delay(1000);
    pullStepper.step(pullSteps);
    pullStepper.step(-pullSteps);
  }
  else if(redActive){
    Serial.println("Red Active");
    Serial.println(pullSteps);
    delay(1000);
    pullStepper.step(pullSteps);
    pullStepper.step(-pullSteps);  
  }
  else{
    Serial.println("Undefined");
  }
  delay(200);
}
