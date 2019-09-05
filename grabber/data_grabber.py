from osgeo import gdal
import numpy as np
import json

def grab_grb2_data(path, band_name):
    # Open gdal data
    data_set = gdal.Open(path, gdal.GA_ReadOnly)

    # Read data size
    width = data_set.RasterXSize
    height = data_set.RasterYSize
    print("Data size", width, height)

    # Geo transform
    geo_transform = data_set.GetGeoTransform()
    arr_list = []
    # Get data band
    for band in range(data_set.RasterCount):
        band += 1
        band_data = data_set.GetRasterBand(band)

        meta_data = band_data.GetMetadata()
        print(str(meta_data))

def grab_data(path):
    data_set = gdal.Open(path, gdal.GA_ReadOnly)
    print(data_set.GetMetadata())


