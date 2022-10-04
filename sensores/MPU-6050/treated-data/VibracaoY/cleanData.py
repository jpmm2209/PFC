import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv('rawVibracaoY.csv')

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
plt.plot(df[:15])
plt.show()

df[:15].to_csv("Parado_1", index=False)

# Vibracao Y
plt.title("Vibracao Y")
plt.plot(df[15:65])
plt.show()

df[15:65].to_csv("VibracaoY_1", index=False)

# Parado
plt.title("Parado")
plt.plot(df[65:90])
plt.show()

df[65:90].to_csv("Parado_2", index=False)

# Vibracao Y
plt.title("Vibracao Y")
plt.plot(df[90:145])
plt.show()

df[90:145].to_csv("VibracaoY_2", index=False)

# Parado 
plt.title("Parado")
plt.plot(df[145:160])
plt.show()

df[145:160].to_csv("Parado_3", index=False)

# Vibração leve Y
plt.title("Vibracao leve Y")
plt.plot(df[160:200])
plt.show()

df[160:200].to_csv("VibracaoY_3", index=False)

# Parado
plt.title("Parado")
plt.plot(df[210:225])
plt.show()

df[210:225].to_csv("Parado_4", index=False)

# Vibração leve Y
plt.title("Vibracao leve Y")
plt.plot(df[220:250])
plt.show()

df[220:250].to_csv("VibracaoY_4", index=False)

# noise
plt.title("noise")
plt.plot(df[250:290])
plt.show()

df[250:290].to_csv("noise_1", index=False)

# Parado
plt.title("Parado")
plt.plot(df[290:])
plt.show()

df[290:].to_csv("Parado_5", index=False)