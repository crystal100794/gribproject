import pandas as pd
import re, csv
import numpy as np

def csv_refactor(csv_path, file_name):
    dt = pd.read_table(csv_path, header=None)
    df = pd.DataFrame(dt)
    extracted_data = []

    for index, row in df.iterrows():
        line = re.sub("\s+", ",", row[0].strip())
        extracted_data.append(line)

    refactored = np.asarray(extracted_data)
    with open(file_name, 'w', newline='') as file:
        wr = csv.writer(file, quoting=csv.QUOTE_ALL)
        wr.writerow(extracted_data)

def csv_location_extractor(csv_path, minLat, minLong, maxLat, maxLong):
    dt = pd.read_csv(csv_path, header=None)
    df = pd.DataFrame(dt)
    extracted_data = []

    for index, row in df.iterrows():
        print(row)