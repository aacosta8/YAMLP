
import time

import numpy as np
import matplotlib.pyplot as plt
import pandas


import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt


dataset = pandas.read_csv('clean6001.csv')


array = dataset.values[0:3000]
train = dataset.values[0:3000]
X = array[:,3:5]
X_train = train[:,3:5]
y = array[:,6]
Y_train = train[:,6]
