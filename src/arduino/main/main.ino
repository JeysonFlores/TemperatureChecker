#include "DHT.h"

#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

float temp;
bool prod = false;

void setup() {
  Serial.begin(9600);
}

void loop() {  
  temp = readTemperature();
  String stringOne = String(temp, 2);
  Serial.write(stringOne.c_str());
  delay(300000);
}

float readTemperature(){
  if (prod) {
    return dht.readTemperature();
  } else {
    return random(200, 400) / 10.0;
  }
}
