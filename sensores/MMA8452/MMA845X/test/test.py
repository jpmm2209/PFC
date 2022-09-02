import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv('testY.csv')

fig, axs = plt.subplots(3, 1, sharex=True)
axs[0].set(ylabel='Aceleração X')
axs[0].plot(df['AccX'])
axs[1].set(ylabel='Aceleração Y')
axs[1].plot(df['AccY'])
axs[2].set(ylabel='Aceleração Z')
axs[2].plot(df['AccZ'])

plt.show()