import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('accelerometer.csv')

print(df)

data = df[(df["wconfid"] < 3)]
X = data[["x", "y", "z"]]
y = data[["wconfid"]]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=300, train_size=700)

X_train = pd.DataFrame(X_train)
X_test = pd.DataFrame(X_test)
y_train = pd.DataFrame(y_train)
y_test = pd.DataFrame(y_test)


X_train.to_csv('X_train.csv', sep=',', index=False, index_label=False, line_terminator=',\n')
X_test.to_csv('X_test.csv', sep=',', index=False, index_label=False, line_terminator=',\n')
y_train.to_csv('y_train.csv', sep=',', index=False, index_label=False, line_terminator=',')
y_test.to_csv('y_test.csv', sep=',', index=False, index_label=False, line_terminator=',')