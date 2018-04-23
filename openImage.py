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
<<<<<<< HEAD

im = plt.imshow(radiance)

plt.show() #Remove comment to see the image
=======
fig = plt.figure(figsize=(6,6),dpi=200)
im = plt.imshow(radiance, cmap='Greys_r')
cb = fig.colorbar(im, orientation='horizontal')
cb.set_ticks([1, 100, 200, 300, 400, 500, 600])
cb.set_label('Radiance (W m-2 sr-1 um-1)')
# plt.show() #Remove comment to see the image

#Traer informacion del formato nc
print g16nc.variables.keys()
print g16nc.variables[u'y']
print g16nc.variables[u'y_image_bounds']
>>>>>>> db5eac7c6fe2d658968f33b15139b080e29c2395
