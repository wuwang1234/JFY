import multiprocessing
import time


def send(p):
    data = [1,2,3,4,5,6,7,8]
    p.put(data)
    time.sleep(1)



def receive(p):
    while True:
        data = p.get(True)
        print(data)


if  __name__=='__main__':
    p = multiprocessing.Queue()
    pw = multiprocessing.Process(target=send,args=(p,))
    pr = multiprocessing.Process(target=receive, args=(p,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
