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

	Serial.println("X = [ ");
	for(int i = 0; i < X.rows() ; i++) {
		for(int j = 0; j < X.cols(); j++){
			Serial.print(X(i,j));
			Serial.print(" ");
		}
		Serial.println();
	}
	Serial.println(" ]");

	Serial.println("y.size() = ");
	Serial.println(y.size());
	Serial.println("x_prd.size() = ");
	Serial.println(x_prd.size());

	// Model
	ListTest mdl = model(Xi, y, false);

	Serial.println("Model Done!");
	ArrayXXd Xtest = x_prd.transpose();

	// Predict
	ArrayXi prd = predict(mdl, Xtest);

	Serial.println("Predict Done!");
	Serial.println("prd.size() = ");
	Serial.println(prd.size());


}

void loop()
{
	Serial.print(" .");
	delay(1000);
}