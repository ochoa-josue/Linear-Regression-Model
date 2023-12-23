import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class LinearRegressionModel:
    def __init__(self) -> None:
        self.slope = None
        self.intercept = None

    def fit(self, x_vals, y_vals) -> None:
        if len(x_vals) != len(y_vals):
            return -1
        
        N = len(x_vals)

        x_sum = sum(x_vals)
        y_sum = sum(y_vals)
        xy_sum = sum([x*y for x, y in zip(x_vals, y_vals)])
        x_sqr_sum = sum([x**2 for x in x_vals])

        self.slope = (((N * xy_sum) - (x_sum * y_sum))/((N * x_sqr_sum) - (x_sum ** 2)))
        self.intercept = ((y_sum - (self.slope * x_sum))/(N))

    def predict(self, X) -> None:
        return X * self.slope + self.intercept

    def plot(self, X, y):
        plt.scatter(X, y)
        plt.plot(X, self.predict(X), linestyle = '--', color = 'red')
        plt.xlabel = ('X')
        plt.ylabel = ('Y')
        plt.title('Linear Regression Fit')
        plt.show()