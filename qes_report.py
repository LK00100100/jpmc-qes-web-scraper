from enum import Enum
from typing import List


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
        self.strategy_detail_table = []
        self.indicative_next_day_table = []

    def __repr__(self):
        output = "Daily Performance\n"
        output += QesReport._get_2d_table_str(self.daily_performance_table)
        output += "\n"
        output += "Strategy Detail\n"
        output += QesReport._get_2d_table_str(self.strategy_detail_table)
        output += "\n"
        output += "Indicative Next Day\n"
        output += QesReport._get_2d_table_str(self.indicative_next_day_table)
        return output

    @staticmethod
    def _get_2d_table_str(array2d: List[List[str]]):
        # TODO fix CSV string
        answer = ""
        for row in array2d:
            answer += ",".join(row) + "\n"

        return answer


class QesReportTableNames(Enum):
    """
    These are the table names in the QES report.
    They're also the html h3/h4 element texts.
    """
    daily_performance = "Daily Performance"
    strategy_detail = "Strategy Detail"
    indicative_next_day = "Indicative Next Day"
