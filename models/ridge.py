
import numpy as np
import matplotlib.pyplot as plt
import pandas


import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
from sklearn import linear_model



dataset = pandas.read_csv('clean6001.csv')


array = dataset.values
X = array[:,0:6]
y = array[:,6]

reg = linear_model.SGDRegressor()
reg.fit(X,y)
y_pred = reg.predict(X)

lw=2
Xnums = range(len(X))
plt.scatter(Xnums, y_pred, color='navy', label='RBF model')
plt.xlabel('data')
plt.ylabel('target')
plt.title('Ridge')
plt.legend()
plt.show()
