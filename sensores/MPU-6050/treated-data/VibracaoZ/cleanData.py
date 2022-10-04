import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv('rawVibracaoZ.csv')

fig, axs = plt.subplots(6, 1, sharex=True)
axs[0].set(ylabel='Aceleração X')
axs[0].plot(df['AccX'])
axs[1].set(ylabel='Aceleração Y')
axs[1].plot(df['AccY'])
axs[2].set(ylabel='Aceleração Z')
axs[2].plot(df['AccZ'])
axs[3].set(ylabel='Angulo X')
axs[3].plot(df['AngX'])
axs[4].set(ylabel='Angulo Y')
axs[4].plot(df['AngY'])
axs[5].set(ylabel='Angulo Z')
axs[5].plot(df['AngZ'])

plt.show()

####################
#
#   Classificação
#
####################

# Noisa
plt.title("Noisa")
plt.plot(df[0:30])
plt.show()

df[0:30].to_csv("Noise_1", index=False)

# Parado
plt.title("Parado")
plt.plot(df[30:60])
plt.show()

df[30:60].to_csv("Parado_1", index=False)

# Vibracao Z
plt.title("Vibracao Z")
plt.plot(df[60:120])
plt.show()

df[60:120].to_csv("VibracaoZ_1", index=False)

# Parado 
plt.title("Parado")
plt.plot(df[120:145])
plt.show()

df[120:145].to_csv("Parado_2", index=False)

# Vibração Z
plt.title("Vibracao Z")
plt.plot(df[120:180])
plt.show()

df[120:180].to_csv("VibracaoZ_2", index=False)

# Parado
plt.title("Parado")
plt.plot(df[180:200])
plt.show()

df[180:200].to_csv("Parado_3", index=False)

# Vibração Z
plt.title("Vibracao Z")
plt.plot(df[200:250])
plt.show()

df[200:250].to_csv("VibracaoZ_3", index=False)

# Parado
plt.title("Parado")
plt.plot(df[250:])
plt.show()

df[250:].to_csv("Parado_4", index=False)