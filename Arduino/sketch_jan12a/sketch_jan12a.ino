const int buttonPin_113 = 0; // 버튼 핀
const int ledPin_113 = 8;   // LED 핀
const int buttonPin_119 = 1; // 버튼 핀
const int ledPin_119 = 9;   // LED 핀
const int buttonPin_211 = 2; // 버튼 핀
const int ledPin_211 = 10;   // LED 핀

int buttonState_113 = 0;     // 버튼 상태 저장
int lastButtonState_113 = 0; // 이전 버튼 상태 저장
int buttonState_119 = 0;     // 버튼 상태 저장
int lastButtonState_119 = 0; // 이전 버튼 상태 저장
int buttonState_211 = 0;     // 버튼 상태 저장
int lastButtonState_211 = 0; // 이전 버튼 상태 저장

void setup() {
  pinMode(buttonPin_113, INPUT);
  pinMode(buttonPin_119, INPUT);
  pinMode(buttonPin_211, INPUT);
  pinMode(ledPin_113, OUTPUT);
  pinMode(ledPin_119, OUTPUT);
  pinMode(ledPin_211, OUTPUT);
}

void loop() {
  buttonState_113 = digitalRead(buttonPin_113);
  buttonState_211 = digitalRead(buttonPin_211);
  buttonState_119 = digitalRead(buttonPin_119);

  // 버튼이 눌렸을 때(113)
  if (buttonState_113 == HIGH && lastButtonState_113 == LOW) {
    digitalWrite(ledPin_113, !digitalRead(ledPin_113)); // LED 상태를 반전시킴
  }
  lastButtonState_113 = buttonState_113;

  // 버튼이 눌렸을 때(119)
  if (buttonState_119 == HIGH && lastButtonState_119 == LOW) {
    digitalWrite(ledPin_119, !digitalRead(ledPin_119)); // LED 상태를 반전시킴
  }
  lastButtonState_119 = buttonState_119;

  // 버튼이 눌렸을 때(211)
  if (buttonState_211 == HIGH && lastButtonState_211 == LOW) {
    digitalWrite(ledPin_211, !digitalRead(ledPin_211)); // LED 상태를 반전시킴
  }
  lastButtonState_211 = buttonState_211;
}
