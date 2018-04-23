
from netCDF4 import Dataset, numpy
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
# from scipy import misc

data = Dataset('images/OR_ABI-L1b-RadF-M3C01_G16_s20180951200403_e20180951211170_c20180951211214.nc')
#print data.variables.keys()
#print data.variables[u'y']
#print data.variables[u'y_image_bounds']
#print data.dimensions
#for dimobj in data.dimensions.values():
#    print dimobj
'''enum_dict = {u'Altocumulus': 7, u'Missing': 255, u'Stratus': 2, u'Clear': 0, u'Nimbostratus': 6, u'Cumulus': 4, u'Altostratus': 5,u'Cumulonimbus': 1, u'Stratocumulus': 3}
cloud_type = data.createEnumType(numpy.uint8,'cloud_t',enum_dict)
print cloud_type
d = data.createDimension('dim',4)
v = data.createVariable('var', np.int, 'dim')
v[np.rank] = np.rank
data.close()'''


'''g16nc = Dataset('ABI-L1b-RadF%2F2018%2F001%2F01%2FOR_ABI-L1b-RadF-M3C01_G16_s20180010130387_e20180010141154_c20180010141200.nc', 'r')
radiance = g16nc.variables['Rad'][:]
g16nc.close()
g16nc = None

fig = plt.figure(figsize=(6,6),dpi=200)
im = plt.imshow(radiance,vmin=9478,vmax=10417,cmap='Greys_r')
cb = fig.colorbar(im, orientation='horizontal')
cb.set_ticks([1, 100, 200, 300, 400, 500, 600])
cb.set_label('Radiance (W m-2 sr-1 um-1)')
plt.show()'''
radiance = data.variables['Rad'][4735-200:4735+200,4735-200:4735+200]
print len(data.variables['Rad'][10717-2:10717+2,9478-2:9478+2])
im = plt.imshow(radiance)
plt.show()
