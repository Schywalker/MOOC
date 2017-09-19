# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import Imputer

# Importing the dataset
dataset = pd.read_csv("Data.csv")

#Independent variables
#first ":" means take all rows, second ":-1" take all columns except for the last columns
X = dataset.iloc[:, : -1].values
y = dataset.iloc[:, len(dataset.columns) -1]

#Taking Care of missing data
# imputer = Imputer(missing_values = "NaN", strategy="mean", axis=0)
# imputer = imputer.fit(X[:, 1:3])
# X[:,1:3] = imputer.transform(X[:,1:3])

# imputer = Imputer(missing_values = "NaN", strategy="median", axis=0)
# imputer = imputer.fit(X[:, 1:3])
# X[:,1:3] = imputer.transform(X[:,1:3])

imputer = Imputer(missing_values = "NaN", strategy="most_frequent", axis=0)
imputer = imputer.fit(X[:, 1:3])
X[:,1:3] = imputer.transform(X[:,1:3])

print(X)