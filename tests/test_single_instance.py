class SingleInstance(object):
    '''单例模式实现'''

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingleInstance, cls).__new__(cls)
        return cls.instance


aa = SingleInstance()
bb = SingleInstance()
print(id(aa))
print(id(bb))


class Fibltertor(object):
    '''
    :param:n 产生多少个
    :return 返回一个序列
    '''

    def __init__(self, n):
        self.n = n
        self.fibl = [1, 2]

    def gene_list(self):
        for i in range(self.n - 2):
            tem = self.fibl[-2] + self.fibl[-1]
            self.fibl.append(tem)
        return self.fibl


test = Fibltertor(10)
print(test.gene_list())


class Fibltertor2(object):
    def __init__(self, n):
        self.n = n
        self.current = 0
        self.num1 = 1
        self.num2 = 2

    def __next__(self):
        if self.current < self.n:
            num = self.num1
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            self.current += 1
            return num
        else:
            raise StopIteration

    def __iter__(self):
        return self


iter = Fibltertor2(10)
for i in iter:
    print(i)

L2 = [1, 2, 3, 5, 4, 6, 1, 2, 3, 8, 9, 10]
L1 = []
[L1.append(i) for i in L2 if i not in L1]
print(L1)


def test(fun):
    def inner_fun(*args,**kwargs):
        print(args)
        print(kwargs)
        fun(*args,**kwargs)
    return inner_fun
@test
def aaaa(*args,**kwargs):
    print(args)
    print(kwargs)
    print('test')

print(aaaa(1,2,3,age=10,gender=1))