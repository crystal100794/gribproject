import requests
from lxml import html
import wget
import os
from datetime import timedelta, date
import time
from os import makedirs

def file_downloader(url, data_path):
    print('=== Start getting files from url', url)
    request = requests.get(url)
    webpage = html.fromstring(request.content)
    file_list = webpage.xpath('//a[contains(@href, ".grb2")]//text()')

    for file_name in file_list:
        total_files = len(file_list)
        download_url = url + file_name
        print('== Start downloading file ' + str(file_list.index(file_name) + 1) + '/' + str(total_files), download_url)

        # wget download and show the download progress bar
        result = wget.download(download_url, data_path + file_name)

        if os.path.exists(data_path + file_name):
            print('= Result:', result)
        else:
            print('= Download error: ', file_name)


def download_file(download_url, data_path, file_name):
    if os.path.exists(data_path + file_name):
        print('File exist, skipping')
    else:
        # wget download and show the download progress bar
        print('Start downloading file', file_name)
        result = wget.download(download_url, data_path + file_name)
        return result


















