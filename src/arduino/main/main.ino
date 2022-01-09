float temp;
bool prod = false;

void setup() {
  Serial.begin(9600);
}

void loop() {
  
  temp = random(200, 400) / 10;
  String stringOne = String(temp, 2);
  Serial.write(stringOne.c_str());
  delay(1000);
}
