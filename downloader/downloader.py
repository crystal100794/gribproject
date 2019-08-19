import requests
from lxml import html
import wget

# downloader is a function for downloading grib2 data from this url
# https://nomads.ncdc.noaa.gov/data/gfs4/
# for example download data at August 1, 2019, the format will be
# ym = 201908, ymd = 20190801
# data_path = local path of data
def file_downloader(url, data_path, ym, ymd):
    url_full = url + '/' + ym + '/' + ymd + '/'

    print('Start getting files from url', url_full)
    request = requests.get(url_full)
    webpage = html.fromstring(request.content)

    file_list = webpage.xpath('//a[contains(@href, "grb2")]//text()')

    for file in file_list:
        total_files = len(file_list)
        download_url = url_full + file
        print('Start downloading file ' + str(file_list.index(file) + 1) + '/' + str(total_files), download_url)

        #wget download and show the download progress bar
        result = wget.download(download_url, data_path + '/' + file)

        print(' === Result:', result)
