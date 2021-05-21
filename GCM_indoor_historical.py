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

			nc_impact = xr.open_mfdataset("/p/tmp/vmaanen/new/Labour_Productivity/indoor/Impact_day_" + model + "_" + scenario + "_r1i1p1_EWEMBI_landonly_*.nc4", concat_dim='time')
			Impact = nc_impact['Impact']

			dataset = xr.Dataset({})

			Impact_historical_Q1 = Impact.loc[np.datetime64('1986-01-01'):np.datetime64('2005-03-31')]
			dataset['Impact_historical_Q1'] = Impact_historical_Q1.mean(dim = 'time')

			Impact_historical_Q2 = Impact.loc[np.datetime64('1986-04-01'):np.datetime64('2005-06-30')]
			dataset['Impact_historical_Q2'] = Impact_historical_Q2.mean(dim = 'time')

			Impact_historical_Q3 = Impact.loc[np.datetime64('1986-07-01'):np.datetime64('2005-09-30')]
			dataset['Impact_historical_Q3'] = Impact_historical_Q3.mean(dim = 'time')

			Impact_historical_Q4 = Impact.loc[np.datetime64('1986-10-01'):np.datetime64('2005-12-31')]
			dataset['Impact_historical_Q4'] = Impact_historical_Q4.mean(dim = 'time')

			# Save data

			out_file = '/p/tmp/vmaanen/new/NiGEM/historical/' + impact + '_' + model + '_' + scenario + '_r1i1p1_EWEMBI_landonly_id.nc4'

			dataset.to_netcdf(out_file)