import sys

a = 1
print(sys.getsizeof(a))  # 28byte
b = 'a'
print(sys.getsizeof(b))  # 50byte

list01 = []
print(list01.__sizeof__())

list02 = [1, 2]
print(list02.__sizeof__())

list03 = [1, 2, 3]
# 列表初始化分配的元素是：40字节+列表中每个元素占用的内存之和
print(list03.__sizeof__())  # 64=40+8*3
list03.append(4)
# 增加元素需要扩内存空间采用的策略是倍增
print(list03.__sizeof__())  # 96
list03.append(5)
print(list03.__sizeof__())  # 96
list03.append(list02)
print(list03.__sizeof__())


class stack(object):
    # def __new__(cls, *args, **kwargs):
    #     cls.__new__(list)
    def __init__(self):
        self.__list = []

    def push(self, item):
        self.__list.append(item)

    def pop(self):
        self.__list.pop()

    def peek(self):
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        if self.__list:
            return False
        else:
            return True

    def size(self):
        return self.__list.__len__()


class Node(object):
    def __init__(self, elem):
        self.element = elem
        self.next = None


class DoubleNode(object):
    def __init__(self, elem):
        self.element = elem
        self.next = None
        self.pre = None


class SingleLinkList(object):
    '''单链表实现'''

    def __init__(self, node=None):
        # 初始化链表，若不传入节点的值则默认值设置为None
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        curl = self.__head
        count = 0
        # while True:
        #     if curl or curl.next == None:
        #         break
        #     else:
        #         count += 1
        #         curl = curl.next
        while curl is not None:
            count += 1
            curl = curl.next
        return count

    # 遍历整个节点
    def travel(self):
        # 游标，用来移动遍历整个链表
        curl = self.__head
        while curl is not None:
            print(curl.element, end=' ')
            curl = curl.next
        print('')

    def add(self, item):
        # 先改变新节点指向，保证原链表关系不打断
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        node = Node(item)
        curl = self.__head
        if curl:
            while curl.next != None:
                curl = curl.next
            curl.next = node
        else:
            self.__head = node

    def insert(self, posi, item):
        '''在固定位置插入指定节点
        :param posi 插入位置，从0开始
        '''
        curl = self.__head
        node = Node(item)
        count = 0
        if posi <= 0:
            self.add(item)
        elif posi > self.length() - 1:
            self.append(item)
        else:
            while count < posi - 1:
                count += 1
                curl = curl.next
            node.next = curl.next
            curl.next = node

    def remove(self, item, flag=False):
        '''删除指是指定节点
        :param flag 这个删除item所有节点
        '''
        pre = None
        curl = self.__head
        while curl != None:
            # 删除头元素
            if curl.element == item and pre is None:
                self.__head = curl.next
                if flag:
                    # 注意这块如果要继续往下走，要改变curl的指向
                    curl = curl.next
                else:
                    break
            elif curl.element == item and pre:
                pre.next = curl.next
                if flag:
                    # 注意这块如果要继续往下走，要改变curl的指向
                    curl = curl.next
                else:
                    break
            else:
                pre = curl
                curl = curl.next

    def search(self, item):
        '''在链表中查找指定节点'''
        curl = self.__head
        count = 0
        while curl:
            if curl.element == item:
                return True
            else:
                count += 1
                curl = curl.next
        return False


class SingleCycleLinkList(object):
    '''单链表循环实现
    测试的时候考虑空链表、链表中只有一个元素
    '''

    def __init__(self, node=None):
        # 初始化链表，若不传入节点的值则默认值设置为None
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        curl = self.__head
        count = 1
        while True:
            if curl is None:
                count = 0
                break
            if curl and curl.next == self.__head:
                break
            else:
                count += 1
                curl = curl.next
        return count

    # 遍历整个节点
    def travel(self):
        # 游标，用来移动遍历整个链表
        curl = self.__head
        if self.is_empty():
            return
        while curl.next != self.__head:
            print(curl.element, end=' ')
            curl = curl.next
        print(curl.element)

    def add(self, item):
        # 先改变新节点指向，保证原链表关系不打断
        node = Node(item)
        curl = self.__head
        if curl is None:
            # 链表为空的情况
            self.__head = node
            self.__head.next = node
        else:
            node.next = self.__head
            while curl.next != self.__head:
                curl = curl.next
            # 退出循环后，游标指向尾节点
            curl.next = node
            self.__head = node

    def append(self, item):
        node = Node(item)
        curl = self.__head
        if curl:
            while curl.next != self.__head:
                curl = curl.next
            curl.next = node
            node.next = self.__head
        else:
            self.__head = node
            node.next = node

    def insert(self, posi, item):
        '''在固定位置插入指定节点
        :param posi 插入位置，从0开始
        '''
        curl = self.__head
        node = Node(item)
        count = 0
        if posi <= 0:
            self.add(item)
        elif posi > self.length() - 1:
            self.append(item)
        else:
            while count < posi - 1:
                count += 1
                curl = curl.next
            node.next = curl.next
            curl.next = node

    def remove(self, item):
        '''删除指是指定节点
        '''
        if self.is_empty():
            return
        curl = self.__head
        pre = None
        # 循环无法处理尾节点
        while curl.next != self.__head:
            if curl.element == item:
                if curl == self.__head:
                    # 删除头元素
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = curl.next
                    rear.next = curl.next
                else:
                    # 删除中间元素
                    pre.next = curl.next
                # 注意这块不能用break，只用break程序还会执行
                # 循环体外面的程序语句，会报错
                return
            else:
                pre = curl
                curl = curl.next
        # 退出循环，处理尾节点
        if curl.element == item:
            if curl == self.__head:
                self.__head = None
            else:
                pre.next = curl.next

    def search(self, item):
        '''在链表中查找指定节点'''
        curl = self.__head
        count = 0
        if self.is_empty():
            return False
        while curl.next != self.__head:
            if curl.element == item:
                return True
            else:
                count += 1
                curl = curl.next
        # 退出循环，游标指向尾节点。
        # 没有判断尾节点的元素值，需要另加判断
        if curl.element == item:
            return True
        return False

