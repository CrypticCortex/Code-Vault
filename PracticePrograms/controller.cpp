//making a controller control rgb, laser and buzzer using breadboard
//

//if the controller moves left buzzer gets on
//if the controller moves right laser gets on
//if the controller moves up led gets on

//defining the pins
#define LASER_PIN 2
#define BUZZER_PIN 3
#define RGB_PIN 8

//defining the variables
int laser_state = 0;
int buzzer_state = 0;
int rgb_state = 0;

//defining the functions
//if the controller moves left buzzer gets on
void laser_on() {
  digitalWrite(LASER_PIN, HIGH);
  laser_state = 1;
}
//if the controller moves right laser gets off
void laser_off() {
  digitalWrite(LASER_PIN, LOW);
  laser_state = 0;
}
//if the controller moves up led gets on
void rgb_on() {
  digitalWrite(RGB_PIN, HIGH);
  rgb_state = 1;
}
//if the controller moves down led gets off
void rgb_off() {
  digitalWrite(RGB_PIN, LOW);
  rgb_state = 0;
}
//if the controller moves left buzzer gets on
void buzzer_on() {
  tone(BUZZER_PIN, 1000, 1000);
  buzzer_state = 1;
}
//if the controller moves right laser gets off
void buzzer_off() {
  noTone(BUZZER_PIN);
  buzzer_state = 0;
}
void setup(){
    pinMode(LASER_PIN, OUTPUT);
    pinMode(BUZZER_PIN, OUTPUT);
    pinMode(RGB_PIN, OUTPUT);
}
void loop(){
    if(analogRead(A0) < 500){
        laser_on();
        buzzer_on();
        rgb_on();
    }
    else{
        laser_off();
        buzzer_off();
        rgb_off();
    }
}