import time
import multiprocessing
import threading


class IOTask():

    '''
    模拟IO密集型场景
    使用场景：常用的文件相关操作
    '''

    def __init__(self):
        print('init task')

    def threading_task01(self,flag,task, n):
        print(task)
        with open('%s.txt'%task,'a+') as OF:
            for i in range(n):
                # 调用write函数直接写到文件中，没有缓冲区，不会出现内容混乱的问题
                OF.write('%s number %s \n'%(flag,i))
        time.sleep(20)


class NetTask():
    '''
    模拟网络请求密集型任务。
    使用场景：模拟多用户同时访问服务端
    用flask框架搭建的WEB服务器采用的是有客户端请求进来就会新建一个线程来进行处理。
    '''
    pass


class CalculateTask():
    '''
    模拟计算密集型任务
    使用场景：图像处理、算法处理
    '''
    pass


if __name__ == '__main__':
    print('begin  to start tasks and compute time')
    incheng = multiprocessing.Pool(5)
    print('please input the number of process: ')
    inputNumberOfProcess = input()
    n = int(inputNumberOfProcess)
    start_time = time.time()
    for m in range(n):
        incheng.apply_async(IOTask().threading_task01,args=('thread',m,10))
    incheng.close()
    incheng.join()
    end_time = time.time()
    print('the time of  file:write is %s'%(end_time-start_time))

    start_time = time.time()
    thread_list = []
    for m in range(n):
        t = threading.Thread(target=IOTask().threading_task01,args=('thread',m,10))
        thread_list.append(t)
    for t in thread_list:
        t.start()
        # t.join()
    print('aaa')
    end_time = time.time()
    print('the time of  file:write is %s' % (end_time - start_time))
    print('all task ending')