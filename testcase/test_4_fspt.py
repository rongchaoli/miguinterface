# import unittest
# from common.config_http import RequestMethod
# from readConfig import ReadConfig
# from common.Log import MyLog
#
#
# class test_aiqiyi(unittest.TestCase):
#
#     def setUp(self):
#         self.config = ReadConfig()
#         self.resultmethod = RequestMethod()
#         self.log = MyLog.get_log()
#         self.logger = self.log.get_logger()
#         self.case_name =str('第三方粉色平台图书渠道接口')
#
#     def tearDown(self):
#         self.log.build_case_line(self.case_name, self.result['code'], self.result['msg'])
