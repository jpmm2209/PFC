#include <Arduino.h>
#include <GGClassification.h>
#include <ArduinoEigenDense.h>

using namespace Eigen;
extern Eigen::ArrayXXf X;
extern vector<int> y;
extern Eigen::ArrayXXf x_prd;

void setup() {
    Serial.begin(9600);
    delay(2000);

    MatrixXd m = MatrixXd::Random(3, 3);
    m = (m + MatrixXd::Constant(3, 3, 1.2)) * 50;

    Serial.println("m =");
    Serial.print(m(0, 0));
    Serial.print(" ");
    Serial.print(m(0, 1));
    Serial.print(" ");
    Serial.print(m(0, 2));
    Serial.println();
    Serial.print(m(1, 0));
    Serial.print(" ");
    Serial.print(m(1, 1));
    Serial.print(" ");
    Serial.print(m(1, 2));
    Serial.println();
    Serial.print(m(2, 0));
    Serial.print(" ");
    Serial.print(m(2, 1));
    Serial.print(" ");
    Serial.print(m(2, 2));
    Serial.println();

    VectorXd v(3);
    v << 1, 2, 3;
    VectorXd vo = m * v;

    Serial.println("m * v =");
    Serial.print(vo(0));
    Serial.println();
    Serial.print(vo(1));
    Serial.println();
    Serial.print(vo(2));
    Serial.println();
}

void loop()
{
  
  ListTest mdl = model(X, y);
  ArrayXi prd = predict(mdl, x_prd);


  delay(1000);
}