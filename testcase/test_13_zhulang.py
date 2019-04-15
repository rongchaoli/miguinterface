#coding = utf-8
import unittest
from common.config_http import RequestMethod
from common.Log import MyLog

class test_zhulang(unittest.TestCase):

    def setUp(self):
        self.resultmethod = RequestMethod()
        self.log = MyLog.get_log()
        self.case_name =str('第三方逐浪图书渠道接口')

    def tearDown(self):
        pass

    def test_013_01(self):
        res = self.resultmethod.get("url_013_01")
        result = res.text.find('bookid')
        self.assertEqual(result, 3)
        self.case_name = str("第三方逐浪图书渠道接口")
        self.log.logger.info(self.case_name + " - Code:第一个'bookid'-的索引是--" + str(result)+'--------成功')

    def test_013_02(self):
        res = self.resultmethod.get("url_013_02")
        result = res.text.find('一代仙帝')
        self.assertEqual(result, 118)
        self.case_name = str("逐浪图书渠道_作品信息")
        self.log.logger.info(self.case_name + " - Code:一代仙帝 -的索引是--" + str(result)+'--------成功')

    def test_013_03(self):
        res = self.resultmethod.get("url_013_03")
        result = res.text.find('chaptersList')
        self.assertEqual(result, 3)
        self.case_name = str("逐浪图书渠道_章节列表")
        self.log.logger.info(self.case_name + " - Code:chaptersList-的索引是--" + str(result)+'--------成功')

    def test_013_04(self):
        res = self.resultmethod.get("url_013_04")
        result = res.text.find('第一章 ')
        self.assertEqual(result, 37)
        self.case_name = str("逐浪图书渠道_正文接口")
        self.log.logger.info(self.case_name + " - Code:第一章-的索引是--" + str(result) + '--------成功')
