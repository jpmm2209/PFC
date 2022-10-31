
##########################################################
#
#    Feature Engineering Stage 1: Data Distribution
#
##########################################################


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

# Distribution of each measurement for each activity
sns.set_style("whitegrid")
plt.figure()
sns.countplot(x = 'class', data = acc_data)
plt.title('activity-wise distribution')
sns.FacetGrid(acc_data, hue = 'class', size = 7).map(sns.distplot, 'AccX').add_legend()
sns.FacetGrid(acc_data, hue = 'class', size = 7).map(sns.distplot, 'AccY').add_legend()
sns.FacetGrid(acc_data, hue = 'class', size = 7).map(sns.distplot, 'AccZ').add_legend()
sns.FacetGrid(acc_data, hue = 'class', size = 7).map(sns.distplot, 'AngX').add_legend()
sns.FacetGrid(acc_data, hue = 'class', size = 7).map(sns.distplot, 'AngY').add_legend()
sns.FacetGrid(acc_data, hue = 'class', size = 7).map(sns.distplot, 'AngZ').add_legend()
plt.show()