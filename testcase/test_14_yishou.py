# #coding = utf-8
# import unittest
# from common.config_http import RequestMethod
# from readConfig import ReadConfig
# from common.Log import MyLog
#
# class test_shuchong(unittest.TestCase):
#     def setUp(self):
#         self.identity = "migu"
#         self.config = ReadConfig()
#         self.resultmethod = RequestMethod()
#         self.log = MyLog.get_log()
#         self.logger = self.log.get_logger()
#         self.case_name =str('书丛图书渠道接口')
#
#     def tearDown(self):
#         pass
#
#     def test_013_01(self):
#         res = self.resultmethod.get("url_013_01")
#         result = res.text.find('url')
#         self.assertEqual(result, 484)
#         self.case_name = str("书丛图书渠道接口")
#         self.log.logger.info(self.case_name + " - Code:第一个url-的索引是" + str(result)+'--------成功')
#
#     def test_013_02(self):
#         res = self.resultmethod.get("url_013_02")
#         result = res.text.find('title')
#         self.assertEqual(result,56)
#         self.case_name = str("书丛图书渠道_获取图书信息")
#         self.log.logger.info(self.case_name + " - Code:第一个title-的索引是" + str(result)+'--------成功')
#
#     def test_013_03(self):
#         res = self.resultmethod.get("url_013_03")
#         result = res.text.find('chaptername')
#         print(result)
#         self.assertEqual(result, 167)
#         self.case_name = str("书丛图书渠道_获取图书章节列表")
#         self.log.logger.info(self.case_name + " - Code:第一个chaptername-索引是" + str(result)+'--------成功')
#
#     def test_013_04(self):
#         res = self.resultmethod.get("url_013_03")
#         result = res.text.find('第2章')
#         print(result)
#         self.assertEqual(result, 486)
#         self.case_name = str("方书丛图书渠道_获取图书章节列表")
#         self.log.logger.info(self.case_name + " - Code:第2章-的索引是" + str(result) + '--------成功')
