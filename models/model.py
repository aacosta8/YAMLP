# Load libraries
import pandas
from pandas.plotting import scatter_matrix
from sklearn import model_selection
from sklearn import svm
from sklearn import linear_model

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

dataset = pandas.read_csv('clean6001.csv')

array = dataset.values[0:550]
train = dataset.values[0:6000]
X = array[:,3:5]
print (X[0:10])
X_train = train[:,3:5]
Y = array[:,6]
Y_train = train[:,6]

regr = linear_model.LinearRegression()
regr.fit(X, Y)


Y_pred = regr.predict(X)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(Y, Y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(Y, Y_pred))



y_result = regr.predict(X_train)
Xnums = range(len(X_train))
plt.scatter(Xnums, Y_train, color='darkorange', label='data')
plt.plot(Xnums, y_result, color='navy', label='RBF model')
#plt.plot(Xnums, y_lin, color='c', lw=lw, label='Linear model')
plt.xlabel('data')
plt.ylabel('target')
plt.title('Support Vector Regression')
plt.legend()
plt.show()


plt.show()
