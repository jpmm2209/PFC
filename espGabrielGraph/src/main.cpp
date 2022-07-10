#include <Arduino.h>
#include <GGClassification.h>

using namespace Eigen;
extern ArrayXXd X_test;
extern ArrayXXd X_train;
extern vector<int> y_train;

void setup()
{

	Serial.begin(9600);
	Serial.println("\n \n --------Starting Program!---------");
	initValues();
	delay(2000);

	printArrayXXd(X_train, "X_train");
	printArrayXXd(X_test, "X_test");
	printVector(y_train, "y_train");
	
	// Model
	ListTest mdl = model(X_train, y_train, false);
	Serial.println("Model Done!");

	// Predict
	ArrayXi prd = predict(mdl, X_test);
	Serial.println("Predict Done!");
	printArrayXi(prd, "Prediction");
}

void loop()
{
	Serial.print(" .");
	delay(1000);
}
