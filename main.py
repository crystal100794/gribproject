from watcher import watcher
import os, requests
import datetime as dt
from lxml import html
from downloader import downloader as dl
from grabber import converter as cvt
from utils import utils
from netCDF4 import Dataset

conda_env_name = 'grb2'
url = 'https://nomads.ncdc.noaa.gov/data/gfs4/'
data_dir = './DATA/'

def convert_data():
    print('### STARTING APP ###')
    day_step = 10

    for d in range(day_step + 1):
        date_time = dt.datetime.now() - dt.timedelta(days=day_step) + dt.timedelta(d)
        year = str(date_time.year)
        month = str('%02d' % date_time.month)
        day = str('%02d' % date_time.day)

        # url that contains all files
        url_path = url + year + month + '/' + year + month + day + "/"
        # Get file list
        request = requests.get(url_path)
        webpage = html.fromstring(request.content)
        file_list = webpage.xpath('//a[contains(@href, "grb2")]//text()')

        # loop all file_list to get single download url
        for file_name in file_list:
            download_url = url_path + file_name
            # Initializing data_path and create local folder if not exist
            data_path = data_dir + year + month + "/" + year + month + day + "/"
            if not os.path.exists(data_path):
                print("== Creating data path:", data_path)
                os.makedirs(data_path)
            # Convert file to csv
            cvt.convert_grb_to_csv(data_path + file_name)

def download_then_convert():
    print('### STARTING APP ###')
    day_step = 10

    for d in range(day_step + 1):
        date_time = dt.datetime.now() - dt.timedelta(days=day_step) + dt.timedelta(d)
        year = str(date_time.year)
        month = str('%02d' % date_time.month)
        day = str('%02d' % date_time.day)

        # url that contains all files
        url_path = url + year + month + '/' + year + month + day + "/"
        # Get file list
        request = requests.get(url_path)
        webpage = html.fromstring(request.content)
        file_list = webpage.xpath('//a[contains(@href, "grb2")]//text()')

        # loop all file_list to get single download url
        for file_name in file_list:
            download_url = url_path + file_name
            # Initializing data_path and create local folder if not exist
            data_path = data_dir + year + month + "/" + year + month + day + "/"
            if not os.path.exists(data_path):
                print("== Creating data path:", data_path)
                os.makedirs(data_path)
            # Download file
            dl.download_file(download_url, data_path, file_name)
            # Convert file to csv
            cvt.convert_grb_to_csv(data_path + file_name)

convert_data()
download_then_convert()