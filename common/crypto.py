#!/usr/bin/python
# coding=utf-8

import hmac
import base64
import hashlib
import time


class Encryption:

    def __init__(self):
        # 密码加密参数：key:秘钥、iv:偏移
        self.aes_key = 'COHeJfoWQgaYBuna'
        self.aes_iv = '5075428636499153'
        # 接口公共参数
        self.params = dict()
        self.params['app_key'] = 'FEF2whL31DJ+awKR/JmQ3A=='
        self.params['version'] = '2.0'
        self.params['time'] = time.time()

    def aspire_aes_crypt(self, passwd):
        chapterId = 'migu'
        """
        用户密码加密算法（key，iv，passwd输入均应为bytes类型）
        :param passwd: 密码
        :return: 返回base64加密后的password
        """
        '''
                String str1 = MD5(chapterId + ”#” + identity + ”#” + 密钥, “UTF-8”);
                String str2 = MD5(随机值str + ”#” + str1, “UTF-8”);
                sign=str2;

                :return:
                '''
        sign = hashlib.md5()
        ln = sign(chapterId+'#')

    def sign(self, params):
        """
        计算签名
        :return:
        """
        lst = []
        for x in sorted(params.keys()):
            lst.append('%s=%s' % (x, params[x]))
        s = '&'.join(lst)
        key = '<#*+*Aspire*+*#>'
        return base64.b64encode(hmac.new(key.encode('utf-8'), s.encode('utf-8'), hashlib.sha1).digest())


if __name__ == '__main__':

    pwd = '332561'
    pwd_crypt = Encryption().aspire_aes_crypt(pwd)
    print(pwd_crypt)
