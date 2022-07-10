#include <Arduino.h>
#include <GGClassification.h>

using namespace Eigen;
extern ArrayXXd X;
extern vector<int> y;
extern ArrayXXd x_prd;

void setup()
{

	Serial.begin(9600);
	Serial.println("\n \n --------Starting Program!---------");
	initValues();
	delay(2000);

	ArrayXXd Xi = X.transpose();
	ArrayXXd Xtest = x_prd.transpose();

	printArrayXXd(Xi, "Xi");
	printArrayXXd(Xtest, "Xtest");
	printVector(y, "y");
	
	// Model
	ListTest mdl = model(Xi, y, false);
	Serial.println("Model Done!");

	// Predict
	ArrayXi prd = predict(mdl, Xtest);
	Serial.println("Predict Done!");
	printArrayXi(prd, "Prediction");
}

void loop()
{
	Serial.print(" .");
	delay(1000);
}
