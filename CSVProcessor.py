import argparse
from Utilities.CSVReader import CSVReader
from Utilities.ReportCreator import ReportCreator

parser = argparse.ArgumentParser()
parser.add_argument("--inputPath", type=str, help="CSV To Process Path", required=True)
parser.add_argument("--outputPath", type=str, help="Output Path", required=True)

option = parser.parse_args()

def main():

    print("CSVParser, 2018")
    print(option.inputPath)
    print(option.outputPath)

    csvReader = CSVReader()
    columns, rows = csvReader.read_csv(option.inputPath)

    reportCreator = ReportCreator()
    reportCreator.create_csv_report(columns, rows, option.outputPath)
    reportCreator.create_frequency_report(columns, rows, option.outputPath)


if __name__ == "__main__":
    main()