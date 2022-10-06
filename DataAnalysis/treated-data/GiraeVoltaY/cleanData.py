import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from pyparsing import col

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
df.loc[0:50,'class'] = 'Parado'
plt.plot(df[0:50].drop(['class'], axis=1))
plt.show()
# df[0:50].to_csv("Parado_1", index=False)

# Gira e Volta Y
plt.title("Gira e Volta Y")
df.loc[50:75,'class'] = 'GiraeVoltaY'
plt.plot(df[50:75].drop(['class'], axis=1))
plt.show()
# df[50:75].to_csv("GiraeVoltaY_1", index=False)

# Parado
plt.title("Parado")
df.loc[75:115,'class'] = 'Parado'
plt.plot(df[75:115].drop(['class'], axis=1))
plt.show()
# df[75:115].to_csv("Parado_2", index=False)

# Gira e Volta Y
plt.title("Gira e Volta Y")
df.loc[115:140,'class'] = 'GiraeVoltaY'
plt.plot(df[115:140].drop(['class'], axis=1))
plt.show()
# df[115:140].to_csv("GiraeVoltaY_2", index=False)

# Parado 
plt.title("Parado")
df.loc[140:165,'class'] = 'Parado'
plt.plot(df[140:165].drop(['class'], axis=1))
plt.show()
# df[140:165].to_csv("Parado_3", index=False)

# Gira e Volta Y
plt.title("Gira e Volta Y")
df.loc[165:190,'class'] = 'GiraeVoltaY'
plt.plot(df[165:190].drop(['class'], axis=1))
plt.show()
# df[165:190].to_csv("GiraeVoltaY_3", index=False)

# Parado 
plt.title("Parado")
df.loc[190:215,'class'] = 'Parado'
plt.plot(df[190:215].drop(['class'], axis=1))
plt.show()
# df[190:215].to_csv("Parado_4", index=False)

# Gira e Volta Y
plt.title("Gira e Volta Y")
df.loc[215:235,'class'] = 'GiraeVoltaY'
plt.plot(df[215:235].drop(['class'], axis=1))
plt.show()
# df[215:235].to_csv("GiraeVoltaY_4", index=False)

# noise
plt.title("noise")
df.loc[235:260,'class'] = 'Noise'
plt.plot(df[235:260].drop(['class'], axis=1))
plt.show()
# df[235:260].to_csv("noise_1", index=False)

# Parado 
plt.title("Parado")
df.loc[260:,'class'] = 'Parado'
plt.plot(df[260:].drop(['class'], axis=1))
plt.show()
# df[260:].to_csv("Parado_5", index=False)


# Classified final data
df.to_csv("classifiedGiraeVolta.csv", index=False)