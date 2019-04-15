import unittest
from common.config_http import RequestMethod
from readConfig import ReadConfig
from common.Log import MyLog
import hashlib

class test_aiqiyi(unittest.TestCase):

    def setUp(self):
        self.identity = "migu"
        self.config = ReadConfig()
        self.resultmethod = RequestMethod()
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        self.case_name = str('第三方爱奇艺图书渠道接口')

    def tearDown(self):
        self.log.build_case_line(self.case_name, self.result['code'], self.result['msg'])

    def test_001_01(self):
        res = self.resultmethod.get('url_001_01')
        self.result = res.json()
        self.assertEqual(self.result['msg'], 'Success')
        self.case_name = str('第三方爱奇艺图书渠道接口')

    def test_001_02(self):
        res = self.resultmethod.get('url_001_02')
        self.result = res.json()
        self.assertEqual(self.result['msg'], 'Success')
        self.case_name = str('爱奇艺获取图书信息接口')

    def test_001_03(self):
        res = self.resultmethod.get('url_001_03')
        self.result = res.json()
        self.assertEqual(self.result['msg'], 'Success')
        self.case_name = str('爱奇艺获取图书结构接口')

    def test_001_04(self):
        res = self.resultmethod.get('url_001_04')
        self.result = res.json()
        self.assertEqual(self.result['msg'], 'Success')
        self.case_name = str('获取指定书籍ID的章节详情(包含内容)')
