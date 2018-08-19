import os


class ReportCreator(object):


    @staticmethod
    def build_header():
        print("PARENT REPORTCREATOR\n")

    @staticmethod
    def build_report(self):
        self.build_header()


    @staticmethod
    def create_csv_report(columns, rows, filePath):
        os.remove(filePath)
        with open(filePath, 'a') as newReport:
            for column in columns:
                newReport.write(column)

            newReport.write("\n")
            for row in rows:
                newReport.write(row.storeName + ", " + row.amount + ", " + row.accountNumber + "\n")

    @staticmethod
    def create_frequency_report(columns, rows, filePath):
        os.remove(filePath)
        with open(filePath, 'a') as newReport:
            for column in columns:
                newReport.write(column)

            newReport.write("\n")
            for row in rows:
                newReport.write(row.storeName + ", " + row.amount + ", " + row.accountNumber + "\n")

