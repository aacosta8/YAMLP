
import time

import numpy as np
import matplotlib.pyplot as plt
import pandas


import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt


dataset = pandas.read_csv('clean6001.csv')


array = dataset.values[0:1500]
train = dataset.values[0:4000]
X = array[:,0:5]
X_train = train[:,0:5]
y = array[:,6]
Y_train = train[:,6]

# #############################################################################
# Fit regression model
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svr_lin = SVR(kernel='linear', C=1e3)
svr_poly = SVR(kernel='poly', C=1e3, degree=2)
y_rbf = svr_rbf.fit(X, y).predict(X_train)
y_lin = svr_lin.fit(X, y).predict(X_train)
y_poly = svr_poly.fit(X, y).predict(X_train)

# #############################################################################
# Look at the results
lw = 2
Xnums = range(len(X_train))
plt.scatter(Xnums, Y_train, color='darkorange', label='data')
plt.plot(Xnums, y_rbf, color='navy', lw=lw, label='RBF model')
plt.plot(Xnums, y_lin, color='black', lw=lw, label='Linear model')
#plt.plot(Xnums, y_poly, color='red', lw=lw, label='poly model')
plt.xlabel('data')
plt.ylabel('target')
plt.title('Support Vector Regression')
plt.legend()
plt.show()
