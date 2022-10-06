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

# Noise
plt.title("Noise")
df.loc[:30,'class'] = 'Noise'
plt.plot(df[:30].drop(['class'], axis=1))
plt.show()
# df[:30].to_csv("Noise_1", index=False)

# Parado
plt.title("Parado")
df.loc[30:60,'class'] = 'Parado'
plt.plot(df[30:60].drop(['class'], axis=1))
plt.show()
# df[30:60].to_csv("Parado_1", index=False)

# Vibracao Z
plt.title("Vibracao Z")
df.loc[60:120,'class'] = 'VibracaoZ'
plt.plot(df[60:120].drop(['class'], axis=1))
plt.show()
# df[60:120].to_csv("VibracaoZ_1", index=False)

# Parado 
plt.title("Parado")
df.loc[120:145,'class'] = 'Parado'
plt.plot(df[120:145].drop(['class'], axis=1))
plt.show()
# df[120:145].to_csv("Parado_2", index=False)

# Vibração Z
plt.title("Vibracao Z")
df.loc[120:180,'class'] = 'VibracaoZ'
plt.plot(df[120:180].drop(['class'], axis=1))
plt.show()
# df[120:180].to_csv("VibracaoZ_2", index=False)

# Parado
plt.title("Parado")
df.loc[180:200,'class'] = 'Parado'
plt.plot(df[180:200].drop(['class'], axis=1))
plt.show()
# df[180:200].to_csv("Parado_3", index=False)

# Vibração Z
plt.title("Vibracao Z")
df.loc[200:250,'class'] = 'VibracaoZ'
plt.plot(df[200:250].drop(['class'], axis=1))
plt.show()
# df[200:250].to_csv("VibracaoZ_3", index=False)

# Parado
plt.title("Parado")
df.loc[250:,'class'] = 'Parado'
plt.plot(df[250:].drop(['class'], axis=1))
plt.show()
# df[250:].to_csv("Parado_4", index=False)

# Classified final data
df.to_csv("classifiedVibracaoZ.csv", index=False)