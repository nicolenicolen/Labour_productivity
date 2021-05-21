import xarray as xr
import os,sys,glob
import numpy as np
import pandas as pd
import os
import psutil
process = psutil.Process(os.getpid())

# Directive on PIK Cluster + example dataset 

os.chdir('/p/tmp/vmaanen/new/Labour_Productivity/GCM_summary_warming/indoor/')

example_nc = xr.open_dataset('Impact_GFDL-ESM2M_rcp85_r1i1p1_EWEMBI_landonly.nc4')


models = ['GFDL-ESM2M', 'IPSL-CM5A-LR','HadGEM2-ES','MIROC5']
impacts = ['Impact']
coordinates = dict(lat=example_nc.lat, lon=example_nc.lon, model=models, impact=impacts)
data = xr.DataArray(data = np.zeros([len(impacts),len(models),len(example_nc.lat),len(example_nc.lon)])*np.nan,
                    coords = coordinates,
                    dims = ['impact','model','lat','lon'])

#print(coordinates)
#print(data)

for impact in impacts:
        for model in models:

            print(xr.open_dataset(impact+'_'+model+'_rcp85_r1i1p1_EWEMBI_landonly.nc4'))
            data.loc[impact,model,:,:] = xr.open_dataset(impact+'_'+model+'_rcp85_r1i1p1_EWEMBI_landonly.nc4')['Impact_3_0'] 

xr.Dataset({'Impact_3_0':data}).to_netcdf('/p/tmp/vmaanen/new/Labour_Productivity/Summary_warming/indoor/Impact_3_0_LP_all_GCMs_warming.nc4')


# mean over models:
#data.mean(dim='model').mean(dim='impact').loc[1.5]