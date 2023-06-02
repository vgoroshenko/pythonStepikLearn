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












