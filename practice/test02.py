import keyword
print(keyword.kwlist)


def test_gen():
    i, a, b = 0, 0, 1
    while i < 1000:
        a, b = b, a+b
        yield b
        i = i + 1


aa = test_gen()
print(test_gen())
print(aa.__next__())
print(next(aa))
print(next(aa))
print(aa.__next__())
print(next(aa))
