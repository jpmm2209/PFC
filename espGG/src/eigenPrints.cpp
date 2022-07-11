#include <espGG.h>


void printArrayXXd(ArrayXXd &array, String arrayName)
{
	Serial.println(arrayName + " = [ ");
	for (int i = 0; i < array.rows(); i++)
	{
		for (int j = 0; j < array.cols(); j++)
		{
			Serial.print(array(i, j));
			Serial.print(" ");
		}
		Serial.println();
	}
	Serial.println(" ]");
}

void printVector(vector<int> &array, String arrayName)
{
	Serial.println(arrayName + " = [ ");
	for (int i = 0; i < array.size(); i++)
	{
		Serial.print(array[i]);
		Serial.print(" ");
	}
	Serial.println();
	Serial.println(" ]");
}

void printArrayXi(ArrayXi &array, String arrayName)
{
	Serial.println(arrayName + " = [ ");
	for (int i = 0; i < array.size(); i++)
	{
		Serial.print(array(i));
		Serial.print(" ");
	}
	Serial.println();
	Serial.println(" ]");
}