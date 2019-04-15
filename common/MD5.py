import hashlib
import random,string


def my_md5(s, salt=''):
    s = s+salt
    news = str(s).encode()
    m = hashlib.md5(news)
    return m.hexdigest()


def genRandomS(slen=34):
    return ''.join(random.sample(string.ascii_letters + string.digits, slen))


str1 = my_md5("WX0320wx!@#")
str2 = my_md5('aIg'+'#'+str1)
ste = genRandomS()
print(str1)
print(ste)
