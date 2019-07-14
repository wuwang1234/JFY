def get_data():
    '''利用生成器yield读取大容量数据的文件'''
    with open('E:\迅雷下载\王p保镖.mp4', errors='ignore') as f:
        # errors='ignore'表示忽视读取文件时的UnicodeDecodeError
        while True:
            data = f.readlines(10240)
            if data:
                yield data
            else:
                break


# count = 0
# for e in get_data():
#     print(count)
#     print(e)
#     count += 1


def print_directory_contents(sPath):
    '''

    :param sPath: 接受一个文件夹路径
    :return:打印该文件夹下所有文件
    '''
    import os
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)


# print_directory_contents('E:\迅雷下载')

# a = [1,2,3]
# print('%s id is :%s'%(a,id(a)))
# b = a[:1]
# print('%s id is :%s'%(b,id(b)))
# a[0]=8
# print('%s id is :%s'%(b,id(b)))
# c= [[1,2],3,4,5]
# d = c[:2]
# print('%s id is :%s'%(c,id(c)))
# print('%s id is :%s'%(d,id(d)))
# c[0].append(3)
# print('%s id is :%s'%(d,id(d)))

def dayofyear():
    import datetime
    year = input('请输入年份')
    month = input('请输入月份')
    day = input('请输入天')
    date1 = datetime.date(year=int(year), month=int(month), day=int(day))
    date2 = datetime.date(year=int(year), month=1, day=1)
    return (date1 - date2).days + 1


# print(dayofyear())

import os
import sys

print(os.path)
print(sys.path)
