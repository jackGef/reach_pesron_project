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
    X = X.T
    X_80 = int((80 * (len(X) - 1)) / 100)
    train_X_change, train_Y_change = X[1:X_80, :(len(X[1]) )], X[1:X_80, (len(X[1]) - 1):]
    test_X_change, test_Y_change = X[X_80:, :(len(X[1]) )], X[X_80:, (len(X[1]) - 1):]
    print(train_X_change.shape)
    print(test_X_change.shape)

    sum_of_cost = 0
    batches_number = 40

    batch_length = int(len(train_Y_change[1])/batches_number)

    for epoch in range(100000):

        sum_of_cost = 0

        for batch_number in range(number_of_batches):
            train_X = X_80[0:, (batch_number * batch_length):((batch_number + 1) * batch_length)]
            train_Y = Y_80[(batch_number * batch_length):((batch_number + 1) * batch_length), 0:]

            # Initilize parameters X and Y of train_data_obj
            train_data_obj.initilize_X_Y(train_X, train_Y)

            # Initlize the parameters W and m(number of examples) of train_data_obj
            parameters = train_data_obj.initilize_parameters(train_X)

            # A for loop to train the the model n times

            # Calculate the Z matrice for the sigmoid function
            Z = train_data_obj.linear_computation(train_X)

            # Calculate the activation function sigmoid
            A = train_data_obj.sigmoid(Z)

            # Calculate the cost of the activation function
            cost = train_data_obj.cost(A, train_Y)

            sum_of_cost += cost[0][0]

            # Print cost and number of itiration every n times

            # Calculate the grads to update parameters W and b
            grads = train_data_obj.backward_propagation(A, train_Y)

            # Update parameters W and b
            train_data_obj.update_parameters(grads, learning_rate=0.001)

        if epoch % 10000 == 0:
            print(f"epoch number: {epoch}")
            print(sum_of_cost / number_of_batches)

        cost_axis_y.append(sum_of_cost / number_of_batches)
        cost_axis_x.append(epoch)


main()
