import csv
from Models.LineItem import LineItem


class CSVReader(object):

    @staticmethod
    def read_csv(fileName):
        with open(fileName) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            columns = []
            rows = []
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    columns = row
                    print(row)
                    line_count += 1
                else:
                    print(row)
                    newItem = LineItem(row[0], row[1], row[2])
                    rows.append(newItem)
                    line_count += 1
            print('Processed {line_count} lines.')
            return columns, rows
