#include <Arduino.h>
#include <MPU6050_light.h>
#include <Adafruit_SSD1306.h>
#include <Adafruit_Sensor.h>
#include "Wire.h"
#include <iostream>

MPU6050 mpu(Wire);

// ----- main setup -----
void setup()
{
	Serial.begin(115200);
	Wire.begin();

	Serial.println("\n\n ----- Starting MPU! ------- \n\n");


	// -----MPU Setup -----
	byte status = mpu.begin(3, 3);
	Serial.print(F("MPU6050 status: "));
	Serial.println(status);

	Serial.println("Starting MPU loop!\n");

	Serial.print("AccX,AccY,AccZ,AngX,AngY,AngZ\n");

}

// ----- main loop -----
void loop()
{
	mpu.update();

	// Output data to serial monitor
	Serial.print(mpu.getAccX());
	Serial.print(",");
	Serial.print(mpu.getAccY());
	Serial.print(",");
	Serial.print(mpu.getAccZ());
	Serial.print(",");
	Serial.print(mpu.getAngleX());
	Serial.print(",");
	Serial.print(mpu.getAngleY());
	Serial.print(",");
	Serial.print(mpu.getAngleZ());
	Serial.println();

	delay(50);
}
