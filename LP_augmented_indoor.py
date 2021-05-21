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

WBGTid_files = glob.glob('/p/tmp/vmaanen/new/WBGTid/*')

for WBGTid_file in WBGTid_files:

	WBGTid = xr.open_dataset(WBGTid_file)

	WBGTid = WBGTid['WBGTid']


	Impact = WBGTid.copy() * 0
	Impact.values[WBGTid.values >= 25] = (WBGTid.values[WBGTid.values >= 25] - 25) * slope + 0
	Impact.values[Impact.values <- 100]= -100

	out_file = '/p/tmp/vmaanen/new/Labour_Productivity/indoor/'+WBGTid_file.split('/')[-1].replace('WBGTid','Impact')
	dataset = xr.Dataset({'Impact': Impact})
	dataset.to_netcdf(out_file)