import pandas

dataset1 = pandas.read_csv('clean6001.csv')
data1 = dataset1.values

dataset2 = pandas.read_csv('clean6002.csv')
data2 = dataset2.values

dataset3 = pandas.read_csv('clean6003.csv')
data3 = dataset3.values

for arr in (data1):
    myString = ",".join(arr)
    print (myString)
