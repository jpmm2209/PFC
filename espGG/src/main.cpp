#include <Arduino.h>
#include <espGG.h>
#include <CSV_Parser.h>

using namespace Eigen;
extern ArrayXXd X_test;
extern ArrayXXd X_train;
extern vector<int> y_train;
extern vector<int> y_test;
extern char *csv_str;

void setup()
{
	// Serial.begin(9600);
	// delay(5000);

	// CSV_Parser cp(csv_str, /*format*/ "sL");

	// Serial.println("Accessing values by column name:");
	// char **strings = (char **)cp["my_strings"];
	// int32_t *numbers = (int32_t *)cp["my_numbers"];

	// for (int row = 0; row < cp.getRowsCount(); row++)
	// {
	// 	Serial.print(row, DEC);
	// 	Serial.print(". String = ");
	// 	Serial.println(strings[row]);
	// 	Serial.print(row, DEC);
	// 	Serial.print(". Number = ");
	// 	Serial.println(numbers[row], DEC);
	// }
	// Serial.println();

	// Serial.println("Accessing values by column number:");
	// strings = (char **)cp[0];
	// numbers = (int32_t *)cp[1];

	// for (int row = 0; row < cp.getRowsCount(); row++)
	// {
	// 	Serial.print(row, DEC);
	// 	Serial.print(". String = ");
	// 	Serial.println(strings[row]);
	// 	Serial.print(row, DEC);
	// 	Serial.print(". Number = ");
	// 	Serial.println(numbers[row], DEC);
	// }

	/*
	  If we wanted to just check if the csv was parsed properly we could use:
	  cp.print();
	  (assumming that "Serial.begin(baud_rate)" was previously called. Because "cp.print()" is using "Serial" object)
	*/

	Serial.begin(9600);
	Serial.println("\n \n --------Starting Program!---------");
	initValues();
	delay(2000);

	// printArrayXXd(X_train, "X_train");
	// printArrayXXd(X_test, "X_test");
	// printVector(y_train, "y_train");

	// Model
	ListTest mdl = model(X_train, y_train, false);
	Serial.println("Model Done!");

	// Predict
	ArrayXi prd = predict(mdl, X_test);
	Serial.println("Predict Done!");
	printArrayXi(prd, "Prediction");

	// Acuracy
	float accuracy = testAccuracy(y_test, prd);
	Serial.print("Acurácia: ");
	Serial.print(accuracy);
	Serial.println("%");
}

void loop()
{
	Serial.print(" .");
	delay(1000);
}

float testAccuracy(vector<int> &y_hat, ArrayXi &y)
{
	int correct = 0;
	int sample;
	if (y_hat.size() != y.size())
	{
		Serial.print("y_hat.size() != y.size()");
		return 0;
	}
	for (sample = 0; sample < y_hat.size(); sample++)
	{
		if (y_hat[sample] == y(sample))
		{
			correct++;
		}
	}

	return (correct / sample) * 100;
}