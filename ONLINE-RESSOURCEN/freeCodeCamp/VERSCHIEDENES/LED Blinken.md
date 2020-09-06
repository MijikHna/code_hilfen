* wird **Elegoo Uno R3 Starter Kit** benutzt.
    * ist MicroController Board.
    + hat 14 Digitale In/Outputs,
    + 6 Anagloge Inputs
    + USB-Verbindung
    + Power Jack
    + Reset Button
### Schritte:
1. LED mit GND (GND = Spannung von der Spannung gemessen wird also Null Volt für die Schaltung (muss aber nicht unbedingt null sein)) - eigentlich braucht man nicht, das LED auf dem Microkontroller an/aus gemacht
2. Code:
```c++
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on 
  delay(1000);                       // wait for a second
  digitalWrite(LED_BUILTIN, LOW);    // turn the LED off
  delay(1000);                       // wait for a second
}