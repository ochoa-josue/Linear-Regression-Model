import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from SimpleLinearRegressionModel import SimpleLinearRegressionModel

#constants:
DATASET = "datasets/Salary_dataset.csv"
HEADER = 0

def main():
    #data preprocessing
    data = pd.read_csv(DATASET, header = HEADER)
    X, y = data['YearsExperience'], data['Salary']

    #data processing
    model = SimpleLinearRegressionModel()
    model.fit(X, y)
    r_squared_score = model.score(X, y)
    mean_squared_error = model.score(X, y, normalized=False)
    print(f'R-squared score: {r_squared_score}')
    print(f'Mean-squared-error: {mean_squared_error}')
    model.plot(X, y, x_label = 'Years of Experience', y_label='Salary')

if __name__ == "__main__":
    main()