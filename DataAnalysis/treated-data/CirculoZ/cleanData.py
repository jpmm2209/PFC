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
df.loc[:20,'class'] = 'Noise'
plt.plot(df[:20].drop(['class'], axis=1))
plt.legend(['AccX','AccY','AccZ','AngX','AngY','AngZ'])
plt.show()
# df[:20].to_csv("noise_1", index=False)


plt.title("Parado")
df.loc[20:40,'class'] = 'Parado'
plt.plot(df[20:40].drop(['class'], axis=1))
plt.legend(['AccX','AccY','AccZ','AngX','AngY','AngZ'])
plt.show()
# df[20:40].to_csv("Parado_1", index=False)


# Circulo Z
plt.title("Circulo Z")
df.loc[40:75,'class'] = 'CirculoZ'
plt.plot(df[40:75].drop(['class'], axis=1))
plt.legend(['AccX','AccY','AccZ','AngX','AngY','AngZ'])
plt.show()
# df[40:75].to_csv("CirculoZ_1", index=False)


# Parado
plt.title("Parado")
df.loc[75:110,'class'] = 'Parado'
plt.plot(df[75:110].drop(['class'], axis=1))
plt.legend(['AccX','AccY','AccZ','AngX','AngY','AngZ'])
plt.show()
# df[75:110].to_csv("Parado_2", index=False)

# Circulo Z
plt.title("Circulo Z")
df.loc[110:145,'class'] = 'CirculoZ'
plt.plot(df[110:145].drop(['class'], axis=1))
plt.legend(['AccX','AccY','AccZ','AngX','AngY','AngZ'])
plt.show()
# df[110:145].to_csv("CirculoZ_2", index=False)

# Parado 
plt.title("Parado")
df.loc[145:180,'class'] = 'Parado'
plt.plot(df[145:180].drop(['class'], axis=1))
plt.legend(['AccX','AccY','AccZ','AngX','AngY','AngZ'])
plt.show()
# df[145:180].to_csv("Parado_2", index=False)

# Circulo Z
plt.title("Circulo Z")
df.loc[180:210,'class'] = 'CirculoZ'
plt.plot(df[180:210].drop(['class'], axis=1))
plt.legend(['AccX','AccY','AccZ','AngX','AngY','AngZ'])
plt.show()
# df[180:210].to_csv("CirculoZ_3", index=False)

# Parado 
plt.title("Parado")
df.loc[210:240,'class'] = 'Parado'
plt.plot(df[210:240].drop(['class'], axis=1))
plt.legend(['AccX','AccY','AccZ','AngX','AngY','AngZ'])
plt.show()
# df[210:240].to_csv("Parado_3", index=False)

# noise
plt.title("noise")
df.loc[240:250,'class'] = 'Noise'
plt.plot(df[240:250].drop(['class'], axis=1))
plt.legend(['AccX','AccY','AccZ','AngX','AngY','AngZ'])
plt.show()
# df[240:250].to_csv("noise_2", index=False)

# Parado 
plt.title("Parado")
df.loc[260:,'class'] = 'Parado'
plt.plot(df[260:].drop(['class'], axis=1))
plt.legend(['AccX','AccY','AccZ','AngX','AngY','AngZ'])
plt.show()
# df[260:].to_csv("Parado_4", index=False)


# Classified final data
df.to_csv("classifiedCirculoZ.csv", index=False)