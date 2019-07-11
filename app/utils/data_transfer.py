import time


def time_transfer(timeStamp):
    timeArray = time.localtime(float(timeStamp))
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return str(otherStyleTime)
