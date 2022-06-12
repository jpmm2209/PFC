#ifndef DEFINES_H_
#define DEFINES_H_

#include<Arduino.h>
#include <ArduinoEigen.h>
#include <vector>
#include <limits>
#include <cmath>

using std::vector;
using Eigen::ArrayXXd;
using Eigen::ArrayXd;
using Eigen::ArrayXi;

typedef Eigen::Map<ArrayXXd> MapArrayXXd;

using std::numeric_limits;
using std::vector;
using Eigen::ArrayXXd;
using Eigen::ArrayXXi;
using Eigen::ArrayXd;
using Eigen::ArrayXi;
using Eigen::VectorXi;
using Eigen::Ref;

typedef Eigen::Map<ArrayXXd> MapArrayXXd;

using std::numeric_limits;
using Eigen::ArrayXXd;
using Eigen::ArrayXXi;
using Eigen::Ref;

typedef Eigen::Map<ArrayXXd> MapArrayXXd;

typedef struct{
  ArrayXXd array_midpoints;
  ArrayXXd array_w;
  vector<double> vector_bias;
  vector<int> labels;
}ListTest;

ArrayXi predict(ListTest model, MapArrayXXd& X_array);
void RemoveArrayElementsByIndex(const ArrayXXd& data, int nrows, Ref<ArrayXXd> updated_data, vector<int> index_of_element_to_remove);
void RemoveVectorElementsByIndex(vector<int>& vector_of_classes, vector<int> index_of_element_to_remove);
void GabrielGraph(const ArrayXXd& data, int nrows, Ref<ArrayXXi> array_of_adjacency);
vector<int> FilterGraph(const ArrayXXi& array_of_adjacency, const vector<int>& vector_of_classes, const vector<int> labels);
ListTest GetModelParams(const ArrayXXi& array_of_adjacency, const ArrayXXd& data, int nrows, int ncols, const vector<int>& vector_of_classes, vector<int> labels);
vector<int> VerificationOfParameters(const ArrayXXd& X, const vector<int> Y);
ListTest model(MapArrayXXd& X_array, vector<int>& Y, bool normalize=false);



void RemoveArrayElementsByIndex(const ArrayXXd& data, int nrows, Ref<ArrayXXd> updated_data, vector<int> index_of_element_to_remove);
void RemoveVectorElementsByIndex(vector<int>& vector_of_classes, vector<int> index_of_element_to_remove);
void GabrielGraph(const ArrayXXd& data, int nrows, Ref<ArrayXXi> array_of_adjacency);
vector<int> FilterGraph(const ArrayXXi& array_of_adjacency, const vector<int>& vector_of_classes, const vector<int> labels);
ListTest GetModelParams(const ArrayXXi& array_of_adjacency, const ArrayXXd& data, int nrows, int ncols, const vector<int>& vector_of_classes, vector<int> labels);
vector<int> VerificationOfParameters(const ArrayXXd& X, const vector<int> Y);
ListTest model(MapArrayXXd& X_array, vector<int>& Y, bool normalize);



#endif /* DEFINES_H_ */