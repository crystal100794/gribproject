from osgeo import gdal
import numpy as np

def grab_grb2_data(path, band_no):
    # Open gdal data
    data_set = gdal.Open(path, gdal.GA_ReadOnly)
    total_bands = data_set.RasterCount
    print("Number of bands:", total_bands)

    band = data_set.GetRasterBand(band_no)
    data_array = band.ReadAsArray()

    arr_list = []

    for row in data_array:
        for value in row:
            arr_list.append(value)

    print('Band:', str(band_no))
    print('Band Max', str(np.max(arr_list)))
    print('Band Min', str(np.min(arr_list)))
    print('Count:', str(len(arr_list)))