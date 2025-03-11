import pandas as pd
import numpy as np
import math


def get_x_y():
    df = pd.read_csv("C:/Users/Matan/OneDrive/שולחן העבודה/Raisin database/Raisin_Dataset.csv")

    # Convert features to numeric type and handle the X data
    X = df.iloc[:, :-1].astype(float).values.T  # Transpose at the end

    # Convert labels
    Y = df.iloc[:, -1].values
    Y = np.where(Y == "Kecimen", 1, 0).astype(float)
    return X, Y


def initialize_parameters():
    n = 7
    W = np.random.randn(n, 1) * 0.01

    b = 0
    return W, b


def linear_computation(X, W, b):
    Z = np.dot(W.T, X) + b
    return Z
    # return Z


def sigmoid(Z):
    return 1 / (1 + np.exp(-Z))
    # return A


def loss(A, Y):
    m = Y.shape[0]
    epsilon = 1e-15
    A = np.clip(A, epsilon, 1 - epsilon)

    return -1 / m * np.sum(Y * np.log(A) + (1 - Y) * np.log(1 - A))
    # return loss


def backward_propagation(X, A, Y):
    n = Y.shape[0]
    dZ = A - Y
    dW = 1 / n * np.dot(X, dZ.T)
    db = 1 / n * np.sum(dZ)
    return dW, db


def update_paramaters(W, b, dW, dB):
    L = 0.01
    W = W - L * dW
    b = b - L * dB
    return W, b


def main():
    X, Y = get_x_y()
    W, b = initialize_parameters()
    Z = linear_computation(X, W, b)
    A = sigmoid(Z)
    cost = loss(A, Y)
    print(cost)
    dW, dB = backward_propagation(X, A, Y)
    print("dW shape ",dW.shape,"dB shape ",dB.shape)
    W, b = update_paramaters(W, b, dW, dB)


main()
