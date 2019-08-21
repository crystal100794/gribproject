from osgeo.gdalconst import GA_ReadOnly
from watcher import watcher
from downloader import downloader
from grabber import data_grabber as dg
from watcher import watcher
from time import gmtime, strftime
import datetime


url = 'https://nomads.ncdc.noaa.gov/data/gfs4'
ym = '201908'
ymd = '20190802'
data_path = './DATA'
grib_path = "./DATA/gfs_4_20190801_0000_000.grb2"

now = datetime.datetime.now()
current_time = now.strftime("%H:%M")
set_time =  "11:41"

downloader.file_downloader(url, data_path, ym, ymd, current_time, set_time)

dg.grab_grb2_data(grib_path, 1)

