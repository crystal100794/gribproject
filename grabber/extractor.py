import pandas as pd
import os


def csv_refactor(data_path, file_name):
        csv = os.path.basename(data_path + file_name)
        print(csv)
        print('Start writing world.csv => vietnam.csv')
        with open(csv, 'r') as f_in, open('_' + csv, 'w') as f_out:
            [f_out.write(','.join(line.split()) + '\n') for line in f_in]
            print('Start remove world.csv')
        try:
            os.remove(csv)
        except :
            print("Something went wrong")


def get_location_data(filename, data_path):
    for data in data_path:
        df = pd.read_csv('_'+ filename)
        dt = df[(df.Latitude >= 8.75) & (df.Latitude <= 23.25) & (df.Longitude >= 102.25) & (df.Longitude <= 115.25)]
        for index, row in df.iterrows():
            if row not in dt :
                print("Getting VietNam data")
                df.drop(index, inplace = True)


