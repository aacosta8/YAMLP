import pandas


dataset = pandas.read_csv('6003.csv')
data = dataset.values
for x,y in data:
    date = x.split(' ')[0].split('-')
    time = x.split(' ')[1].split(':')
    total = date  + time + [str(y)]
    myString = ",".join(total)
    print (myString)
