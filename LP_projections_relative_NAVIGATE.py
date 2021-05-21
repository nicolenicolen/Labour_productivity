# Load Packages

import os,sys,glob
import xarray as xr
import numpy as np
from netCDF4 import Dataset, num2date
import os
import psutil
process = psutil.Process(os.getpid()) 

os.chdir('/p/tmp/vmaanen')


#models = sorted([u'GFDL-ESM2M', u'IPSL-CM5A-LR', u'HadGEM2-ES', u'MIROC5'])
models = sorted([u'IPSL-CM5A-LR'])
scenarios =  sorted([u'rcp26', u'rcp60'])
#scenarios =  sorted([u'rcp26'])
impacts = sorted([u'Impact'])

years = np.arange(2006,2100,1)

for scenario in scenarios:
	for model in models:
		for impact in impacts:
			for year in years:

				nc_impact = xr.open_dataset('/p/tmp/vmaanen/new/NAVIGATE/indoor/annual_projections/Impact_' + model + '_' + scenario + '_' + str(year) + '_r1i1p1_EWEMBI_landonly_id.nc4')

				#nc_impact = xr.open_mfdataset("/p/tmp/vmaanen/new/NAVIGATE/indoor/annual_projections/Impact_" + model + "_" + scenario + "_" + str(year) + "_r1i1p1_EWEMBI_landonly_id.nc4")
				Impact = nc_impact['Impact']

				nc_historical = xr.open_dataset("/p/tmp/vmaanen/new/Labour_Productivity/GCM_summary_historical/indoor/Impact_" + model + "_historical_r1i1p1_EWEMBI_landonly.nc4")
				Impact_historical = nc_historical['Impact_historical']

				dataset = xr.Dataset({})

				dataset['Impact'] = Impact - Impact_historical

				out_file = '/p/tmp/vmaanen/new/NAVIGATE/indoor/annual_projections/relative/' + impact + '_' + model + '_' + scenario + '_' + str(year) + '_r1i1p1_EWEMBI_landonly_id.nc4'
				dataset.to_netcdf(out_file)

