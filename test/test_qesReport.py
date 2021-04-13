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
        pass
