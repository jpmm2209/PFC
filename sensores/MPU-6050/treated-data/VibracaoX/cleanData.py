import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv('rawVibracaoX.csv')

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
df.loc[0:15,'class'] = 'Parado'
plt.plot(df[0:15].drop(['class'], axis=1))
plt.show()
# df[0:30].to_csv("Parado_1", index=False)

# Vibracao X
plt.title("Vibracao X")
df.loc[15:100,'class'] = 'VibracaoX'
plt.plot(df[15:100].drop(['class'], axis=1))
plt.show()
# df[15:100].to_csv("VibracaoX_1", index=False)

# Noise
plt.title("Noise")
df.loc[100:200,'class'] = 'Noise'
plt.plot(df[100:200].drop(['class'], axis=1))
plt.show()
# df[100:200].to_csv("Parado_1", index=False)

# Vibracao X
plt.title("Vibracao X")
df.loc[200:255,'class'] = 'VibracaoX'
plt.plot(df[200:255].drop(['class'], axis=1))
plt.show()
# df[200:255].to_csv("VibracaoX_2", index=False)

# Parado 
plt.title("Parado")
df.loc[255:290,'class'] = 'Parado'
plt.plot(df[255:290].drop(['class'], axis=1))
plt.show()
# df[255:290].to_csv("Parado_2", index=False)

# Vibração leve X
plt.title("Vibracao leve X")
df.loc[290:360,'class'] = 'VibracaoX'
plt.plot(df[290:360].drop(['class'], axis=1))
plt.show()
# df[290:340].to_csv("VibracaoX_3", index=False)

# Parado
plt.title("Parado")
df.loc[360:,'class'] = 'Parado'
plt.plot(df[360:].drop(['class'], axis=1))
plt.show()
# df[340:].to_csv("Parado_3", index=False)

# Classified final data
df.to_csv("classifiedVibracaoX.csv", index=False)