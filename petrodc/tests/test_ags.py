from unittest import TestCase
import petrodc.ags as ags
import pandas as pd


class TestAGS(TestCase):

    def test_get_las(self):
        data = ags.get_las(10)
        self.assertIsInstance(data, dict, msg='function is not returning a dictionary')
        self.assertEqual(len(data), 10, msg='incorrect number of files')
        first_file = list(data.values())[0]
        self.assertIsInstance(first_file, pd.DataFrame, msg='single file data is not presented as a dataframe')
