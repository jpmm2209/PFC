# importing libraries
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.signal import find_peaks
import warnings
warnings.filterwarnings('ignore')

# reading raw data file
acc_data = pd.read_csv('classifiedData.csv')
print('\nclassifiedData\n')
title = 'classifiedData'

# removing null values
acc_data = acc_data.dropna()
acc_data.shape

x_acc_list = []
y_acc_list = []
z_acc_list = []
x_ang_list = []
y_ang_list = []
z_ang_list = []
class_list = []

window_size = 100
step_size = 50

# creating overlaping windows of size window-size 100
for i in range(0, acc_data.shape[0] - window_size, step_size):
    x_acc = acc_data['AccX'].values[i: i + 100]
    y_acc = acc_data['AccY'].values[i: i + 100]
    z_acc = acc_data['AccZ'].values[i: i + 100]
    x_ang = acc_data['AngX'].values[i: i + 100]
    y_ang = acc_data['AngY'].values[i: i + 100]
    z_ang = acc_data['AngZ'].values[i: i + 100]
    label = stats.mode(acc_data['Class'][i: i + 100])[0][0]

    x_acc_list.append(x_acc)
    y_acc_list.append(y_acc)
    z_acc_list.append(z_acc)
    x_ang_list.append(x_ang)
    y_ang_list.append(y_ang)
    z_ang_list.append(z_ang)
    class_list.append(label)

# Statistical Features on raw x, y and z in time domain
X_train = pd.DataFrame()

# print("\nx_acc_list: ", x_acc_list)
# print("\ny_acc_list: ", y_acc_list)
# print("\nz_acc_list: ", z_acc_list)
# print("\nx_ang_list: ", x_ang_list)
# print("\ny_ang_list: ", y_ang_list)
# print("\nz_ang_list: ", z_ang_list)
print("\nclass_list: ", class_list)

# mean
X_train['acc_x_mean'] = pd.Series(x_acc_list).apply(lambda x: x.mean())
X_train['acc_y_mean'] = pd.Series(y_acc_list).apply(lambda x: x.mean())
X_train['acc_z_mean'] = pd.Series(z_acc_list).apply(lambda x: x.mean())
X_train['ang_x_mean'] = pd.Series(x_ang_list).apply(lambda x: x.mean())
X_train['ang_y_mean'] = pd.Series(y_ang_list).apply(lambda x: x.mean())
X_train['ang_z_mean'] = pd.Series(z_ang_list).apply(lambda x: x.mean())

print("\nX_train['acc_x_mean']: ", X_train['acc_x_mean'])
print("\nX_train['acc_y_mean']: ", X_train['acc_y_mean'])
print("\nX_train['acc_z_mean']: ", X_train['acc_z_mean'])
print("\nX_train['ang_x_mean']: ", X_train['ang_x_mean'])
print("\nX_train['ang_y_mean']: ", X_train['ang_y_mean'])
print("\nX_train['ang_z_mean']: ", X_train['ang_z_mean'])

# std dev
X_train['acc_x_std'] = pd.Series(x_acc_list).apply(lambda x: x.std())
X_train['acc_y_std'] = pd.Series(y_acc_list).apply(lambda x: x.std())
X_train['acc_z_std'] = pd.Series(z_acc_list).apply(lambda x: x.std())
X_train['ang_x_std'] = pd.Series(x_ang_list).apply(lambda x: x.std())
X_train['ang_y_std'] = pd.Series(y_ang_list).apply(lambda x: x.std())
X_train['ang_z_std'] = pd.Series(z_ang_list).apply(lambda x: x.std())


# avg absolute diff
X_train['acc_x_aad'] = pd.Series(x_acc_list).apply(lambda x: np.mean(np.absolute(x - np.mean(x))))
X_train['acc_y_aad'] = pd.Series(y_acc_list).apply(lambda x: np.mean(np.absolute(x - np.mean(x))))
X_train['acc_z_aad'] = pd.Series(z_acc_list).apply(lambda x: np.mean(np.absolute(x - np.mean(x))))
X_train['ang_x_aad'] = pd.Series(x_ang_list).apply(lambda x: np.mean(np.absolute(x - np.mean(x))))
X_train['ang_y_aad'] = pd.Series(y_ang_list).apply(lambda x: np.mean(np.absolute(x - np.mean(x))))
X_train['ang_z_aad'] = pd.Series(z_ang_list).apply(lambda x: np.mean(np.absolute(x - np.mean(x))))