class DoubleLinkList(object):
    '''双链表实现'''

    def __init__(self, node=None):
        # 初始化链表，若不传入节点的值则默认值设置为None
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        curl = self.__head
        count = 0
        # while True:
        #     if curl or curl.next == None:
        #         break
        #     else:
        #         count += 1
        #         curl = curl.next
        while curl is not None:
            count += 1
            curl = curl.next
        return count

    # 遍历整个节点
    def travel(self):
        # 游标，用来移动遍历整个链表
        curl = self.__head
        while curl is not None:
            print(curl.element, end=' ')
            curl = curl.next
        print('')

    def add(self, item):
        # 先改变新节点指向，保证原链表关系不打断
        node = DoubleNode(item)
        self.__head.pre = node
        node.next = self.__head
        self.__head = node

    def append(self, item):
        node = DoubleNode(item)
        curl = self.__head
        if curl:
            while curl.next is not None:
                curl = curl.next
            curl.next = node
            node.pre = curl
        else:
            self.__head = node

    def insert(self, posi, item):
        '''在固定位置插入指定节点
        :param posi 插入位置，从0开始
        '''
        curl = self.__head
        node = DoubleNode(item)
        count = 0
        if posi <= 0:
            self.add(item)
        elif posi > self.length() - 1:
            self.append(item)
        else:
            while count < posi - 1:
                count += 1
                curl = curl.next
            node.next = curl.next
            node.pre = curl
            curl.next = node
            curl.next.pre = node

    def remove(self, item, flag=False):
        '''删除指是指定节点
        :param flag 这个删除item所有节点
        测试的时候考虑空链表、单节点链表、多节点链表
        考虑删除首节点、尾节点、中间节点
        '''
        curl = self.__head
        while curl != None:
            # 删除头元素
            if curl.element == item and curl.pre is None:
                self.__head = curl.next
                # 判断链表是否只有一个节点
                if curl.next:
                    curl.next.pre = None
                if flag:
                    # 注意这块如果要继续往下走，要改变curl的指向
                    curl = curl.next
                else:
                    break
            elif curl.element == item:
                curl.pre.next = curl.next
                # 判断是否是尾节点
                if curl.next:
                    curl.next.pre = curl.pre
                if flag:
                    # 注意这块如果要继续往下走，要改变curl的指向
                    curl = curl.next
                else:
                    break
            else:
                curl = curl.next

    def search(self, item):
        '''在链表中查找指定节点'''
        curl = self.__head
        count = 0
        while curl:
            if curl.element == item:
                return True
            else:
                count += 1
                curl = curl.next
        return False


if __name__ == '__main__':
    # s = stack()
    # print(s.size())
    # print(s.peek())
    # s.push(58)
    # print(s.size())
    # print(s.peek())
    # s.push(22)
    # s.push(65)
    # s.push(25)
    # s.pop()
    # s.pop()
    # print(s.peek())

    # single = SingleLinkList()
    # print(single.is_empty())
    # print(single.length())
    # single.travel()
    # single.append(5)
    # single.travel()
    # print(single.is_empty())
    # print(single.length())
    # single.add(55)
    # single.append(1)
    # single.append(2)
    # single.append(3)
    # single.append(4)
    # single.travel()
    # single.insert(0, 'a')
    # single.insert(100, 'b')
    # single.insert(-100, '-1')
    # single.travel()
    # print(single.length())
    # print(single.search(55))
    # print(single.search(555))
    # single.append(5)
    # single.append(55)
    # single.travel()
    # single.remove(5)
    # single.travel()
    # single.remove(54)
    # single.travel()
    # single.add(-1)
    # single.travel()
    # single.remove(-1)
    # single.travel()

    single = SingleCycleLinkList()
    print(single.is_empty())
    print(single.length())
    single.travel()
    single.append(5)
    single.travel()
    print(single.is_empty())
    print(single.length())
    single.add(55)
    single.append(1)
    single.append(2)
    single.append(3)
    single.append(4)
    single.travel()
    single.insert(0, 'a')
    single.insert(100, 'b')
    single.insert(-100, '-1')
    single.travel()
    print(single.length())
    print(single.search(55))
    print(single.search(555))
    single.append(5)
    single.append(55)
    single.travel()
    single.remove(5)
    single.travel()
    single.remove(54)
    single.travel()
    single.add(-1)
    single.travel()
    single.remove(-1)
    single.travel()
    single.remove(55)
    single.travel()
    single.remove(55)
    single.travel()
