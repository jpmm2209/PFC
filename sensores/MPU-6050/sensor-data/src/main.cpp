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

}

// ----- main loop -----
void loop()
{
	mpu.update();

	// Raw MPU
	std::cout << mpu.getAccX() << " " << mpu.getAccY() << " " << mpu.getAccZ() << std::endl;
	std::cout << mpu.getAngleX() << " " << mpu.getAngleY() << " " << mpu.getAngleZ() << std::endl;

	Serial.println();

	delay(500);
}
