from enum import Enum


class QesReport:
    """
    Holds 2d arrays of tables
    """

    def __init__(self):
        # these are just 2d arrays of the table.
        # 0th row is the header, the rest are data rows.
        self.daily_performance_table = []
        self.strategy_detail_table = []
        self.indicative_next_day_table = []


class QesReportTableNames(Enum):
    """
    These are the table names in the QES report.
    They're also the html h3 element texts.
    """
    daily_performance = "Daily Performance"
    strategy_detail = "Strategy Detail"
    indicative_next_day = "Indicative Next Day"
