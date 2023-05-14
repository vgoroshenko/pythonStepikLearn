# from time import monotonic, sleep
#
# def calculate_it(fnc, *args):
#     st_time = monotonic()
#     tmp = fnc(*args)
#     end_time = monotonic()
#     return (tmp, end_time - st_time)
#
# def add(a, b, c):
#     sleep(3)
#     return a + b + c
#
# print(calculate_it(add, 1, 2, 3))

from time import monotonic, sleep
from math import factorial

def get_the_fastest_func(fnc, arg):
    min_time = 0
    tmp_fnc =  fnc[0]
    for i in fnc:
        st_time = monotonic()
        i(arg)
        end_time = monotonic()
        tmp = end_time - st_time
        print(min_time, 'min')
        print(tmp, 'время выполнения программы')
        print('-----')
        if fnc[0] == i:
            min_time = tmp
            tmp_fnc = i
            continue
        if tmp < min_time or tmp == 0.0:
            min_time = tmp
            tmp_fnc = i
    return tmp_fnc


def asd (n):
    return factorial(n)

def factorial_recurrent(n):                  # рекурсивная функция
    if n == 0:
        return 1
    return n * factorial_recurrent(n - 1)


def factorial_classic(n):                    # итеративная функция
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

funcs = [factorial_classic, factorial_recurrent, factorial]

q = get_the_fastest_func(funcs, 900)
print(q)
# print(q(3))