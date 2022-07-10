#include <Arduino.h>
#include <GGClassification.h>

using namespace Eigen;
extern ArrayXXd X;
extern vector<int> y;
extern ArrayXXd x_prd;

void setup()
{
	Serial.begin(9600);
	Serial.println("Starting Program");
	initValues();
	delay(2000);
}

void loop()
{

	Serial.println("\n \n------- LOOP ---------");

	ArrayXXd Xi = X.transpose();

	Serial.println("X.size() = ");
	Serial.println(X.size());

	Serial.println("y.size() = ");
	Serial.println(y.size());

	Serial.println("x_prd.size() = ");
	Serial.println(x_prd.size());

	ListTest mdl = model(Xi, y, false);

	Serial.println("Model Done!");

	ArrayXXd Xtest = x_prd.transpose();

	ArrayXi prd = predict(mdl, Xtest);

	Serial.println("Predict Done!");

	Serial.println("prd.size() = ");
	Serial.println(prd.size());

	delay(1000);
}