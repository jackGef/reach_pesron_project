import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/Matan/Downloads/Score.csv/Score.csv")
Y = (df[['Credit_Score']])
df = df.drop(columns=['Payment_of_Min_Amount', 'Credit_Mix', 'Payment_Behaviour', 'Credit_Score'])

Y = np.where(Y != "Poor", Y, 0)
Y = np.where(Y != "Standard", Y, 0.33333)
Y = np.where(Y != "Good", Y, 0.66666)

B = 0
# pd.set_option('display.max_columns', None)
W = np.random.randn(17, 1) * 0.01
X = np.matrix(df[:8000]).T
print("X first index is ", X[0])
print(X.mean())
Z = np.dot(W.T, X) + B
print(Z, "\n")
print("W:", W, W.shape, "end\n\n", "X:", X, X.shape, "end\n\n", "B:", B, "end\n\n")


def sigmoid(Z_func):
    return 1 / (1 + (np.exp(-Z_func)))


A = sigmoid(Z)
print("index 0 is:", A[0][0])
print(np.shape(A))


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

def sigmoid(Z_func):
    A = 1 / (1 + np.exp(Z_func))
    return A
