# Load packages 

import os,sys,glob
import xarray as xr
import numpy as np
from netCDF4 import Dataset, num2date
import os
import psutil
process = psutil.Process(os.getpid())
print(process.memory_info().rss)

# Directive 

os.chdir('/p/projects/isimip/isimip/ISIMIP2b/InputData/GCM_atmosphere/biascorrected/landonly/')

# Variables needed  

models = sorted([u'GFDL-ESM2M', u'IPSL-CM5A-LR', u'HadGEM2-ES', u'MIROC5'])
scenarios =  sorted([u'historical', u'rcp26', u'rcp60', u'rcp85'])

# Out data, file names, models 
for scenario in scenarios:
	for model in models:
		tasmax_files = glob.glob('/p/projects/isimip/isimip/ISIMIP2b/InputData/GCM_atmosphere/biascorrected/landonly/' + scenario + '/' + model + '/tasmax*')
		#hurs_files = glob.glob('/p/projects/isimip/isimip/ISIMIP2b/InputData/GCM_atmosphere/biascorrected/landonly/' + scenario + '/' + model + '/hurs*')

		for tasmax_file in tasmax_files:
			hurs_file = tasmax_file.replace('tasmax','hurs')

			#print(tasmax_file)
			#print(hurs_file) 

			hurs = xr.open_dataset(hurs_file)
			tasmax = xr.open_dataset(tasmax_file)

			tasmax = tasmax['tasmax'] - 273.15
			hurs = hurs['hurs']

			#print(tasmax)
			#print(hurs)

			### Calculate and save Tw 

			Tw = tasmax * np.arctan(0.151977*(hurs + 8.313659)**(1/2)) + np.arctan(tasmax + hurs)\
        	- np.arctan(hurs - 1.676331) + 0.00391838*((hurs)**(3/2) * np.arctan(0.023101 * hurs)) - 4.686035

			out_file = '/p/tmp/vmaanen/new/Tw/'+tasmax_file.split('/')[-1].replace('tasmax','TW')
			#print(out_file)
			dataset = xr.Dataset({'Tw': Tw})
			dataset.to_netcdf(out_file)

			### Calculate and save WBGTid

			WBGTid = 0.67 * Tw + 0.33 * tasmax

			out_file = '/p/tmp/vmaanen/new/WBGTid/'+tasmax_file.split('/')[-1].replace('tasmax','WBGTid')
			#print(out_file)
			dataset = xr.Dataset({'WBGTid': WBGTid})
			dataset.to_netcdf(out_file)

			### Calculate and save WBGTod 

			WBGTod = WBGTid + 3

			out_file = '/p/tmp/vmaanen/new/WBGTod/'+tasmax_file.split('/')[-1].replace('tasmax','WBGTod')
			#print(out_file)
			dataset = xr.Dataset({'WBGTod': WBGTod})
			dataset.to_netcdf(out_file)

	