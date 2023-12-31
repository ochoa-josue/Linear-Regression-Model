import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class LinearRegressionModel:
    def __init__(self) -> None:
        self.slope = None
        self.intercept = None

    def _is_valid_input(self, X, y) -> bool:
        if len(X) == len(y):
            return True
        return False
    
    def _convert_to_array(self, X):
        if not isinstance(X, np.ndarray):
            try:
                X = np.array(X, dtype=float)
            except ValueError:
                raise ValueError("Input data could not be converted to a NumPy array")
        return X
    
    def fit(self, X, y) -> None:
        if not self._is_valid_input(X, y):
            raise ValueError("Input variables x_vals and y_vals must have the same number of elements")
        
        N = len(X)

        X_sum = sum(X)
        y_sum = sum(y)
        xy_sum = sum([X_val * y_val for X_val, y_val in zip(X, y)])
        x_sqr_sum = sum([X_val **2 for X_val in X])

        self.slope = (((N * xy_sum) - (X_sum * y_sum))/((N * x_sqr_sum) - (X_sum ** 2)))
        self.intercept = ((y_sum - (self.slope * X_sum))/(N))

    def predict(self, X) -> None:
        return X * self.slope + self.intercept

    def plot(self, X, y, line_style = '--', line_color = 'red', x_label = 'X Values', y_label = 'Y Label', axis_title = 'Linear Regression Fit'):
        plt.scatter(X, y)
        plt.plot(X, self.predict(X), linestyle = line_style, color = line_color)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(axis_title)
        plt.show()

    def score(self, X, y, normalized = True):
        if not self._is_valid_input(X, y):
            raise ValueError("Input variables x_vals and y_vals must have the same number of elements")
        
        y_pred = self.predict(X)
        N = len(X)
        mean_squared_error = np.mean((y - y_pred)**2)
        total_variance = np.var(y)
        
        if normalized:
            return 1 - (mean_squared_error / total_variance)
        
        return mean_squared_error
    