
import time

import numpy as np
import matplotlib.pyplot as plt
import pandas

from sklearn import linear_model
from sklearn import datasets


dataset = pandas.read_csv('clean6001.csv')


array = dataset.values[:2000]
X = array[:,3:5]
y = array[:,6]

model_aic = linear_model.ARDRegression()
model_aic.fit(X, y)

y_aic = model_aic.predict(X)
Y_validation = y
plt.scatter(range(len(X))[0:2000], Y_validation[:2000],  color='orange')
plt.plot(range(len(X))[0:2000], y_aic[:2000], color='red', linewidth=3)


plt.show()
