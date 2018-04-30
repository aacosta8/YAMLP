#!/usr/bin/env python3

from subprocess import call
from string import Template
from netCDF4 import Dataset
import glob
import os
import pathlib
import numpy as np

def cropNC(file):
	rootgrp = Dataset(file, "r", format="NETCDF4")
	rad = rootgrp.variables["Rad"]
	result = None
	if rad.shape[0] > 11000:
		result = rad[6484:12486, 10868:16870]
	else:
		result = rad[3241:6242, 5433:8434]
	print(result.shape)
    if type(result) == np.ma.core.MaskedArray:
        rootgrp.close()
        os.system('cp ' + file + './maskedArrayImages')
        os.remove(file)
    else:
        result.astype('int16').tofile(os.path.join("Crops", file))
        rootgrp.close()
        os.remove(file)
	return 1

def main():
	files = glob.glob("*.nc")
	return list(map(cropNC, files))


if __name__ == "__main__":
    main()
