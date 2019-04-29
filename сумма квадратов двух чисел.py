def square(n):    # возведение в квадрат
    return n**2


def sum_sq(a, b): # сложение квадратов
    return square(a) + square(b)


def sorter(elem): # сортировочка
    elem = list(elem)
    elem.sort()
    elem.reverse()
    return elem[0], elem[1]


def fn(*elem):    # результирующая функция
    elem = sorter(elem)
    return sum_sq(elem[0], elem[1])


print(fn(3,1,2,4))

