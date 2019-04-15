import datetime
import time


def new_data():
    h1 = int(time.mktime(datetime.datetime.now().timetuple()))
    return h1


def one_data():
    h2 = int(time.mktime(datetime.date(datetime.date.today().year,datetime.date.today().month,1).timetuple()))
    return h2


if __name__ == '__main__':
    ss = new_data()
    print(ss)