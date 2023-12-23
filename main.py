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
    model.plot(X, y)

    return 0

if __name__ == "__main__":
    main()