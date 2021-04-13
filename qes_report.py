from enum import Enum
from typing import List
from io import StringIO
import csv
import os


class QesReport:
    """
    Holds one QesReport.
    Has 2d arrays of tables
    """

    def __init__(self):
        self.report_name = None

        # these are just 2d arrays of the table.
        # 0th row is the header, the rest are data rows.
        self.daily_performance_table = []
        self.intraday_activity_table = []
        self.strategy_detail_table = []
        self.indicative_next_day_table = []

    def __repr__(self):
        output = "Daily Performance\n"
        output += QesReport.get_2d_table_csv_str(self.daily_performance_table)
        output += "\n"
        output += "Intraday Activity\n"
        output += QesReport.get_2d_table_csv_str(self.intraday_activity_table)
        output += "\n"
        output += "Strategy Detail\n"
        output += QesReport.get_2d_table_csv_str(self.strategy_detail_table)
        output += "\n"
        output += "Indicative Next Day\n"
        output += QesReport.get_2d_table_csv_str(self.indicative_next_day_table)
        return output

    def save_to_location(self, folder_path):
        """
        saves a file for each report in a standard csv.
        If one of the reports is none, it will skip that one report.
        :param folder_path:
        :return:
        """

        if len(self.daily_performance_table) != 0:
            file_name = "{}-{}.csv".format(self.report_name, "daily_performance")
            file_path = os.path.join(folder_path, file_name)
            file = open(file_path, "w")
            output_str = QesReport.get_2d_table_csv_str(self.daily_performance_table)
            file.write(output_str)
            file.close()

        if len(self.intraday_activity_table) != 0:
            file_name = "{}-{}.csv".format(self.report_name, "intraday_activity")
            file_path = os.path.join(folder_path, file_name)
            file = open(file_path, "w")
            output_str = QesReport.get_2d_table_csv_str(self.intraday_activity_table)
            file.write(output_str)
            file.close()

        if len(self.strategy_detail_table) != 0:
            file_name = "{}-{}.csv".format(self.report_name, "strategy_detail")
            file_path = os.path.join(folder_path, file_name)
            file = open(file_path, "w")
            output_str = QesReport.get_2d_table_csv_str(self.strategy_detail_table)
            file.write(output_str)
            file.close()

        if len(self.indicative_next_day_table) != 0:
            file_name = "{}-{}.csv".format(self.report_name, "indicative_next_day")
            file_path = os.path.join(folder_path, file_name)
            file = open(file_path, "w")
            output_str = QesReport.get_2d_table_csv_str(self.indicative_next_day_table)
            file.write(output_str)
            file.close()

    @staticmethod
    def get_2d_table_csv_str(array2d: List[List[str]]):
        """
        Prints a csv string of a 2d str array.
        Accounts for commas and quotes.

        :param array2d:
        :return:
        """
        answer = ""
        for row in array2d:
            line = StringIO()
            writer = csv.writer(line)
            writer.writerow(row)
            # rstrips the /r/n (double new line in file)
            # the last value could be spaces, which will be stripped.
            # but for this job, it wouldn't matter
            csv_str = line.getvalue().rstrip() + "\n"
            answer += csv_str  # ends with new line

        return answer


class QesReportTableNames(Enum):
    """
    These are the table names in the QES report.
    They're also the html h3/h4 element texts.
    """
    daily_performance = "Daily Performance"
    intraday_activity = "Intraday Activity"
    strategy_detail = "Strategy Detail"
    indicative_next_day = "Indicative Next Day"
