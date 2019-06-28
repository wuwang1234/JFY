import threading
import time

def music(n):
    for i in range(n):
        print('this is music method;number is %s'%i)
        time.sleep(1)


def dance(n):
    for i in range(n):
        print('this is dance method;number is %s'%i)
        print('the thread name is %s'%threading.Thread.getName(t2))
        print('time is %s'%time.ctime())
        time.sleep(1)

# 有了GIL全局锁，线程间访问全局变量还是需要同步
total = 0
def add():
    global total
    for i in range(1000000):
        total += 1

def desc():
    global total
    for i in range(1000000):
        total -= 1


thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)

t1 = threading.Thread(target=music,name='music', args=(20,))
t2 = threading.Thread(target=dance,name='dance', args=(10,))
t2.setName('dance02')

if __name__ == '__main__':
    # t1.setDaemon(True)
    # t2.setDaemon(True)
    t1.start()
    # t1.join()
    t2.start()
    print(t1.isDaemon())
    # time.sleep(20)
    print(threading.Thread.is_alive(t1))  #True
    print(threading.Thread.is_alive(t2))  #False

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(total)
