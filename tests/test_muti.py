import time
import multiprocessing
import threading

n = 0


def change():
    global n
    n = n + 1
    time.sleep(2)
    print(n)
    n = n - 1
    print('output %s' % n)


def work():
    global n
    for i in range(10000):
        change()
        print(i)


class FunWork(multiprocessing.Process):

    def __init__(self):
        multiprocessing.Process.__init__(self)
        print('begin')

    def run(self):
        for i in range(100):
            time.sleep(1)
            print('end %s' % i)


if __name__ == '__main__':
    # 方式1，实例化multiprocessing的Process类
    # p1 = multiprocessing.Process(target=work)
    # p2 = multiprocessing.Process(target=work)
    # p1.start()
    # p2.start()
    # print(n)  # 0

    # 方式2：定义类，继承Process.
    # 注意要重写run方法，在init初始化方法中调用父类的初始化方法
    # pp1 = FunWork()
    # pp2 = FunWork()
    # pp1.start()
    # pp2.start()

    t1 = threading.Thread(target=work)
    t2 = threading.Thread(target=work)
    t1.start()
    t2.start()
