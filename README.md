# Linear-Regression-Model

## Description

This repository contains my own Python implementation of a linear regression model. This project aims to demonstrate a fundamental understanding of the linear regression algorithm, its mathematical foundations, and practical applications.

## Installation

### Prerequisites

- Python 3.x
- pip

### Setting Up a Virtual Environment and Installing Dependencies

1. **Install Virtualenv**

   If you don't have `virtualenv` installed, open your terminal (Command Prompt on Windows or Terminal on macOS/Linux) and run:

   ```bash
   pip install virtualenv
   ```

   If the pip command is not found on macOS/Linux, and you have Python 3 installed, use:

   ```bash
   pip3 install virtualenv
   ```
   
2. **Clone the Repository**

   First, clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/Linear-Regression-Model.git
   ```

   Navigate to the project directory:

   ```bash
   cd Linear-Regression-Model
   ```
3. **Create a Virtual Environment**

   In the project directory, create a virtual environment:

   ```bash
   virtualenv venv
   ```

   This command creates a new folder `venv` in your project directory, containing the virtual environment.
4. **Activate the Virtual Environment**

   Before installing dependencies, activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

   Your command prompt should change to indicate that the virtual environment is activated.
5. **Install Project Dependencies**

   With the virtual environment activated, install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   or if using macOS/Linux:
      ```bash
   pip3 install -r requirements.txt
   ```

6. **Deactivating the Virtual Environment**

   When you're finished working, you can deactivate the virtual environment:

   ```bash
   deactivate
   ```

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

To evaluate the performance of your model, you can use the `score` method which returns the R² score (coefficient of determination):

```python
r_squared = model.score(X, y)
print("R² Score:", r_squared)
```
