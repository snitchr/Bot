from .config import sample_data
from .context import pandas_ta

from unittest import skip, TestCase
from pandas import DataFrame


class TestTrendExtension(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = sample_data

    @classmethod
    def tearDownClass(cls):
        del cls.data

    def setUp(self): pass
    def tearDown(self): pass


    def test_adx_ext(self):
        self.data.ta.adx(append=True)
        self.assertIsInstance(self.data, DataFrame)
        self.assertEqual(list(self.data.columns[-3:]), ["ADX_14", "DMP_14", "DMN_14"])

    def test_amat_ext(self):
        self.data.ta.amat(append=True)
        self.assertIsInstance(self.data, DataFrame)
        self.assertEqual(list(self.data.columns[-2:]), ["AMATe_LR_2", "AMATe_SR_2"])

    def test_aroon_ext(self):
        self.data.ta.aroon(append=True)
        self.assertIsInstance(self.data, DataFrame)
        self.assertEqual(list(self.data.columns[-3:]), ["AROOND_14", "AROONU_14", "AROONOSC_14"])

    def test_chop_ext(self):
        self.data.ta.chop(append=True, ln=False)
        self.assertIsInstance(self.data, DataFrame)
        self.assertEqual(self.data.columns[-1], "CHOP_14_1_100")

        self.data.ta.chop(append=True, ln=True)
        self.assertIsInstance(self.data, DataFrame)
        self.assertEqual(self.data.columns[-1], "CHOPln_14_1_100")

    def test_cksp_ext(self):
        self.data.ta.cksp(tvmode=False, append=True)
        self.assertIsInstance(self.data, DataFrame)
        self.assertEqual(list(self.data.columns[-2:]), ["CKSPl_10_3_20", "CKSPs_10_3_20"])

    def test_cksp_tv_ext(self):
        self.data.ta.cksp(tvmode=True, append=True)
        self.assertIsInstance(self.data, DataFrame)
        self.assertEqual(list(self.data.columns[-2:]), ["CKSPl_10_1_9", "CKSPs_10_1_9"])

    def test_decay_ext(self):
        self.data.ta.decay(append=True)
        self.assertIsInstance(self.data, DataFrame)
        self.assertEqual(self.data.columns[-1], "LDECAY_5")

        self.data.ta.decay(mode="exp", append=True)
        self.assertIsInstance(self.data, DataFrame)
        self.assertEqual(self.data.columns[-1], "EXPDECAY_5")

    def test_decreasing_ext(self):
        self.data.ta.decreasing(append=True)
        self.assertIsInstance(self.data, DataFrame)
        self.assertEqual(self.data.columns[-1], "DEC_1")

        self.data.ta.decreasing(length=3, strict=True, append=True)
        self.assertIsInstance(self.data, DataFrame)
        self.assertEqual(self.data.columns[-1], "SDEC_3")

    def test_dpo_ext(self):
        self.data.ta.dpo(append=True)
        self.assertIsInstance(self.data, DataFrame)
        self.assertEqual(self.data.columns[-1], "DPO_20")

    def test_increasing_ext(self):
        self.data.ta.increasing(append=True)
        self.assertIsInstance(self.data, DataFrame)
        self.assertEqual(self.data.columns[-1], "INC_1")

        self.data.ta.increasing(length=3, strict=True, append=True)
        self.assertIsInstance(self.data, DataFrame)
        self.assertEqual(self.data.columns[-1], "SINC_3")

    def test_long_run_ext(self):
        # Nothing passed, return self
        self.assertEqual(self.data.ta.long_run(append=True).shape, self.data.shape)

        fast = self.data.ta.ema(8)
        slow = self.data.ta.ema(21)
        self.data.ta.long_run(fast, slow, append=True)
        self.assertIsInstance(self.data, DataFrame)
        self.assertEqual(self.data.columns[-1], "LR_2")

    def test_psar_ext(self):
        self.data.ta.psar(append=True)
        self.assertIsInstance(self.data, DataFrame)
        self.assertEqual(
            list(self.data.columns[-4:]), ["PSARl_0.02_0.2", "PSARs_0.02_0.2", "PSARaf_0.02_0.2", "PSARr_0.02_0.2"])

    def test_qstick_ext(self):
        self.data.ta.qstick(append=True)
        self.assertIsInstance(self.data, DataFrame)
        self.assertEqual(self.data.columns[-1], "QS_10")

    def test_short_run_ext(self):
        # Nothing passed, return self
        self.assertEqual(
            self.data.ta.short_run(append=True).shape, self.data.shape)

        fast = self.data.ta.ema(8)
        slow = self.data.ta.ema(21)
        self.data.ta.short_run(fast, slow, append=True)
        self.assertIsInstance(self.data, DataFrame)
        self.assertEqual(self.data.columns[-1], "SR_2")

    def test_ttm_trend_ext(self):
        self.data.ta.ttm_trend(append=True)
        self.assertIsInstance(self.data, DataFrame)
        self.assertEqual(list(self.data.columns[-1:]), ["TTM_TRND_6"])

    def test_vortext_ext(self):
        self.data.ta.vortex(append=True)
        self.assertIsInstance(self.data, DataFrame)
        self.assertEqual(list(self.data.columns[-2:]), ["VTXP_14", "VTXM_14"])
