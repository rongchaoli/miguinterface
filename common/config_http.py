#!/usr/bin/python
# coding=utf-8

import configparser as cparser
# from common.config_json import OperetionJson
import requests
import os

# ------------------读取配置文件----------------------
base_path = str(os.path.dirname(os.path.dirname(__file__)))
base_path = base_path.replace('\\', '/')
cfg_path = base_path + '/config.ini'
cf = cparser.ConfigParser()
cf.read(cfg_path, encoding='utf-8')


class RequestMethod:
    """ 定义请求类型 """

    def __init__(self):
        """初始化参数"""
        self.base_url = cf.get('URL', 'base_url')
        self.files = {}
        self.params = {}

    def get_inter(self, params):
        return cf.get('URL', 'base_url')+cf.get('interface', params)

    def get_header(self, header):
        return cf.get('HEADER', header)

    def get_in(self,url):
        """
        定义获取地址信息
        :return:
        """
        test_url = self.get_inter(url)
        return test_url

    def get(self, url):
        """
        定义get方法请求
        :return:
        """
        test_url = self.get_inter(url)
        try:
            return requests.get(url=test_url, params=None, timeout=60)
        except TimeoutError:
            return print('%s get request timeout!' % url)

    def post(self, url, params):
        """
        定义post方法请求
        :return:
        """
        header = self.get_header(params)
        try:
            return requests.post(url=self.base_url, data=header, timeout=60)
        except TimeoutError:
            return print('%s post request timeout!' % url)

    def post_with_file(self, url, fp):
        """
        定义post方法请求
        :return:
        """
        test_url = self.base_url + url
        file = {
            'head_img': open(fp, 'rb')
        }
        try:
            return requests.post(url=test_url, files=file, timeout=60)
        except TimeoutError:
            return print('%s post request timeout!' % url)


if __name__ == '__main__':
    RequestMethod = RequestMethod()
    i = RequestMethod.inter('url_001')
    print(i)