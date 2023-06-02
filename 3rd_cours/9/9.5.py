# def make_adder(n):
#     def add(x):
#         return x + n
#     return add
#
# plus_3 = make_adder(3)
#
# print(plus_3(10), plus_3(100))



# def outer(x):
#     y = 20
#     def inner(z):
#         t = 30
#         return x + y + z + t
#     return inner
#
# func = outer(10)
# qwd = func(12)
#
# for var in func.__closure__:
#     print(var.cell_contents)


# def power(degree):
#     def tmp(x):
#         return x**degree
#     return tmp
#
# result = power(4)(2)
# print(result)



# def generator_square_polynom(a, b, c):
#     def tmp(x):
#         return a*(x**2) + b * x + c
#     return tmp
#
# print(generator_square_polynom(9, 52, 64)(8))


# def sourcetemplate(url):
#     def tmp(**kwargs):
#         if len(kwargs) == 0:
#             return url
#         else:
#             return url + '?' + '&'.join([f'{k}={v}' for k, v in sorted(kwargs.items())])
#     return tmp
#
#
# url = 'https://beegeek.ru'
# load = sourcetemplate(url)
# print(load(name='timur'))
#
#
# url = 'https://stepik.org/lesson/651459/step/14'
# load = sourcetemplate(url)
# print(load(thread='solutions', unit=648165))
#
#
# url = 'https://beegeek.ru'
# load = sourcetemplate(url)
# print(load())
#
# url = 'https://all_for_comfort_life.com'
# load = sourcetemplate(url)
# print(load(smartphone='iPhone', notebook='huawei', sale=True))

# from datetime import date
#
#
# d = {'ru': '%d.%m.%Y',
#      'us': '%m-%d-%Y',
#      'ca': '%Y-%m-%d',
#      'br': '%d/%m/%Y',
#      'fr': '%d.%m.%Y',
#      'pt': '%d-%m-%Y',}
#
# def date_formatter(country_code):
#     def tmp(today):
#         return today.strftime(d[country_code])
#     return tmp
#
#
# date_ru = date_formatter('ca')
# today = date(2015, 12, 7)
# print(date_ru(today))

#print(date(2022, 1, 25))


def sort_priority(values, group):
    pass






