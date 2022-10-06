
##########################################################
#
#    Feature Engineering Stage 1: Statistical measures
#
##########################################################


import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# reading raw data file
acc_data = pd.read_csv('classifiedData.csv')
print('\nclassifiedData\n')
title = 'classifiedData'

# removing null values
acc_data = acc_data.dropna()
acc_data.shape

# mean
x_mean = acc_data['AccX'].mean()
print("x_mean", x_mean)
y_mean = acc_data['AccY'].mean()
print("y_mean", y_mean)
z_mean = acc_data['AccZ'].mean()
print("z_mean", z_mean)

# # # std dev
# # X_train['x_std'] = pd.Series(x_list).apply(lambda x: x.std())

# # avg absolute diff
# x_aad = acc_data['AccX'].apply(lambda x: np.mean(np.absolute(x - np.mean(x))))
# print("x_aad", x_aad)
# y_aad = acc_data['AccY'].apply(lambda x: np.mean(np.absolute(x - np.mean(x))))
# print("y_aad", y_aad)
# z_aad = acc_data['AccZ'].apply(lambda x: np.mean(np.absolute(x - np.mean(x))))
# print("z_aad", z_aad)

# min
x_min = acc_data['AccX'].min()
print("x_min", x_min)
y_min = acc_data['AccY'].min()
print("y_min", y_min)
z_min = acc_data['AccZ'].min()
print("z_min", z_min)

# max
x_max = acc_data['AccX'].max()
print("x_max", x_max)
y_max = acc_data['AccY'].max()
print("y_max", y_max)
z_max = acc_data['AccZ'].max()
print("z_max", z_max)

# max-min diff
x_maxmin_diff = x_max - x_min
print("x_maxmin_diff", x_maxmin_diff)
y_maxmin_diff = y_max - y_min
print("y_maxmin_diff", y_maxmin_diff)
z_maxmin_diff = z_max - z_min
print("z_maxmin_diff", z_maxmin_diff)

# # median
# X_train['x_median'] = acc_data['AccX'].apply(lambda x: np.median(x))

# # # median abs dev 
# # X_train['x_mad'] = acc_data['AccX'].apply(lambda x: np.median(np.absolute(x - np.median(x))))

# # # interquartile range
# # X_train['x_IQR'] = acc_data['AccX'].apply(lambda x: np.percentile(x, 75) - np.percentile(x, 25))

# # negtive count
# x_neg_count = acc_data['AccX'].apply(lambda x: np.sum(x < 0))
# print("x_neg_count", x_neg_count)
# y_neg_count = acc_data['AccY'].apply(lambda x: np.sum(x < 0))
# print("y_neg_count", y_neg_count)
# z_neg_count = acc_data['AccZ'].apply(lambda x: np.sum(x < 0))
# print("z_neg_count", z_neg_count)

# # positive count
# x_pos_count = acc_data['AccX'].apply(lambda x: np.sum(x > 0))
# print("x_pos_count", x_pos_count)
# y_pos_count = acc_data['AccY'].apply(lambda x: np.sum(x > 0))
# print("y_pos_count", y_pos_count)
# z_pos_count = acc_data['AccZ'].apply(lambda x: np.sum(x > 0))
# print("z_pos_count", z_pos_count)

# # values above mean
# x_above_mean = acc_data['AccX'].apply(lambda x: np.sum(x > x.mean()))
# print("x_above_mean", x_above_mean)
# y_above_mean = acc_data['AccY'].apply(lambda x: np.sum(x > x.mean()))
# print("y_above_mean", y_above_mean)
# z_above_mean = acc_data['AccZ'].apply(lambda x: np.sum(x > x.mean()))
# print("z_above_mean", z_above_mean)

# # number of peaks
# x_peaks = acc_data['AccX'].apply(lambda x: len(find_peaks(x)[0]))
# print("x_peaks", x_peaks)
# y_peaks = acc_data['AccY'].apply(lambda x: len(find_peaks(x)[0]))
# print("y_peaks", y_peaks)
# z_peaks = acc_data['AccZ'].apply(lambda x: len(find_peaks(x)[0]))
# print("z_peaks", z_peaks)

# # # skewness
# # X_train['x_skewness'] = acc_data['AccX'].apply(lambda x: stats.skew(x))

# # # kurtosis
# # X_train['x_kurtosis'] = acc_data['AccX'].apply(lambda x: stats.kurtosis(x))

# # # energy
# x_energy = acc_data['AccX'].apply(lambda x: np.sum(x**2)/100)
# print("x_energy", x_energy)

# # avg resultant
# avg_result_accl = [i.mean() for i in ((acc_data['AccX']**2 + acc_data['AccY']**2 + acc_data['AccZ']**2)**0.5)]
# print("avg_result_accl", avg_result_accl)

# # signal magnitude area
# sig_mag_area = acc_data['AccX'].apply(lambda x: np.sum(abs(x)/100)) + acc_data['AccY'].apply(lambda x: np.sum(abs(x)/100)) + acc_data['AccZ'].apply(lambda x: np.sum(abs(x)/100))
# print("sig_mag_area", sig_mag_area)
