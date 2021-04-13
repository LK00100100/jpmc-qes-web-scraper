from unittest import TestCase

from qes_report import QesReport


class TestQesReport(TestCase):

    def test_get_2d_table_csv_str(self):
        table = [["a", "\"", ",", "b"], ["1", "2", "3", "4"]]

        the_str = QesReport.get_2d_table_csv_str(table)

        expected = 'a,"""",",",b\r\n'
        expected += "1,2,3,4\r\n"
        self.assertEqual(expected, the_str)

    def test_save_to_location(self):
        qes_report = QesReport()
        qes_report.report_name = "some test.html"
        qes_report.daily_performance_table = [["a", "b"], ["1", "2"]]
        qes_report.intraday_activity_table = [["c", "d"], ["3", "4"]]
        qes_report.strategy_detail_table = [["e", "f"], ["5", "6"]]
        qes_report.indicative_next_day_table = [["g", "h"], ["7", "8"]]

        folder_path = "../output"
        qes_report.save_to_location(folder_path)
