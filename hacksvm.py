# -*- coding: utf-8 -*-
"""hacksvm.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1haNoEjonq6ycdxrvjtAz5hjg5eh4HdBP
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.svm import SVR
import sklearn.metrics as metrics

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder

df=pd.read_csv('/content/aakash data - malaria.csv')
df

data = df
print(data.columns)
# Separate features and target variable
X = data.iloc[:, [1,3,4,5,6]]
y =np.array( [data['cases'].copy()])

# Define numeric and categorical columns
numeric_cols = ["rainfall in mm", "temprature", "avg relative humidity"]
categorical_cols = ["state", "mosquito"]

# Scale numeric columns
scaler = StandardScaler()
X[numeric_cols] = scaler.fit_transform(X[numeric_cols])
y=y.T
y=scaler.fit_transform(y)


# One-hot encode categorical columns
encoder = OneHotEncoder(sparse_output=False, drop=None)  # Change drop parameter
encoded_cols = encoder.fit_transform(data[categorical_cols])
encoded_df = pd.DataFrame(encoded_cols, columns=encoder.get_feature_names_out())

print(X.columns,categorical_cols)

# Replace original categorical columns with encoded columns
X.drop(columns=categorical_cols, inplace=True)
X = pd.concat([X, encoded_df], axis=1)
X.drop(columns='mosquito_anopheles', inplace=True)

# Split data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

x_train

y_train

svr=SVR(kernel='rbf')

svr.fit(x_train, y_train)

result=svr.predict(x_test)
  mae = metrics.mean_absolute_error(y_test, result)
  mse = metrics.mean_squared_error(y_test, result)
  rmse = np.sqrt(mse)
  r2 = metrics.r2_score(y_test, result)
  print("Results of sklearn.metrics:")
  print("MAE:",mae)
  print("MSE:", mse)
  print("RMSE:", rmse)
  print("R-Squared:", r2)
  z=np.linspace(0,50,20)
  plt.scatter(z,y_test[20:40])
  plt.scatter(z,result[20:40],c='red')
  plt.show()

result

from sklearn.neighbors import KNeighborsRegressor
neigh = KNeighborsRegressor(n_neighbors=7)
neigh.fit(x_train,y_train)

result=neigh.predict(x_test)

mse = metrics.mean_squared_error(y_test, result)
  rmse = np.sqrt(mse)
  r2 = metrics.r2_score(y_test, result)
  print("Results of sklearn.metrics:")
  print("MAE:",mae)
  print("MSE:", mse)
  print("RMSE:", rmse)
  print("R-Squared:", r2)
  z=np.linspace(0,50,20)
  plt.scatter(z,y_test[20:40])
  plt.scatter(z,result[20:40],c='red')
  plt.show()

from sklearn.ensemble import RandomForestRegressor
regr = RandomForestRegressor(max_depth=3, random_state=60)
regr.fit(x_train,y_train)

result=regr.predict(x_test)

mse = metrics.mean_squared_error(y_test, result)
  rmse = np.sqrt(mse)
  r2 = metrics.r2_score(y_test, result)
  print("Results of sklearn.metrics:")
  print("MAE:",mae)
  print("MSE:", mse)
  print("RMSE:", rmse)
  print("R-Squared:", r2)
  z=np.linspace(0,50,20)
  plt.scatter(z,y_test[20:40])
  plt.scatter(z,result[20:40],c='red')
  plt.show()

