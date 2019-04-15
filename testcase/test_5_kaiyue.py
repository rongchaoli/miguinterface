#coding = utf-8
import unittest
from common.config_http import RequestMethod
from common.Log import MyLog

class test_kaiyue(unittest.TestCase):

    def setUp(self):
        self.resultmethod = RequestMethod()
        self.log = MyLog.get_log()
        self.case_name =str('第三方开阅图书渠道接口')

    def tearDown(self):
        pass

    def test_005_01(self):
        res = self.resultmethod.get("url_005_01")
        result = res.text.find('bookid')
        self.assertEqual(result, 59)
        self.case_name = str("第三方开阅图书渠道接口")
        self.log.logger.info(self.case_name + " - Code:第一个'bookid'-的索引是--" + str(result)+'--------成功')

    def test_005_02(self):
        res = self.resultmethod.get("url_005_02")
        result = res.text.find('现言')
        self.assertEqual(result, 110)
        self.case_name = str("开阅图书渠道_作品信息")
        self.log.logger.info(self.case_name + " - Code:现言 -的索引是--" + str(result)+'--------成功')

    def test_005_03(self):
        res = self.resultmethod.get("url_005_03")
        result = res.text.find('默认卷')
        self.assertEqual(result, 71)
        self.case_name = str("开阅图书渠道_章节列表")
        self.log.logger.info(self.case_name + " - Code:默认卷-的索引是--" + str(result)+'--------成功')

    def test_005_04(self):
        res = self.resultmethod.get("url_005_04")
        result = res.text.find('极不舒服')
        self.assertEqual(result, 60)
        self.case_name = str("开阅图书渠道_正文接口")
        self.log.logger.info(self.case_name + " - Code:极不舒服-的索引是--" + str(result) + '--------成功')
