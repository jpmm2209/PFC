#ifndef DEFINES_H_
#define DEFINES_H_

#include<Arduino.h>
#include <ArduinoEigen.h>
#include <vector>
#include <limits>
#include <cmath>
#include <ArduinoEigenDense.h>
#include<ArduinoEigenSparse.h>


using std::numeric_limits;
using std::vector;
using Eigen::ArrayXXd;
using Eigen::ArrayXXi;
using Eigen::ArrayXd;
using Eigen::ArrayXi;
using Eigen::MatrixXd;
using Eigen::VectorXi;
using Eigen::Ref;
using Eigen::VectorwiseOp;

typedef Eigen::Map<ArrayXXd> MapArrayXXd;  // Array<double,Dynamic,Dynamic> = ArrayXXd
typedef Eigen::Map<ArrayXd> MapArrayXd;  // Array<double,Dynamic,Dynamic> = ArrayXd

typedef struct{
  ArrayXXd array_midpoints;
  ArrayXXd array_w;
  vector<double> vector_bias;
  vector<int> labels;
}ListTest;

ArrayXi predict(ListTest model,const ArrayXXd& X_array);
void RemoveArrayElementsByIndex(const ArrayXXd& data, int nrows, Ref<ArrayXXd> updated_data, vector<int> index_of_element_to_remove);
void RemoveVectorElementsByIndex(vector<int>& vector_of_classes, vector<int> index_of_element_to_remove);
void GabrielGraph(const ArrayXXd& data, int nrows, Ref<ArrayXXi> array_of_adjacency);
vector<int> FilterGraph(const ArrayXXi& array_of_adjacency, const vector<int>& vector_of_classes, const vector<int> labels);
ListTest GetModelParams(const ArrayXXi& array_of_adjacency, const ArrayXXd& data, int nrows, int ncols, const vector<int>& vector_of_classes, vector<int> labels);
vector<int> VerificationOfParameters(const ArrayXXd& X, const vector<int> Y);
ListTest model(ArrayXXd& X_array, vector<int>& Y, bool normalize);
void initValues();
void printArrayXXd(ArrayXXd &array, String arrayName);
void printVector(vector<int> &array, String arrayName);
void printArrayXi(ArrayXi &array, String arrayName);



#endif /* DEFINES_H_ */