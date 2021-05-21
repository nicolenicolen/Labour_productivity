# Load Packages

import os,sys,glob
import xarray as xr
import numpy as np
import pandas as pd
import os
import psutil
process = psutil.Process(os.getpid())

# Directive on PIK Cluster

os.chdir('/p/tmp/vmaanen')

# Varbiables

models = sorted([u'GFDL-ESM2M', u'IPSL-CM5A-LR', u'HadGEM2-ES', u'MIROC5'])
#scenarios =  sorted([u'rcp85'])
scenarios =  sorted([u'historical'])
impacts = sorted([u'Impact'])

for scenario in scenarios:
	for model in models:
		for impact in impacts:

			nc_impact = xr.open_mfdataset("/p/tmp/vmaanen/new/Labour_Productivity/outdoor/Impact_day_" + model + "_" + scenario + "_r1i1p1_EWEMBI_landonly_*.nc4", concat_dim='time')
			Impact = nc_impact['Impact']

			dataset = xr.Dataset({})

			Impact_historical = Impact.loc[np.datetime64('1986-01-01'):np.datetime64('2005-12-31')]
			dataset['Impact_historical'] = Impact_historical.mean(dim = 'time')

			#Impact_1_5 = Impact.loc[np.datetime64('2015-01-01'):np.datetime64('2035-12-31')]
			#dataset['Impact_1_5'] = Impact_1_5.mean(dim = 'time')
			#dataset['Impact_2041_2060_median'] = Impact_2041_2060.median(dim = 'time')

			#Impact_2_0 = Impact.loc[np.datetime64('2027-01-01'):np.datetime64('2047-12-31')]
			#dataset['Impact_2_0'] = Impact_2_0.mean(dim = 'time')
			#dataset['Impact_2061_2080_median'] = Impact_2061_2080.median(dim = 'time')

			#Impact_3_0 = Impact.loc[np.datetime64('2046-01-01'):np.datetime64('2066-12-31')]
			#dataset['Impact_3_0'] = Impact_3_0.mean(dim = 'time')
			#dataset['Impact_2081_2100_median'] = Impact_2081_2100.median(dim = 'time')

			# Save data

			out_file = '/p/tmp/vmaanen/new/Labour_Productivity/GCM_summary_historical/outdoor/' + impact + '_' + model + '_' + scenario + '_r1i1p1_EWEMBI_landonly.nc4'

			dataset.to_netcdf(out_file)