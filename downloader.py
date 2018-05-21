from subprocess import call
from string import Template
from netCDF4 import Dataset
import glob
import os
import pathlib
import numpy as np

def downloadFolder(year, day, hour, directory):
	str = Template("s3://noaa-goes16/ABI-L1b-RadF/$year/$day/$hour")
	call(
		'aws s3 cp ' + str.substitute(day=day,hour=hour,year=year) + ' . --no-sign-request --endpoint-url https://osdc.rcc.uchicago.edu --no-verify-ssl --recursive --exclude "*" --include "*M3C0[123]?*"' 
		, cwd = directory)
	files = glob.glob("*.nc")
	return list(map(cropNC, files))

def cropNC(file):
	rootgrp = Dataset(file, "r", format="NETCDF4")
	rad = rootgrp.variables["Rad"]
	result = None
	if rad.shape[0] > 11000:
		result = rad[6484:12486, 10868:16870]
	else:
		result = rad[3241:6242, 5433:8434]
	print(result.shape)
	result.astype('int16').tofile(os.path.join("Crops", file))
	rootgrp.close()
	os.remove(file)
	return 1

def main():
	pathlib.Path('Crops').mkdir(exist_ok=True) 
	for day in range(213, 301):
		for hour in range(11, 24):
			downloadFolder(2017, day, hour, os.getcwd())

if __name__ == "__main__":
    main()