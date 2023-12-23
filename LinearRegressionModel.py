import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class LinearRegressionModel:
    def __init__(self) -> None:
        self.slope = None
        self.intercept = None

    def _is_valid_input(self, x_vals, y_vals) -> bool:
        if len(x_vals) == len(y_vals):
            return True
        return False
    
    def fit(self, x_vals, y_vals) -> None:
        if not self._is_valid_input(x_vals, y_vals):
            raise ValueError("Input variables x_vals and y_vals must have the same number of elements")
        
        N = len(x_vals)

        x_sum = sum(x_vals)
        y_sum = sum(y_vals)
        xy_sum = sum([x_vals*y_vals for x_vals, y_vals in zip(x_vals, y_vals)])
        x_sqr_sum = sum([x_vals**2 for x_vals in x_vals])

        self.slope = (((N * xy_sum) - (x_sum * y_sum))/((N * x_sqr_sum) - (x_sum ** 2)))
        self.intercept = ((y_sum - (self.slope * x_sum))/(N))

    def predict(self, x_vals) -> None:
        return x_vals * self.slope + self.intercept

    def plot(self, x_vals, y_vals, line_style = '--', line_color = 'red', x_label = 'X Values', y_label = 'Y Label', axis_title = 'Linear Regression Fit'):
        plt.scatter(x_vals, y_vals)
        plt.plot(x_vals, self.predict(x_vals), linestyle = line_style, color = line_color)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(axis_title)
        plt.show()

    def score(self, x_vals, y_vals, normalized = True):
        if not self._is_valid_input(x_vals, y_vals):
            raise ValueError("Input variables x_vals and y_vals must have the same number of elements")
        
        y_vals_pred = self.predict(x_vals)
        N = len(x_vals)
        mean_squared_error = np.mean((y_vals - y_vals_pred)**2)
        total_variance = np.var(y_vals)
        
        if normalized:
            return 1 - (mean_squared_error / total_variance)
        
        return mean_squared_error