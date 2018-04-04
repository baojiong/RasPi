#include<stdio.h>
#include<wiringPi.h>
#include<time.h>

void main() {
	wiringPiSetup();
	pinMode(17, OUTPUT);
	printf("\n Hi, I am using wiringPi, Blink Blink!");
	printf("\n Press ctrl C to exit\n");
	for(;;) {
		digitalWrite(17, HIGH);
		delay(1000);
		digitalWrite(17, LOW);
		delay(500);
	}
}
