import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv('rawVibracaoZ.csv')

fig, axs = plt.subplots(6, 1, sharex=True)
axs[0].set(ylabel='AccX')
axs[0].plot(df['AccX'])
axs[1].set(ylabel='AccY')
axs[1].plot(df['AccY'])
axs[2].set(ylabel='AccX')
axs[2].plot(df['AccZ'])
axs[3].set(ylabel='AngX')
axs[3].plot(df['AngX'])
axs[4].set(ylabel='AngY')
axs[4].plot(df['AngY'])
axs[5].set(ylabel='AngZ')
axs[5].plot(df['AngZ'])


plt.show()