#include <Arduino.h>
#include <GGClassification.h>

using namespace Eigen;
extern Eigen::ArrayXXd X;
extern vector<int> y;
extern Eigen::ArrayXXd x_prd;

void setup() {
    Serial.begin(9600);
    Serial.println("Starting Program");
    initValues();
    delay(2000);


}

void loop()
{
  ArrayXXd Xi = X.transpose();

  ListTest mdl = model(Xi, y, false);
  ArrayXi prd = predict(mdl, x_prd);

  delay(1000);
}