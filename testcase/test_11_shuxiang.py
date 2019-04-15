#coding = utf-8
import unittest
from common.config_http import RequestMethod
from common.Log import MyLog

class test_shuxiang(unittest.TestCase):

    def setUp(self):
        self.resultmethod = RequestMethod()
        self.log = MyLog.get_log()
        self.case_name =str('第三方书香图书渠道接口')

    def tearDown(self):
        pass

    def test_011_01(self):
        res = self.resultmethod.get("url_011_01")
        result = res.text.find('booktitle')
        self.assertEqual(result, 148)
        self.case_name = str("第三方书香图书渠道接口")
        self.log.logger.info(self.case_name + " - Code:第一个'booktitle'-的索引是--" + str(result)+'--------成功')

    def test_011_02(self):
        res = self.resultmethod.get("url_011_02")
        result = res.text.find('闪婚独宠')
        self.assertEqual(result,390)
        self.case_name = str("书香图书渠道_获取图书信息")
        self.log.logger.info(self.case_name + " - Code:闪婚独宠 -的索引是--" + str(result)+'--------成功')

    def test_011_03(self):
        res = self.resultmethod.get("url_011_03")
        result = res.text.find('第1章')
        self.assertEqual(result, 115)
        self.case_name = str("书香丛图书渠道_获取图书章节列表")
        self.log.logger.info(self.case_name + " - Code:第1章-的索引是--" + str(result)+'--------成功')

    def test_011_04(self):
        res = self.resultmethod.get("url_011_04")
        result = res.text.find('莫晚晚')
        self.assertEqual(result, 131)
        self.case_name = str("书香图书渠道_获取图书章节内容")
        self.log.logger.info(self.case_name + " - Code:莫晚晚-的索引是--" + str(result) + '--------成功')
