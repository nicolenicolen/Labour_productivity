# Load Packages

# %matplotlib inline
import os,sys,glob
import xarray as xr
import numpy as np
from netCDF4 import Dataset, num2date
import os
import psutil
process = psutil.Process(os.getpid())
import os,sys
import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd

slope = -7.125246314842896

os.chdir('/p/tmp/vmaanen')

WBGTod_files = glob.glob('/p/tmp/vmaanen/new/WBGTod/*')

for WBGTod_file in WBGTod_files:

	WBGTod = xr.open_dataset(WBGTod_file)

	WBGTod = WBGTod['WBGTod']


	Impact = WBGTod.copy() * 0
	Impact.values[WBGTod.values >= 25] = (WBGTod.values[WBGTod.values >= 25] - 25) * slope + 0
	Impact.values[Impact.values <- 100]= -100

	out_file = '/p/tmp/vmaanen/new/Labour_Productivity/outdoor/'+WBGTod_file.split('/')[-1].replace('WBGTod','Impact')
	dataset = xr.Dataset({'Impact': Impact})
	dataset.to_netcdf(out_file)
