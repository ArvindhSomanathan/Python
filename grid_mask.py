import numpy as np
from matplotlib import pyplot as plt
from netCDF4 import Dataset as dt

dataset = dt('met_era_karnataka_2014_2015.nc', 'r')
lon = np.array(dataset['longitude'])
lat = np.array(dataset['latitude'])
zvar = np.array(dataset['skt'])

# DEFINE YOUR DOMAIN
lat1 = 14
lat2 = 15
lon1 = 75
lon2 = 76

if lat1 > lat2 or lat1 < lat.min() or lat2 > lat.max():
    print "INVALID DOMAIN"

a1 = np.where(lat >= lat1)[0][-1]+1
a2 = np.where(lat >= lat2)[0][-1]-1
lat11 = lat[a2:a1+1]
a1 = np.where(lon >= lon1)[0][0]-1
a2 = np.where(lon >= lon2)[0][0]+1
lon11 = lon[a1:a2+1]
