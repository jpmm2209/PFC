import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv('rawGiraeVoltaY.csv')

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

# Parado
plt.title("Parado")
plt.plot(df[0:50])
plt.show()

df[0:50].to_csv("Parado_1", index=False)

# Gira e Volta Y
plt.title("Gira e Volta Y")
plt.plot(df[50:75])
plt.show()

df[50:75].to_csv("GiraeVoltaY_1", index=False)

# Parado
plt.title("Parado")
plt.plot(df[75:115])
plt.show()

df[75:115].to_csv("Parado_2", index=False)

# Gira e Volta Y
plt.title("Gira e Volta Y")
plt.plot(df[115:140])
plt.show()

df[115:140].to_csv("GiraeVoltaY_2", index=False)

# Parado 
plt.title("Parado")
plt.plot(df[140:165])
plt.show()

df[140:165].to_csv("Parado_3", index=False)

# Gira e Volta Y
plt.title("Gira e Volta Y")
plt.plot(df[165:190])
plt.show()

df[165:190].to_csv("GiraeVoltaY_3", index=False)

# Parado 
plt.title("Parado")
plt.plot(df[190:215])
plt.show()

df[190:215].to_csv("Parado_4", index=False)

# Gira e Volta Y
plt.title("Gira e Volta Y")
plt.plot(df[215:235])
plt.show()

df[215:235].to_csv("GiraeVoltaY_4", index=False)

# noise
plt.title("noise")
plt.plot(df[235:260])
plt.show()

df[235:260].to_csv("noise_1", index=False)

# Parado 
plt.title("Parado")
plt.plot(df[260:])
plt.show()

df[260:].to_csv("Parado_5", index=False)