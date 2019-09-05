from watcher import watcher
from downloader import downloader
from grabber import data_grabber as dg
from watcher import watcher
from time import gmtime, strftime
import datetime

import cfgrib
import xarray as xr
import subprocess

url = 'https://nomads.ncdc.noaa.gov/data/gfs4'
ym = '201908'
ymd = '20190802'
data_path = './DATA'
grib_path = "./vietnam2.grb2"



# downloader.file_downloader(url, data_path, ym, ymd)

# band_name = ['TMP']
#
# for name in band_name:
#     dg.grab_grb2_data(grib_path, name)

# dg.grab_data(grib_path)

subprocess.run("grib_get_data -p dataDate,dataTime,stepRange,typeOfLevel,shortName vietnam.grb2 > 1.csv", shell=True)