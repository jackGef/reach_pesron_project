import numpy as np


class LogisticRegression:

    def __init__(self, lr=0.001, n_iters=1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        # init paramaters
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        loss = []

        # gradient descent
        for _ in range(self.n_iters):
            linear_module = np.dot(X, self.weights) + self.bias
            y_predicted = self._sigmoid(linear_module)

            loss.push(1 / n_samples * np.dot(y * np.log(y_predicted) + (1 - y) * (1 - np.log(y_predicted)))) 

            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)

            self.weights -= self.lr * dw
            self.bias -= self.lr * db
        
        return loss

    def predict(self, X):
        linear_module = np.dot(X, self.weights) + self.bias
        y_predicted = self._sigmoid(linear_module)
        y_predicted_cls = [1 if i > 0.5 else 0 for i in y_predicted]
        return y_predicted_cls

    def _sigmoid(self, x):
        x = np.clip(x, -500, 500)
        return 1 / (1 + np.exp(-x))
