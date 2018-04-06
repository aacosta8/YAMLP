from netCDF4 import Dataset
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#Open image as a Dataset and take the variables to graph
g16nc = Dataset('images/OR_ABI-L1b-RadF-M3C01_G16_s20180951200403_e20180951211170_c20180951211214.nc', 'r')
radiance = g16nc.variables['Rad'][:]
g16nc.close()
g16nc = None

#Show image

im = plt.imshow(radiance)

plt.show() #Remove comment to see the image
