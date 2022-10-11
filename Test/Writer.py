import csv

array = [None] * 10


class Writer:
    def __init__(self):
        pass

    def insert_to_array(self, index, data):
        array[index] = data

    def write_csv(self, filename):
        filename = "csv/" + filename
        file = open(filename, 'a+', newline='')
        writer = csv.writer(file)
        writer.writerow(array)
        file.close()
