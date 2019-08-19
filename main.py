from osgeo.gdalconst import GA_ReadOnly

from downloader import downloader
from grabber import data_grabber as dg

url = 'https://nomads.ncdc.noaa.gov/data/gfs4'
ym = '201908'
ymd = '20190801'
data_path = './DATA'
grib_path = "./DATA/gfs_4_20190801_0000_000.grb2"

# downloader.file_downloader(url, data_path, ym, ymd)

dg.grab_grb2_data(grib_path, 1)