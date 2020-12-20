const int BUTTON1 = 2;
const int BUTTON2 = 4;
const int LED1 = 8;
const int LED2 = 12;
int BUTTONstate1 = 0;
int BUTTONstate2 = 0;

void setup()
{

  pinMode(BUTTON1, INPUT);
  pinMode(BUTTON2, INPUT);
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  Serial.begin(9600);
}

void loop()
{

  BUTTONstate1 = digitalRead(BUTTON1);
  if (BUTTONstate1 == HIGH)
  {
    digitalWrite(LED1, HIGH);
  } 
  else{
    digitalWrite(LED1, LOW);
  }
  BUTTONstate2 = digitalRead(BUTTON2);
  if (BUTTONstate2 == HIGH)
  {
    digitalWrite(LED2, HIGH);
  } 
  else{
    digitalWrite(LED2, LOW);
  }
  int value1 = analogRead(A0); 
  int value2 = analogRead(A1); 
  Serial.print(value1/200);
  Serial.print(",");
  Serial.println(value2/200);
  delay(500); 
}
