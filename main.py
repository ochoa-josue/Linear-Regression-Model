import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from LinearRegressionModel import LinearRegressionModel

#constants:
DATASET = "datasets/Salary_dataset.csv"
HEADER = 0

def main():
    #data preprocessing
    data = pd.read_csv(DATASET, header = HEADER)
    X, y = data['YearsExperience'], data['Salary']

    #data processing
    model = LinearRegressionModel()
    model.fit(X, y)
    print(f'R-squared score: {model.score(X, y)}')
    print(f'Mean-squared-error: {model.score(X, y, normalized=False)}')
    model.plot(X, y, x_label = 'Years of Experience', y_label='Salary')

if __name__ == "__main__":
    main()