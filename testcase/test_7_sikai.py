import unittest
from common.config_http import RequestMethod
from readConfig import ReadConfig
from common.Log import MyLog


class test_sikai(unittest.TestCase):

    def setUp(self):
        self.config = ReadConfig()
        self.resultmethod = RequestMethod()
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        self.case_name = str('第三方斯凯图书渠道接口')

    def tearDown(self):
        self.log.logger.info(self.case_name+" - Code:"+str(self.result['code']))

    def test_001_01(self):
        res = self.resultmethod.get('url_007_01')
        self.result = res.json()
        self.assertEqual(self.result['code'],200)
        self.case_name = str('第三方斯凯图书渠道接口')

    def test_001_02(self):
        res = self.resultmethod.get('url_007_02')
        self.result = res.json()
        self.assertEqual(self.result['code'], 200)
        self.case_name = str('斯凯图书渠道_获取图书信息')

    def test_001_03(self):
        res = self.resultmethod.get('url_007_03')
        self.result = res.json()
        self.assertEqual(self.result['code'], 200)
        self.case_name = str('斯凯图书渠道_获取图书章节列表')

    def test_001_04(self):
        res = self.resultmethod.get('url_007_04')
        self.result = res.json()
        self.assertEqual(self.result['code'], 200)
        self.case_name = str('斯凯图书渠道_获取图书内容')
