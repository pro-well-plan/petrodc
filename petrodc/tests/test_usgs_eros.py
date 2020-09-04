from unittest import TestCase
import petrodc.usgs_eros as topo
import pandas as pd


class TestUSGS(TestCase):

    def test_elevation(self):
        df = topo.elevation(lat=(40, 41), lon=(-61, -60)).data
        self.assertIsInstance(df, pd.DataFrame, msg='function is not returning a dataframe')
        self.assertTrue(len(df) > 0, msg='No data reached')
        self.assertEqual(len(df.columns), 3, msg='different number of columns')
        columns = ['lat', 'lon', 'elev']
        self.assertListEqual(columns, df.columns.to_list(), msg='Difference in column headers')

    def test_point_elev(self):
        elevation = topo.point_elev(50, 6)
        self.assertIsInstance(elevation, int, msg='function is not returning an integer')
