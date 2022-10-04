import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv('rawCirculoZ.csv')

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

# noise
plt.title("noise")
plt.plot(df[:20])
plt.show()

df[:20].to_csv("noise_1", index=False)


# Parado
plt.title("Parado")
plt.plot(df[20:40])
plt.show()

df[20:40].to_csv("Parado_1", index=False)

# Circulo Z
plt.title("Circulo Z")
plt.plot(df[40:75])
plt.show()

df[40:75].to_csv("CirculoZ_1", index=False)


# Parado
plt.title("Parado")
plt.plot(df[75:110])
plt.show()

df[75:110].to_csv("Parado_2", index=False)

# Circulo Z
plt.title("Circulo Z")
plt.plot(df[110:145])
plt.show()

df[110:145].to_csv("CirculoZ_2", index=False)

# Parado 
plt.title("Parado")
plt.plot(df[145:180])
plt.show()

df[145:180].to_csv("Parado_2", index=False)

# Circulo Z
plt.title("Circulo Z")
plt.plot(df[180:210])
plt.show()

df[180:210].to_csv("CirculoZ_3", index=False)

# Parado 
plt.title("Parado")
plt.plot(df[210:240])
plt.show()

df[210:240].to_csv("Parado_3", index=False)

# noise
plt.title("noise")
plt.plot(df[240:250])
plt.show()

df[240:250].to_csv("noise_2", index=False)

# Parado 
plt.title("Parado")
plt.plot(df[260:])
plt.show()

df[260:].to_csv("Parado_4", index=False)