import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from LogisticRegression import LogisticRegression
from sklearn.preprocessing import StandardScaler


def get_values():
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


    regressor = LogisticRegression(lr=5, n_iters=10)
    loss = regressor.fit(X_train, y_train)
    predictions = regressor.predict(X_test)

    model_accuracy = accuracy(y_test, predictions)

    print("LR classification accuracy:", model_accuracy)

    for i in range(len(predictions[0])):
            print(f"Value of predivted: {predictions[0][i]} Y => {y_test[i][0]}")
            if predictions[0][i] == y_test[i][0] and y_test[i][0] == 1:
                prediction_true_positive += 1
            elif predictions[0][i] == y_test[i][0] and y_test[i][0] == 0:
                prediction_true_negative += 1
            elif predictions[0][i] != y_test[i][0] and y_test[i][0] == 0:
                prediction_false_negative += 1
            elif predictions[0][i] != y_test[i][0] and y_test[i][0] == 1:
                prediction_false_positive += 1

    return model_accuracy, prediction_true_positive, prediction_true_negative, prediction_false_negative, prediction_false_positive, loss


def accuracy(y_true, y_pred):
    return np.sum(y_true == y_pred) / len(y_true)
