import numpy as np


def adamOptimizer():
    learning_rate = 0.001
    epsilon = 0

    vdW = 0
    sdW = 0
    dW1 = 0
    dw2 = 0

    vdb = 0
    sdb = 0
    db1 = 0
    db2 = 0

    b1 = 0, b2 = 0

    # Momentum
    vdW = b1 * vdW + (1 - b1) * dW1
    vdb = b1 * vdb + (1 - b1) * db1

    # RMSprop
    sdW = b2 * sdW + (1 - b2) * dw2
    sdb = b2 * sdb + (1 - b2) * db2

    vdWc = vdW / (1 - b1)
    vdbc = vdb / (1 / b1)

    sdWc = sdW / (1 - b2)
    sdbc = sdb / (1 - b2)

    # Update parameters
    W = W - learning_rate * (vdWc / np.sqrt(sdWc) + epsilon)
    b = b - learning_rate * (vdbc / np.sqrt(sdbc) + epsilon)


def learning_rate_decay():
    learning_rate = 0.001
    decay_rate = 0
    epoch_number = 0

    learning_rate = 1 / (1 + decay_rate * epoch_number) * learning_rate * 0 # 0 Means a variable(I think)


def regularization():
    learning_rate = 0.001
    dW = 0
    lambd = 0
    m = 0 # Number of training examples

    W = W - learning_rate * dW + lambd / m * W

def normalizing():
    m = 0 # Number of training examples

    mean = 1 / m * np.sum(X)
    X = X - m


    al = 1 / m * np.sum(X ** 2) # Normalizing variance



    # Another normalizing
    X = X - np.min(X) / np.max(X) - np.min(X)