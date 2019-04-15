import unittest
from common.config_http import RequestMethod
from readConfig import ReadConfig
from common.Log import MyLog
import requests
import warnings


class test_wangyi(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.config = ReadConfig()
        self.resultmethod = RequestMethod()
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        self.case_name =str('第三方网易云分销图书渠道接口')
        self.s = requests.session()
        data = {
            "username": "sysadmin",
            "password": "e1638ef8e5bbd0604032539aedfeb60d",
            "token": "G6gIVRMah9nWwiJQq5AsFZEcP4kvSUmejN"
        }
        self.session = self.s.post('http://www.cmread.com/adminwx/user/login/check', data=data)
        print(self.session.text)

    def tearDown(self):
        pass

    def test_002_01(self):
        res = self.s.get("http://www.cmread.com/adminwx/api/wangyi/getBookChapters/14707344552912")
        result = res.text.find('lastId')
        self.assertEqual(result, 29)
        print(res.text)
        self.case_name = str("第三方网易云分销图书渠道接口")
        self.log.logger.info(self.case_name + " - Code:第一个'lastId'-的索引是--" + str(result) + '--------成功')

    def test_002_02(self):
        res = self.s.get("http://www.cmread.com/adminwx/api/wangyi/getBookInfo/15082115169596")
        result = res.text.find('200')
        self.assertEqual(result, 8)
        self.case_name = str("网易—获取图书信息接口")
        self.log.logger.info(self.case_name + " - Code:状态码'200'-的索引是--" + str(result) + '--------成功')
