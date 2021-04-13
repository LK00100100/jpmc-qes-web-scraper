from enum import Enum
from typing import List
from io import StringIO
import csv


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

    def save_to_location(self, save_to_folder):
        """
        saves a file for each report in a standard csv.
        :param save_to_folder: folder path
        :return:
        """

        if self.daily_performance_table is not None:
            file = open("{}-{}.csv".format(self.report_name, "daily_performance"), "w")
            output_str = QesReport.get_2d_table_csv_str(self.daily_performance_table)
            file.write(output_str)
            file.close()

        if self.intraday_activity_table is not None:
            file = open("{}-{}.csv".format(self.report_name, "intraday_activity"), "w")
            output_str = QesReport.get_2d_table_csv_str(self.intraday_activity_table)
            file.write(output_str)
            file.close()

        if self.strategy_detail_table is not None:
            file = open("{}-{}.csv".format(self.report_name, "strategy_detail"), "w")
            output_str = QesReport.get_2d_table_csv_str(self.strategy_detail_table)
            file.write(output_str)
            file.close()

        if self.indicative_next_day_table is not None:
            file = open("{}-{}.csv".format(self.report_name, "indicative_next_day"), "w")
            output_str = QesReport.get_2d_table_csv_str(self.indicative_next_day_table)
            file.write(output_str)
            file.close()

    @staticmethod
    def get_2d_table_csv_str(array2d: List[List[str]]):
        """
        Prints a csv string of a 2d str array.
        Accounts for commas and quotes
        :param array2d:
        :return:
        """
        answer = ""
        for row in array2d:
            line = StringIO()
            writer = csv.writer(line)
            writer.writerow(row)
            csv_str = line.getvalue()
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
