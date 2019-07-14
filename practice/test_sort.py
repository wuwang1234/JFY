import random
import math

data = [100, 1, 2, 8, 3, 1, 6, 11, 55, 66, 44, 33, 18, 18, 17, 16, 0, 23, 7, 9]


def sort01(data):
    for j in range(data.__len__() - 1):
        for i in range(data.__len__() - j - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
    return data


print(sort01(data))


def sort02(data02):
    min = ''
    for j in range(data02.__len__() - 1):
        # 第j次循环假设第j个元素就是本次循环的最小值，注意这块记录的是下标的值
        min_index = j
        for i in range(j + 1, data02.__len__()):
            # 内层循环从j+1开始，把第j个元素与j+1开始到最后一个元素进行比较
            if data02[i] < data02[min_index]:
                # 注意这块比较的最小值是实时跟新的，即min_index始终是比较的最小值的下表
                min_index = i
        # 注意这个交换 要放到循环外，循环退出后min_index就是本轮循环最小值的下标
        data02[min_index], data02[j] = data02[j], data02[min_index]
    return data02


data02 = []
for i in range(30):
    data02.append(random.randint(0, 100))
print(data02)
print(sort02(data02))


def sort03(data03):
    # 每次循环插入一个元素，需要插入n-1个元素
    # 从第索引为1的元素开始插入，到最后一个元素,元素索引为len(data)-1
    for j in range(1, data03.__len__()):
        # 前面已经有序的序列是j个,索引为的元素与前面元素比较
        for i in range(j,0,-1):
            if data03[i] < data03[i-1]:
                data03[i-1], data03[i] = data03[i], data03[i-1]
    return data03


data03 = []
for i in range(10):
    data03.append(random.random())
print('data3',end='')
print(data03)
print(sort03(data03))


def sort04(data04):
    gap = len(data04) // 2
    # 进行插入
    while gap >= 1:
        for j in range(gap, data04.__len__()):
            i = j
            while i > 0:
                # 感觉有点想冒泡，让插入的元素，以gap间距向左移动到合适位置
                if data04[i] < data04[i - gap]:
                    data04[i], data04[i - gap] = data04[i - gap], data04[i]
                    # print(data04)
                    i -= gap
                # 注意必须要加break，不加的话会陷入死循环
                # 找到位置后跳出循环
                else:
                    break

        gap = gap // 2
    return data04


def sort05(data04):
    gap = len(data04) // 2
    # 进行插入
    while gap >= 1:
        # 和插入排序一样，还是表示要插入的元素
        for j in range(gap, data04.__len__()):
            # 表示在已排序元素插入的过程。
            # 当前要插入的元素下标是j，前面已经排序的元素索引
            # 是j-gap，j-2gap.....到j-n*gap,j-n*gap的值即j % gap，
            #   它表示子序列的第一个值
            for i in range(j,j % gap ,-gap):
                if data04[i] < data04[i - gap]:
                    data04[i], data04[i - gap] = data04[i - gap], data04[i]
        gap = gap // 2
    return data04


data04 = []
for i in range(10):
    data04.append(random.random())
print(data04)
print(sort04(data04))
print(sort05(data04))


# def quick_sort(data05, first, last):
#     if first >= last:
#         return
#     medium_value = data05[first]
#     min_value = first
#     max_value = last
#     # 当最小值和最大值相遇的时候终止循环
#     while max_value > min_value:
#         '''
#         需要解决的问题
#         移动原则：最小值指针指向元素小于中间值元素，最大值指向的元素大于中间值元素。
#         当两个指针都停止移动的时候交换
#         1、刚开始移动的是第一个元素：最小值指针指向的是中间值，我们将中间值抽出来，
#         则现在最小值指向元素为空，所以不能移动最小值指针，所以先移动最大值指针
#         2、若最大值大于中间值那么指针一直移动
#         3、若最大值小于或者等于中间值，我们这里采取的策略是让所有的与中间值相等的元素都放到左边
#         所以这个时候是停止移动
#         4、交换最大值指针和最小值指针对应元素
#         5、由于最大值指针对应元素为空，此时可以移动最小值指针
#         6、若最小值小于或者等于中间值那么指针一直移动
#         7、当最小值大于中间值元素的时候停止移动交换
#         8、交换后最大值指针对应元素大于中间值元素，最小值指针指向是空
#         9、此时要跳到步骤2继续执行，我们使用循环
#         10、考虑一下最大值指针的最小值指针相遇的情况，也就是最大值指针和最小值指针差1
#         此时有3种情况
#             情况1：
#             最大值指针指向元素大于最小值指针指向元素，移动最大值指针：
#             移动后max_value=min_value，此时应该直接退出循环
#             最大值指针指向元素大于最小值指针指向元素，移动最小值指针：
#             移动后max_value=min_value，此时应该直接退出循环
#             情况2：
#             最大值指针指向元素小于最小值指针指向元素，此时交换元素，交换后移动调到情况1
#             情况3：
#             最大值指针指向元素等于最小值指针指向元素，此时若最大值指针移动，让移动停止。
#             让最小值元素指针移动
#         '''
#         while max_value > min_value and data05[max_value] > medium_value:
#             # 当最大值指针指向的值大于中间值的话一直往左移动
#             max_value -= 1
#         if data05[max_value] < data05[min_value]:
#             # 加这个if条件主要解决当最大值指针和最小值指针差1的情况
#             data05[min_value], data05[max_value] = data05[max_value], data05[min_value]
#         while max_value > min_value and data05[min_value] <= medium_value:
#             # 当最小值指针指向的值小于中间值的话一直往右移动
#             min_value += 1
#         if data05[max_value] < data05[min_value]:
#             data05[min_value], data05[max_value] = data05[max_value], data05[min_value]
#     print(medium_value)
#     # 不能这样操作，因为要操作原有列表对象，下面这种方式是新列表，的而不是新的列表
#     # quick_sort(data04[:min_value-1])
#     # quick_sort(data04[min_value+1:])
#     quick_sort(data05, 0, min_value - 1)
#     quick_sort(data05, min_value + 1, last)
#
#
# data05 = []
# for i in range(6):
#     data05.append(random.random())
# print(data05)
# quick_sort(data05, 0, len(data05) - 1)
# print(data05)


# def merge_sort(alist):
#     n = len(alist)
#     if n <= 1:
#         return alist
#     mid = n // 2
#     left = merge_sort(alist[:mid])
#     right = merge_sort(alist[mid:])
#     left_point, right_point = 0, 0
#     result = []
#     while left_point < len(left) and right_point < len(right):
#         if left[left_point] < right[right_point]:
#             result.append(left[left_point])
#             left_point += 1
#         else:
#             result.append(right[right_point])
#             right_point += 1
#     result += left[left_point:]
#     result += right[right_point:]
#     return result
#
#
# alist = []
# for i in range(6):
#     alist.append(random.random())
# print(alist)
# sort_alist = merge_sort(alist)
# print(sort_alist)
