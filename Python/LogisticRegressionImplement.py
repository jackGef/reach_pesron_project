import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from LogisticRegression import LogisticRegression
from sklearn.preprocessing import StandardScaler

df = pd.read_json("C:/Users/Matan/OneDrive/שולחן העבודה/New folder/reach_pesron_project/Python/data.json")

df = df.iloc[:-1]
print(df.to_string())
X = df.iloc[:, :-1].astype(float).values

y = df.iloc[:, -1].values
y = np.where(y == "Kecimen\r", 1, 0).astype(float)
print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)



def accuracy(y_true, y_pred):
    return np.sum(y_true == y_pred) / len(y_true)


regressor = LogisticRegression(lr=5, n_iters=10)
regressor.fit(X_train, y_train)
predictions = regressor.predict(X_test)
print("LR classification accuracy:", accuracy(y_test, predictions))
