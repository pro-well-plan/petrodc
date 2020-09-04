from unittest import TestCase
import petrodc.npd as npd
import pandas as pd


class TestNPD(TestCase):

    def test_wellbore_1(self):
        df = npd.wellbore(1)
        self.assertIsInstance(df, pd.DataFrame, msg='function is not returning a dataframe')
        columns = ['wlbOilSampleBottomDepth', 'wlbName', 'wlbNPDID_wellbore',
                   'wlbOilSampleTestType', 'wlbOilSampleDateUpdated',
                   'wlbOilSampleTestDate', 'wlbOilSampleFluidType',
                   'wlbOilSampledateReceivedDate', 'datesyncNPD', 'wlbOilSampleTestNumber',
                   'wlbOilSampleTopDepth']
        self.assertTrue(len(df) > 0, msg='No data reached')
        self.assertEqual(len(df.columns), 11, msg='Data columns have been added or removed')
        self.assertListEqual(columns, df.columns.to_list(), msg='Data columns have been changed')

    def test_wellbore_2(self):
        df = npd.wellbore(2)
        self.assertIsInstance(df, pd.DataFrame, msg='function is not returning a dataframe')
        columns = ['wlbWell', 'wlbWellboreName', 'wlbWellType', 'wlbNpdidWellbore', 'datesyncNPD']
        self.assertTrue(len(df) > 0, msg='No data reached')
        self.assertEqual(len(df.columns), 5, msg='Data columns have been added or removed')
        self.assertListEqual(columns, df.columns.to_list(), msg='Data columns have been changed')

    def test_wellbore_3(self):
        df = npd.wellbore(3)
        self.assertIsInstance(df, pd.DataFrame, msg='function is not returning a dataframe')
        columns = ['lsuNpdidLithoStratParent', 'wlbName', 'lsuBottomDepth', 'lsuLevel',
                   'lsuName', 'wlbNpdidWellbore', 'lsuNpdidLithoStrat',
                   'IsuWellboreUpdatedDate', 'datesyncNPD', 'lsuNameParent',
                   'lsuTopDepth']
        self.assertTrue(len(df) > 0, msg='No data reached')
        self.assertEqual(len(df.columns), 11, msg='Data columns have been added or removed')
        self.assertListEqual(columns, df.columns.to_list(), msg='Data columns have been changed')

    def test_wellbore_4(self):
        df = npd.wellbore(4)
        self.assertIsInstance(df, pd.DataFrame, msg='function is not returning a dataframe')
        columns = ['wlbHistoryDateUpdated', 'wlbName', 'wlbNPDID_wellbore', 'wlbHistory',
                   'datesyncNPD']
        self.assertTrue(len(df) > 0, msg='No data reached')
        self.assertEqual(len(df.columns), 5, msg='Data columns have been added or removed')
        self.assertListEqual(columns, df.columns.to_list(), msg='Data columns have been changed')

    def test_wellbore_5(self):
        df = npd.wellbore(5)
        self.assertIsInstance(df, pd.DataFrame, msg='function is not returning a dataframe')
        columns = ['wlbMudWeightAtMD', 'wlbName', 'wlbMudViscosityAtMD',
                   'wlbNPDID_wellbore', 'wlbMudDateMeasured', 'wlbMudDateUpdated',
                   'wlbYieldPointAtMD', 'wlbMD', 'wlbMudType', 'datesyncNPD']
        self.assertTrue(len(df) > 0, msg='No data reached')
        self.assertEqual(len(df.columns), 10, msg='Data columns have been added or removed')
        self.assertListEqual(columns, df.columns.to_list(), msg='Data columns have been changed')

    def test_wellbore_6(self):
        df = npd.wellbore(6)
        self.assertIsInstance(df, pd.DataFrame, msg='function is not returning a dataframe')
        columns = ['wlbDstTestNumber', 'wlbDstToDepth', 'wlbName', 'wlbDstChokeSize',
                   'wlbDstBottomHolePress', 'wlbDstFromDepth', 'wlbDstOilProd',
                   'wlbDstOilDensity', 'wlbDstGasProd', 'wlbDstFinShutInPress',
                   'wlbDstGasOilRelation', 'wlbDstDateUpdated', 'wlbDstFinFlowPress',
                   'wlbNpdidWellbore', 'datesyncNPD', 'wlbDstGasDensity',
                   'wlbDstDownholeTemperatur']
        self.assertTrue(len(df) > 0, msg='No data reached')
        self.assertEqual(len(df.columns), 17, msg='Data columns have been added or removed')
        self.assertListEqual(columns, df.columns.to_list(), msg='Data columns have been changed')

    def test_wellbore_7(self):
        df = npd.wellbore(7)
        self.assertIsInstance(df, pd.DataFrame, msg='function is not returning a dataframe')
        columns = ['wlbDocumentFormat', 'wlbName', 'wlbDocumentDateUpdated',
                   'wlbDocumentName', 'wlbNPDID_wellbore', 'wlbDocumentType',
                   'wlbDocumentUrl', 'wlbDocumentSize', 'datesyncNPD']
        self.assertTrue(len(df) > 0, msg='No data reached')
        self.assertEqual(len(df.columns), 9, msg='Data columns have been added or removed')
        self.assertListEqual(columns, df.columns.to_list(), msg='Data columns have been changed')

    def test_wellbore_8(self):
        df = npd.wellbore(8)
        self.assertIsInstance(df, pd.DataFrame, msg='function is not returning a dataframe')
        columns = ['wlbCoreNumber', 'wlbName', 'wlbCoreIntervalBottom',
                   'wlbCoreIntervalUom', 'wlbNumberOfCores', 'wlbNPDID_wellbore',
                   'wlbCoreDateUpdated', 'wlbCoreSampleAvailable', 'wlbCoreIntervalTop',
                   'wlbTotalCoreLength', 'datesyncNPD']
        self.assertTrue(len(df) > 0, msg='No data reached')
        self.assertEqual(len(df.columns), 11, msg='Data columns have been added or removed')
        self.assertListEqual(columns, df.columns.to_list(), msg='Data columns have been changed')

    def test_wellbore_9(self):
        df = npd.wellbore(9)
        self.assertIsInstance(df, pd.DataFrame, msg='function is not returning a dataframe')
        columns = ['wlbCoreNumber', 'wlbName', 'wlbCorePhotoTitle', 'wlbNPDID_wellbore',
                   'wlbCorePhotoDateUpdated', 'wlbCorePhotoImgUrl']
        self.assertTrue(len(df) > 0, msg='No data reached')
        self.assertEqual(len(df.columns), 6, msg='Data columns have been added or removed')
        self.assertListEqual(columns, df.columns.to_list(), msg='Data columns have been changed')

    def test_wellbore_10(self):
        df = npd.wellbore(10)
        self.assertIsInstance(df, pd.DataFrame, msg='function is not returning a dataframe')
        columns = ['wlbUtmZone', 'wlbWellType', 'wlbEwDeg', 'wlbEwCode', 'wlbEntryDate',
                   'wlbNsSec', 'wlbEwMin', 'wlbEwSec', 'wlbNsDecDeg',
                   'wlbProductionLicence', 'wlbNsDeg', 'wlbNpdidWellbore',
                   'wlbPurposePlanned', 'wlbField', 'wlbNsCode', 'wlbCompletionDate',
                   'wlbEwUtm', 'wlbNsMin', 'wlbWellboreName', 'wlbContent',
                   'wlbDrillingOperator', 'wlbEwDesDeg', 'wlbNsUtm', 'wlbGeodeticDatum',
                   'datesyncNPD', 'wlbMainArea']
        self.assertTrue(len(df) > 0, msg='No data reached')
        self.assertEqual(len(df.columns), 26, msg='Data columns have been added or removed')
        self.assertListEqual(columns, df.columns.to_list(), msg='Data columns have been changed')

    def test_wellbore_11(self):
        df = npd.wellbore(11)
        self.assertIsInstance(df, pd.DataFrame, msg='function is not returning a dataframe')
        columns = ['wlbHoleDepth', 'wlbName', 'wlbCasingDiameter', 'wlbNPDID_wellbore',
                   'wlbLotMudDencity', 'wlbCasingDateUpdated', 'wlbFormationTestType',
                   'datesyncNPD', 'wlbHoleDiameter', 'wlbCasingType', 'wlbCasingDepth']
        self.assertTrue(len(df) > 0, msg='No data reached')
        self.assertEqual(len(df.columns), 11, msg='Data columns have been added or removed')
        self.assertListEqual(columns, df.columns.to_list(), msg='Data columns have been changed')

    def test_wellbore_12(self):
        df = npd.wellbore(12)
        self.assertIsInstance(df, pd.DataFrame, msg='function is not returning a dataframe')
        columns = ['wlbNpdidWellboreReclass', 'wlbPluggedDate', 'wlbEwCode',
                   'wlbSeismicLocation', 'wlbMultilateral', 'wlbAgeWithHc2',
                   'fclNpdidFacilityDrilling', 'wlbEntryDate', 'wlbAgeWithHc1', 'wlbNsSec',
                   'wlbFormationWithHc1', 'wlbEwMin', 'wlbFormationWithHc2', 'wlbEwSec',
                   'prlNpdidProductionLicence', 'wlbFormationWithHc3', 'fldNpdidField',
                   'wlbProductionLicence', 'wlbNpdidWellbore', 'wlbFormationAtTd',
                   'wlbFacilityTypeDrilling', 'wlbNsCode', 'wlbCompletionDate',
                   'wlbDateReclass', 'wlbReentry', 'wlbDrillPermit', 'wlbNsMin',
                   'wlbContent', 'wlbAgeAtTd', 'wlbDrillingFacilityFixedOrMoveable',
                   'wlbEntryYear', 'wlbDrillingFacility', 'wlbEwDesDeg',
                   'wlbGeodeticDatum', 'dscNpdidDiscovery', 'wlbPluggedAbandonDate',
                   'wlbDrillingDays', 'wlbWell', 'wlbFinalVerticalDepth', 'wlbTotalDepth',
                   'wlbKellyBushElevation', 'wlbUtmZone', 'wlbPlotSymbol', 'wlbWellType',
                   'wlbDiscoveryWellbore', 'wlbEwDeg', 'wlbFactMapUrl', 'wlbWdssQcDate',
                   'wlbDateUpdated', 'wlbSubSea', 'wlbReentryExplorationActivity',
                   'wlbMaxInclation', 'wlbDiskosWellboreType', 'wlbReleasedDate',
                   'wlbCompletionYear', 'wlbNsDecDeg', 'wlbLicenceTargetName',
                   'wlbPressReleaseUrl', 'wlbStatus', 'wlbNsDeg', 'wlbPurposePlanned',
                   'wlbField', 'wlbKickOffPoint', 'wlbSiteSurvey', 'wlbWaterDepth',
                   'wlbEwUtm', 'wlbNamePart5', 'wlbNamePart6', 'wlbDiscovery',
                   'wlbNamePart3', 'wlbNamePart4', 'wlbNamePart1', 'wlbWellboreName',
                   'wlbAgeWithHc3', 'wlbNamePart2', 'wlbNpdidSiteSurvey',
                   'wlbDrillingOperator', 'wlbBottomHoleTemperature', 'wlbNsUtm',
                   'wlbLicensingActivity', 'wlbFactPageUrl', 'wlbDiskosWellboreParent',
                   'wlbDateUpdatedMax', 'wlbPurpose', 'datesyncNPD', 'wlbMainArea',
                   'wlbReclassFromWellbore']
        self.assertTrue(len(df) > 0, msg='No data reached')
        self.assertEqual(len(df.columns), 87, msg='Data columns have been added or removed')
        self.assertListEqual(columns, df.columns.to_list(), msg='Data columns have been changed')

    def test_wellbore_13(self):
        df = npd.wellbore(13)
        self.assertIsInstance(df, pd.DataFrame, msg='function is not returning a dataframe')
        columns = ['wlbNpdidWellboreReclass', 'wlbPluggedDate', 'wlbEwCode',
                   'wlbMultilateral', 'fclNpdidFacilityDrilling', 'wlbEntryDate',
                   'wlbNsSec', 'wlbEwMin', 'wlbEwSec', 'prlNpdidProductionLicence',
                   'wlbContentPlanned', 'fldNpdidField', 'wlbProductionLicence',
                   'wlbNpdidWellbore', 'wlbProductionFacility', 'wlbFacilityTypeDrilling',
                   'wlbNsCode', 'wlbCompletionDate', 'fclNpdidFacilityProducing',
                   'wlbDrillPermit', 'wlbNsMin', 'wlbContent',
                   'wlbDrillingFacilityFixedOrMoveable', 'wlbEntryYear',
                   'wlbCompPreDrillDate', 'wlbDrillingFacility', 'wlbEwDesDeg',
                   'wlbEntryPreDrillDate', 'wlbGeodeticDatum', 'dscNpdidDiscovery',
                   'wlbPluggedAbandonDate', 'wlbWell', 'wlbFinalVerticalDepth',
                   'wlbTotalDepth', 'wlbKellyBushElevation', 'wlbUtmZone', 'wlbPlotSymbol',
                   'prlNpdidProdLicenceTarget', 'wlbWellType', 'wlbDiscoveryWellbore',
                   'wlbEwDeg', 'wlbFactMapUrl', 'wlbWdssQcDate', 'wlbDateUpdated',
                   'wlbSubSea', 'wlbDiskosWellboreType', 'wlbReleasedDate',
                   'wlbCompletionYear', 'wlbNsDecDeg', 'wlbLicenceTargetName', 'wlbStatus',
                   'wlbNsDeg', 'wlbPurposePlanned', 'wlbField', 'wlbKickOffPoint',
                   'wlbWaterDepth', 'wlbEwUtm', 'wlbNamePart5', 'wlbNamePart6',
                   'wlbDiscovery', 'wlbNamePart3', 'wlbNamePart4', 'wlbNamePart1',
                   'wlbWellboreName', 'wlbNamePart2', 'wlbDrillingOperator', 'wlbNsUtm',
                   'wlbLicensingActivity', 'wlbFactPageUrl', 'wlbDiskosWellboreParent',
                   'wlbDateUpdatedMax', 'wlbPurpose', 'datesyncNPD', 'wlbMainArea',
                   'wlbReclassFromWellbore']
        self.assertTrue(len(df) > 0, msg='No data reached')
        self.assertEqual(len(df.columns), 75, msg='Data columns have been added or removed')
        self.assertListEqual(columns, df.columns.to_list(), msg='Data columns have been changed')

    def test_wellbore_14(self):
        df = npd.wellbore(14)
        self.assertIsInstance(df, pd.DataFrame, msg='function is not returning a dataframe')
        columns = ['wlbWell', 'wlbTotalDepth', 'wlbKellyBushElevation', 'wlbPluggedDate',
                   'wlbUtmZone', 'wlbWellType', 'wlbEwDeg', 'wlbDateUpdated', 'wlbEwCode',
                   'wlbSeismicLocation', 'wlbEntryDate', 'wlbNsSec', 'wlbEwMin',
                   'wlbCompletionYear', 'wlbEwSec', 'wlbNsDecDeg', 'wlbProductionLicence',
                   'wlbLicenceTargetName', 'wlbNsDeg', 'wlbNpdidWellbore', 'wlbNsCode',
                   'wlbCompletionDate', 'wlbSiteSurvey', 'wlbWaterDepth', 'wlbEwUtm',
                   'wlbNamePart5', 'wlbNamePart6', 'wlbNamePart3', 'wlbDrillPermit',
                   'wlbNamePart4', 'wlbNsMin', 'wlbNamePart1', 'wlbWellboreName',
                   'wlbNamePart2', 'wlbNpdidSiteSurvey', 'wlbDrillingOperator',
                   'wlbEntryYear', 'wlbDrillingFacility', 'wlbEwDesDeg', 'wlbNsUtm',
                   'wlbFactPageUrl', 'wlbDateUpdatedMax', 'wlbGeodeticDatum', 'wlbPurpose',
                   'wlbPluggedAbandonDate', 'datesyncNPD', 'wlbMainArea']
        self.assertTrue(len(df) > 0, msg='No data reached')
        self.assertEqual(len(df.columns), 47, msg='Data columns have been added or removed')
        self.assertListEqual(columns, df.columns.to_list(), msg='Data columns have been changed')
