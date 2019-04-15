#coding = utf-8
import unittest
from common.config_http import RequestMethod
from common.Log import MyLog

class test_shuxiang(unittest.TestCase):

    def setUp(self):
        self.resultmethod = RequestMethod()
        self.log = MyLog.get_log()
        self.case_name =str('第三方百度阅读图书渠道接口')

    def tearDown(self):
        pass

    def test_011_01(self):
        res = self.resultmethod.get("url_009_01")
        result = res.text.find('id')
        self.assertEqual(result, 3)
        self.case_name = str("第三方百度阅读图书渠道接口")
        self.log.logger.info(self.case_name + " - Code:第一个'id'-的索引是--" + str(result)+'--------成功')

    def test_011_02(self):
        res = self.resultmethod.get("url_009_02")
        result = res.text.find('bookstatus')
        self.assertEqual(result,2)
        self.case_name = str("百度阅读图书渠道接口_获取书籍属性列表")
        self.log.logger.info(self.case_name + " - Code:bookstatus -的索引是--" + str(result)+'--------成功')

    def test_011_03(self):
        res = self.resultmethod.get("url_009_03")
        result = res.text.find('第一章')
        self.assertEqual(result, 17)
        self.case_name = str("百度阅读图书渠道接口_获取书籍章节列表")
        self.log.logger.info(self.case_name + " - Code:第一章 -的索引是--" + str(result)+'--------成功')

    def test_011_04(self):
        res = self.resultmethod.get("url_009_04")
        result = res.text.find('volumeid')
        self.assertEqual(result, 20)
        self.case_name = str("百度阅读图书渠道接口_获取章节内容")
        self.log.logger.info(self.case_name + " - Code:volumeid-的索引是--" + str(result) + '--------成功')
