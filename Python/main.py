import math
import sys
import pandas as pd
import numpy as np


def sigmoid(Z_func):
    return 1 / (1 + (np.exp(-Z_func)))


# receiving data
df = pd.read_csv("C:/Users/Matan/Downloads/Score.csv/Score.csv")
Y = (df[['Credit_Score']])
df = df.drop(columns=['Payment_of_Min_Amount', 'Credit_Mix', 'Payment_Behaviour', 'Credit_Score'])
np.set_printoptions(threshold=sys.maxsize)

# normalization
Y = np.where(Y != "Poor", Y, 0)
Y = np.where(Y != "Standard", Y, 0.33333)
Y = np.where(Y != "Good", Y, 0.66666)

# Vector creation and initialization
B = 0
W = np.random.randn(17, 1) * 0.01
X = np.matrix(df.iloc[:8000]).T
x = pd.DataFrame(X.T)
Z = np.dot(W.T, x.T) + B

print("the data is: \n", x)

# forward propagation
A = sigmoid(Z)
print("Z vector is : \n", Z)
print("A vector is : \n", A)
print(type(Z))
dZ = A - Y
# print("A is", A)
# print("Y is", Y)
print("dZ type is ", type(dZ))
print("dZ is", dZ)
print("END")

# def data_collect():
#     df = pd.read_csv("C:/Users/Matan/Downloads/Score.csv/Score.csv")
#
# def normalization():
#     df = df.drop(columns=['Payment_of_Min_Amount', 'Credit_Mix', 'Payment_Behaviour', 'Credit_Score'])
#     Y = np.where(Y != "Poor", Y, 0)
#     Y = np.where(Y != "Standard", Y, 0.33333)
#     Y = np.where(Y != "Good", Y, 0.66666)
#
# def initialization():
#     B = 0
#     W = np.random.randn(17, 1)
#     X = np.matrix(df[:8000]).T
#     Z = np.dot(W.T, X) + B
# print(Z, "\n")
# print("W:", W, W.shape, "end\n\n", "X:", X, X.shape, "end\n\n", "B:", B, "end\n\n")
