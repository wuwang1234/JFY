def binary_search(alist, item):
    '''二分查找递归实现'''
    n = len(alist)

    if n > 0:
        mid = n // 2
        if item == alist[mid]:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)
        elif item > alist[mid]:
            return binary_search(alist[mid + 1:], item)
        else:
            return False


def binary_search_2(alist, item):
    '''二分查找非递归实现'''
    n = len(alist)
    first = 0
    last = n - 1

    while first <= last:
        mid = (first + last) // 2
        if item == alist[mid]:
            return True
        elif item < alist[mid]:
            last = mid - 1
        elif item > alist[mid]:
            first = mid + 1
        else:
            return False


alist = [1, 2, 3, 4, 5, 6, 7, 8]
print(binary_search_2(alist, 6))
