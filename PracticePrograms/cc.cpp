//ardunio code to make common cathode led blink
//#include <Arduino.h>
//#include <avr/io.h>

//declaring rgb led pins
int redPin = 9;
int greenPin = 10;
int bluePin = 11;

//brightness of each color
int redBrightness = 0;
int greenBrightness = 0;
int blueBrightness = 0;

void setup() {
  //setting pins as output
  Serial.begin(9600);

  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
}

void loop() {
  //setting brightness of each color
  analogWrite(redPin, redBrightness);
  analogWrite(greenPin, greenBrightness);
  analogWrite(bluePin, blueBrightness);
  //delay
  delay(100);
  //increasing brightness of each color
  redBrightness = redBrightness + 10;
  greenBrightness = greenBrightness + 10;
  blueBrightness = blueBrightness + 10;
  //if brightness is greater than 255, set it to 255
  if (redBrightness > 255) {
    redBrightness = 255;
  }
  if (greenBrightness > 255) {
    greenBrightness = 255;
  }
  if (blueBrightness > 255) {
    blueBrightness = 255;
  }
}