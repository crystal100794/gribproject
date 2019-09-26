import subprocess
import os

def convert_grb_to_csv(file_path):
    grb2_path = str(file_path)
    csv_path = grb2_path.replace('.grb2', '.csv')
    print('=== Try to convert file: ', file_path)
    print('csv_path', csv_path)
    if os.path.exists(csv_path):
        print('== File already converted, skipping')
    else:
        try:
            if os.path.exists(file_path):
                print('== Start subprocess to convert file...')
                data_to_extract = 'dataDate,dataTime,shortName,typeOfLevel'
                grib_cmd = 'grib_get_data -p ' + data_to_extract + ' ' + file_path + ' > ' + csv_path
                print('= Sub Process Command:', grib_cmd)
                subprocess.call(grib_cmd, shell=True)
                print('File convert completed!')
            else:
                print('File not found, pass')
        except subprocess.CalledProcessError as e:
            print(e.output)


