import csv
import pandas as pd

array = [None] * 22


class Writer:
    def __init__(self):
        pass

    def insert_to_array(self, index, data):
        array[index] = data

    def write_csv(self, filename):
        filename = "csv/" + filename
        file = open(filename, 'w')
        writer = csv.writer(file)
        writer.writerow(array)
        file.close()
        pd.read_csv(filename, header=None).T.to_csv(filename, header=False, index=False)
