#coding = utf-8
import unittest
from common.config_http import RequestMethod
from common.Log import MyLog

class test_shuqi(unittest.TestCase):

    def setUp(self):
        self.resultmethod = RequestMethod()
        self.log = MyLog.get_log()
        self.case_name =str('第三方书旗图书渠道接口')

    def tearDown(self):
        pass

    def test_012_01(self):
        res = self.resultmethod.get("url_006_01")
        result = res.text.find('bookid')
        self.assertEqual(result, 51)
        self.case_name = str("第三方书旗图书渠道接口")
        self.log.logger.info(self.case_name + " - Code:第一个'bookid'-的索引是--" + str(result)+'--------成功')

    def test_012_02(self):
        res = self.resultmethod.get("url_006_02")
        result = res.text.find('现言')
        self.assertEqual(result, 66)
        self.case_name = str("书旗图书渠道_作品信息")
        self.log.logger.info(self.case_name + " - Code:现言 -的索引是--" + str(result)+'--------成功')

    def test_012_03(self):
        res = self.resultmethod.get("url_006_03")
        result = res.text.find('第1章')
        self.assertEqual(result, 291)
        self.case_name = str("书旗图书渠道_章节列表")
        self.log.logger.info(self.case_name + " - Code:第1章-的索引是--" + str(result)+'--------成功')

    def test_012_04(self):
        res = self.resultmethod.get("url_006_04")
        result = res.text.find('十三年前')
        self.assertEqual(result, 77)
        self.case_name = str("书旗图书渠道_正文接口")
        self.log.logger.info(self.case_name + " - Code:十三年前-的索引是--" + str(result) + '--------成功')
