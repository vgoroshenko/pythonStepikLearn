# def sample_decorator(func):          # определяем декоратор
#     def wrapper():
#         print('Начало функции')
#         func()
#         print('Конец функции')
#     return wrapper
#
# @sample_decorator                    # декорируем функцию
# def say():
#     print('Привет Мир!')
#
# say()


# def bold(func):
#     def wrapper():
#         return '<b>' + func() + '</b>'
#     return wrapper
#
# def italic(func):
#     def wrapper():
#         return '<i>' + func() + '</i>'
#     return wrapper
#
#
# @bold
# @italic
# def greet():
#     return 'Hello world!'
#
# print(greet())


# def sandwich(func):
#     def tmp(*args, **kwargs):
#         print('---- Верхний ломтик хлеба ----')
#         tmp = func(*args, **kwargs)
#         print('---- Нижний ломтик хлеба ----')
#         return tmp
#     return tmp
#
#
# @sandwich
# def counter(*args, **kwargs):
#     for i in args + tuple(kwargs.keys()) + tuple(kwargs.values()):
#         print(i)
#
# counter(10, 20, 30, sep='40', end='!!!', step='beegeek')



# def new_print(func):
#     def tmp(*args, **kwargs):
#         args = map(lambda x: x.upper() if not str(x).isdigit() else x, args)
#         kwargs = {k: v.upper() for k, v in kwargs.items()}
#         func(*args, **kwargs)
#     return tmp
#
# print = new_print(print)
#
#
# print('hi', 'there', end='!')
# print('are you in trouble?')
# print(111, 222, 333, sep='xxx')


# def do_twice(func):
#         def tmp(*args, **kwargs):
#             func(*args, **kwargs)
#             return func(*args, **kwargs)
#
#         return tmp
#
#
# @do_twice
# def beegeek():
#     print('beegeek')
#
#
# print(beegeek())


# def reverse_args(func):
#     def tmp(*args, **kwargs):
#         return func(*args[::-1], **kwargs)
#     return tmp
#
#
# @reverse_args
# def operation(a, b, value=10):
#     return a // b - value
#
# print(operation(70, 70, value=70))



# def exception_decorator(func):
#     def tmp(*args, **kwargs):
#         try:
#             return func(*args, **kwargs), 'Функция выполнилась без ошибок'
#         except:
#             return None, 'При вызове функции произошла ошибка'
#     return tmp
#
#
#
# @exception_decorator
# def f(x):
#     return x ** 2 + 2 * x + 1
#
#
# print(f(7))
#
# sum = exception_decorator(sum)
#
# print(sum(['199', '1', 187]))
#
#
# @exception_decorator
# def f(*args, **kwargs):
#     return sum(args) + sum(kwargs.values())
#
#
# print(f(1, 2, 3, param1=4, param2=10))


def takes_positive(func):
    def tmp(*args, **kwargs):
        print((*args, *kwargs.values()))
        if any(map(lambda x: isinstance(x, float), (*args, *kwargs.values()))):
            raise TypeError
        elif any(map(lambda x: x <= 0, (*args, *kwargs.values()))):
            raise ValueError
        return func(*args, **kwargs)
    return tmp

@takes_positive
def positive_sum(*args):
    return sum(args)

try:
    print(positive_sum(11, 20.1, 10))
except Exception as err:
    print(type(err))


@takes_positive
def positive_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, par1=1, sep=4))


@takes_positive
def positive_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


try:
    print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, par1=1, sep=-40))
except Exception as err:
    print(type(err))
