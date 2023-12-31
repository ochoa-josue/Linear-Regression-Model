# Simple-Linear-Regression-Model

## Description

This repository contains my implementation of a simple linear regression model, inspired by the design and approach of SKLearn's linear regression functionality. This project aims to demonstrate a fundamental understanding of the linear regression algorithm, its mathematical foundations, and practical applications.

## Installation

### Prerequisites

- Python 3.x

### Optional: Virtual Environment Setup

Using a Python virtual environment is recommended for managing dependencies without affecting your global Python installation. 

For guidance on setting up a Python virtual environment, refer to the following introductory tutorial:

- [Python Virtual Environment Tutorial](https://github.com/ochoa-josue/python-venv-guide)
  - Description: A step-by-step beginner guide to setting up Python virtual environments using `virtualenv` and `venv`.

## Usage

### Importing the Model

First, ensure that the `LinearRegressionModel.py` file is in your project directory. You can import the model into your Python script as follows:

```python
from LinearRegressionModel import LinearRegressionModel
```

### Preparing Your Data

Your data should be in the form of two lists or NumPy arrays: one for the independent variable (X) and one for the dependent variable (y). Here's an example of preparing a simple dataset:

```python
import numpy as np

# Example Data
X = np.array([1, 2, 3, 4, 5])  # Independent variable (e.g., years of experience)
y = np.array([2, 4, 6, 8, 10]) # Dependent variable (e.g., salary)
```

### Fitting the Model

Instantiate the `LinearRegressionModel` and fit it to your data:

```python
model = LinearRegressionModel()
model.fit(X, y)
```

### Making Predictions

Once the model is fitted, you can use it to make predictions:

```python
predicted_values = model.predict(X)
print(predicted_values)
```

### Plotting the Results

To visualize the linear regression line along with the data points:

```python
model.plot(X, y, line_style='--', line_color='red', x_label='Years of Experience', y_label='Salary', axis_title='Linear Regression Fit')
```

### Evaluating the Model

To evaluate the performance of your model, you can use the `score` method which returns the R² score (coefficient of determination) by default:

```python
r_squared = model.score(X, y)
print("R² Score:", r_squared)

#For mean-squared-error
mse = model.score(X, y, normalized=False)
print("R² Score:", mse)
```
## Resources

- [Kaggle Dataset: Salary Dataset](https://www.kaggle.com/datasets/abhishek14398/salary-dataset-simple-linear-regression/code)
  - Description: This dataset was used for model training and testing. It contains salary data for simple linear regression.
  
- [Math Is Fun: Least Squares Regression](https://www.mathsisfun.com/data/least-squares-regression.html)
  - Description: This resource provides an explanation of least squares regression, along with a relevant formula to calculate mean-squared-error
  
- [Wikipedia: Coefficient of Determination](https://en.wikipedia.org/wiki/Coefficient_of_determination)
  - Description: Wikipedia page explaining the coefficient of determination R<sup>2</sup>, used in regression analysis, along with a relevant formula used in calculating R<sup>2</sup> score
