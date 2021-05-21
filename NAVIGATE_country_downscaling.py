# Load packages

import os,sys,glob
import xarray as xr
import numpy as np
from netCDF4 import Dataset, num2date
import os
import psutil
import os,sys,glob
import pandas as pd

#os.chdir('/p/tmp/vmaanen/')

all_files = glob.glob('/p/tmp/vmaanen/new/NAVIGATE/indoor/annual_projections/relative/Impact*')

for Impact_file in all_files:

	Impact = xr.open_dataset(Impact_file)

	Impact = Impact['Impact']

	country_mask = xr.open_dataset('/p/tmp/vmaanen/Data/mask_countries_lat-weighted_720x360.nc')

	countries = sorted([u'AGO',u'DZA',u'EGY',u'BGD',u'NER',u'LIE',u'NAM',u'BGR',u'BOL',u'GHA',u'PAK',u'CPV',u'JOR',u'LBR',u'LBY',u'MYS',u'DOM',u'PRI',u'SXM',u'PRK',u'PSE',u'TZA',u'BWA',u'KHM',u'NIC',u'TTO',u'ETH',u'PRY',u'HKG',u'SAU',u'LBN',u'SVN',u'BFA',u'CHE',u'MRT',u'HRV',u'CHL',u'CHN',u'KNA',u'SLE',u'JAM',u'SMR',u'DJI',u'GIN',u'FIN',u'URY',u'THA',u'STP',u'SYC',u'NPL',u'LAO',u'YEM',u'PHL',u'ZAF',u'KIR',u'ROU',u'VIR',u'SYR',u'MAC',u'MAF',u'MLT',u'KAZ',u'TCA',u'PYF',u'NIU',u'DMA',u'BEN',u'NGA',u'BEL',u'MSR',u'TGO',u'DEU',u'GUM',u'LKA',u'SSD',u'FLK',u'GBR',u'GUY',u'CRI',u'CMR',u'MAR',u'MNP',u'LSO',u'HUN',u'TKM',u'SUR',u'NLD',u'BMU',u'TCD',u'GEO',u'MNE',u'MNG',u'MHL',u'BLZ',u'NFK',u'MMR',u'AFG',u'BDI',u'VGB',u'BLR',u'BLM',u'GRD',u'GRC',u'RUS',u'GRL',u'SHN',u'AND',u'MOZ',u'TJK',u'HTI',u'MEX',u'ZWE',u'LCA',u'IND',u'LVA',u'BTN',u'VCT',u'VNM',u'NOR',u'CZE',u'ATG',u'FJI',u'HND',u'MUS',u'LUX',u'ISR',u'FSM',u'PER',u'IDN',u'VUT',u'MKD',u'COD',u'COG',u'ISL',u'COK',u'COM',u'COL',u'TLS',u'TWN',u'PRT',u'MDA',u'GGY',u'MDG',u'ECU',u'SEN',u'ESH',u'MDV',u'ASM',u'SPM',u'CUW',u'FRA',u'LTU',u'RWA',u'ZMB',u'GMB',u'WLF',u'JEY',u'FRO',u'GTM',u'DNK',u'IMN',u'AUS',u'AUT',u'VEN',u'PLW',u'KEN',u'WSM',u'TUR',u'ALB',u'OMN',u'ALA',u'BRN',u'TUN',u'PCN',u'BRB',u'BRA',u'CIV',u'SRB',u'GNQ',u'USA',u'QAT',u'SWE',u'AZE',u'GNB',u'SWZ',u'TON',u'CAN',u'UKR',u'KOR',u'AIA',u'CAF',u'SVK',u'CYP',u'BIH',u'SGP',u'SOM',u'UZB',u'ERI',u'POL',u'KWT',u'GAB',u'CYM',u'VAT',u'EST',u'MWI',u'ESP',u'IRQ',u'SLV',u'MLI',u'IRL',u'IRN',u'ABW',u'PNG',u'PAN',u'SDN',u'SLB',u'NZL',u'MCO',u'ITA',u'JPN',u'KGZ',u'UGA',u'NCL',u'ARE',u'ARG',u'BHS',u'BHR',u'ARM',u'NRU',u'CUB'])

	output = pd.DataFrame(columns = ['country','impact'])
	output['country'] = countries

	for country_name in countries:

		mask = country_mask[country_name]

		output.loc[(output.country == country_name), 'impact'] = np.nansum(Impact * mask, axis=(0,1))

	output.to_csv('/p/tmp/vmaanen/new/NAVIGATE/indoor/annual_projections/relative/country_level/'+Impact_file.split('/')[-1].replace('Impact','Impact_country').replace('.nc4','.csv'))

