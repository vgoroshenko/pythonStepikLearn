# import functools
# import time
#
#
# def slow_down(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         time.sleep(1)
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @slow_down
# def countdown(number):
#     if number < 1:
#         print('Конец!')
#     else:
#         print(number)
#         countdown(number - 1)
#
#
# countdown(5)

# import functools
#
# def square(func):
#     @functools.wraps(func)
#     def wrapper(*args):
#         return func(*args) ** 2
#     return wrapper
#
# @square
# def add(a, b):
#     '''прекрасная функция'''
#     return a + b
#
# print(add(1, 1))
# print(add.__name__)
# print(add.__doc__)
import functools

# def returns_string(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if isinstance(result, str):
#             return result
#         else:
#             raise TypeError
#     return wrapper
#
#
# @returns_string
# def add(a, b):
#     return a + b
#
# try:
#     print(add(3, 7))
# except TypeError as e:
#     print(type(e))

# import functools
#
# def trace(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         trace1 = f'TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}'
#         trace2 = f"TRACE: возвращаемое значение {func.__name__}(): {repr(result)}"
#         print(trace1, trace2, sep='\n')
#         return result
#     return wrapper
#
#
# @trace
# def sub(a, b, c):
#     '''прекрасная функция'''
#     return a - b + c
#
#
# print(sub.__name__)
# print(sub.__doc__)
# sub(20, 5, c=10)
#
#
# @trace
# def say(name, line):
#     return f'{name}: {line}'
#
#
# say('Jane', 'Hello, World')

# import functools
# def prefix(sting, to_the_end=False):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             return result + sting if to_the_end else sting + result
#         return wrapper
#     return decorator
#
#
# @prefix('$$$', to_the_end=True)
# def get_bonus():
#     return '2000'
#
#
# print(get_bonus())


# import functools
# def make_html(tag):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             return f'<{tag}>{func(*args, **kwargs)}</{tag}>'
#         return wrapper
#     return decorator
#
#
# @make_html('i')
# @make_html('del')
# def get_text(text):
#     return text
#
#
# print(get_text(text='decorators are so cool!'))


# import functools
#
# def repeat(times):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for i in range(1, times + 1):
#                 value = func(*args, **kwargs)
#             return value
#         return wrapper
#     return decorator
#
#
# @repeat(10)
# def add(a, b):
#     '''sum of two numbers'''
#     return a + b


# print(add.__name__)
# print(add.__doc__)
# print(add(10, b=20))


# import  functools
#
# def strip_range(start, end, char='.'):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             value = func(*args, **kwargs)
#             value = {k: v if k not in [i for i in range(start, end)] else char for k, v in enumerate(value)}
#             return ''.join([i for i in value.values()])
#         return wrapper
#     return decorator
#
#
# @strip_range(3, 5)
# def beegeek():
#     return 'beegeek'
#
#
# print(beegeek())
#
#
# @strip_range(3, 20, '_')
# def beegeek():
#     return 'beegeek'
#
#
# print(beegeek())
# @strip_range(20, 30)
# def beegeek():
#     return 'beegeek'
#
#
# print(beegeek())


# import functools
#
# def returns(datatype):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             value = func(*args, **kwargs)
#             if isinstance(value, datatype):
#                 return value
#             raise TypeError
#         return wrapper
#     return decorator
#
# @returns(int)
# def add(a, b):
#     return a + b
#
# try:
#     print(add('199', '1'))
# except TypeError as e:
#     print(type(e))

# import functools
# def takes(*type_args):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             if not all(map(lambda x: False if type(x) not in type_args else True, [*args, *kwargs.values()])):
#                 raise TypeError
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator
#
#
# @takes(int, str)
# def repeat_string(string, times):
#     return string * times
#
# print(repeat_string('bee', 3))
#
# @takes(str)
# def beegeek(word, repeat):
#     return word * repeat
#
#
# try:
#     print(beegeek('beegeek', repeat=2))
# except TypeError as e:
#     print(type(e))
#
#
# @takes(list, bool, float, int)
# def repeat_string(string, times):
#     return string * times
#
# try:
#     print(repeat_string('bee', 4))
# except TypeError as e:
#     print(type(e))


# import functools
#
# def add_attrs(**f_kwargs):
#     def decorator(func):
#         for k, v in f_kwargs.items():
#             func.__dict__[k] = v
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator
#
#
# @add_attrs(attr2='geek')
# @add_attrs(attr1='bee')
# def beegeek():
#     return 'beegeek'
#
#
# print(beegeek.attr1)
# print(beegeek.attr2)
# print(beegeek.__name__)


# import functools
#
# def ignore_exception(*f_args):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             try:
#                 value = func(*args, **kwargs)
#                 return value
#             except f_args as e:
#                 print(f'Исключение {e.__class__.__name__} обработано')
#         return wrapper
#     return decorator
#
#
# @ignore_exception(ZeroDivisionError, TypeError, ValueError)
# def f(x):
#     return 1 / x
#
#
# f(0)

import functools

class MaxRetriesException(Exception):
    pass

def retry(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            tmp_times = times
            for i in range(times):
                try:
                    value = func(*args, **kwargs)
                    break
                except:
                    tmp_times -= 1
            if tmp_times == 0:
                raise MaxRetriesException
            return value
        return wrapper
    return decorator


@retry(8)
def beegeek():
    beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
    if beegeek.calls < 5:
        raise ValueError
    print('beegeek')


beegeek()






