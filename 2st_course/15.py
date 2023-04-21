# def matrix(n=None, m=None, value=None):
#     if n is not None and m is not None and value is not None:
#         return [[value] * m for _ in range(n)]
#     elif n is not None and m is not None:
#         return [[0] * m for _ in range(n)]
#     elif n is not None:
#         return [[0]*n for _ in range(n)]
#     else:
#         return [[0] * 1 for _ in range(1)]

# def count_args(*args):
#     return len(args)
#
# print(count_args([], (''), 'a', 12, False))

# def sq_sum(*args):
#     return sum([i ** 2 for i in args])
#
#
# print(sq_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# def mean(*args):
#     tmp = [i for i in args if type(i) == float or type(i) == int]
#     if len(tmp) != 0:
#         return sum(tmp) / len(tmp)
#     else:
#         return 0.0
#
#
# print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))


# def greet(asd, *args):
#     hello = 'Hello, '
#     if asd !='':
#         args = (asd, *args)
#     tmp = [i + ' and ' for i in args]
#     if len(args) > 0:
#         tmp[-1] = args[-1]
#     else:
#         hello = 'Hello'
#     for i in tmp:
#         hello += i
#     return hello + '!'
#
# print(greet('a'))


# def print_products(*args):
#     tmp = [i for i in args if type(i) == str and i != '']
#     if len(tmp) > 0:
#         for i in range(1, len(tmp) + 1):
#             print(f'{i}'+') ' + tmp[i - 1])
#     else:
#         print('Нет продуктов')
#
# print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)

# def info_kwargs(**kwargs):
#     for i in sorted(kwargs):
#         print(f'{i}: {kwargs[i]}')
#
# info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')


# numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]
#
# def compare(x):
#     return sum(x) / len(x)
#
# print(min(numbers, key=compare))
# print(max(numbers, key=compare))
#
# l_compare = lambda x: sum(x) / len(x)
#
# print(min(numbers, key=lambda x: sum(x) / len(x)))


# points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
#
# def compare(x):
#     return (x[0] ** 2 + x[1] ** 2) ** 0.5
# #points.sort(key=compare)
# points.sort(key=lambda x: (x[0] ** 2 + x[1] ** 2) ** 0.5)
#
# print(points)

# numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
# # def compare(x):
# #     return min(x) + max(x)
# numbers.sort(key=lambda x: min(x) + max(x))
#
# print(numbers)


# athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
# num = int(input())
# # def compare(x):
# #     return x[num - 1]
# athletes.sort(key=lambda x: x[num - 1])
#
# for i in athletes:
#     print(*i)
# import math
#
# def kvadrat(x):
#     return x ** 2
#
# comm_dict = {'квадрат': kvadrat,
#              'куб': lambda x: x ** 3,
#              'корень': lambda x: x ** 0.5,
#              'модуль': lambda x: abs(x),
#              'синус': lambda x: math.sin(x)}
# def command(x, comm):
#     return comm_dict[comm](x)
#
# num = int(input())
# comm = input()
#
# print(command(num, comm))


# nums = [tuple(int(i) for i in list(_)) for _ in input().split()]
#
# nums.sort(key=lambda x: sum(x))
#
# for i in nums:
#     print(*i, sep='', end=' ')


# def comparator(n):
#     return sum([int(i) for i in str(n)])
#
# numbers = sorted(int(i) for i in input().split())
#
# print(*sorted(numbers, key=comparator))

# def high_order_function(func, x):     # функция высшего порядка, так как принимает функцию
#     return func(x)
#
# def double(x):                     # обычная функция = функция первого порядка
#     return 2*x
#
# def add_one(x):                    # обычная функция = функция первого порядка
#     return x + 1
#
# print(high_order_function(double, 4))
# print(double(5))


# numbers = [-2, 45, 45, -7, -45, 37, -42, 27, -58, -58, -12, -27, -49, -27, -56, 4, -99, -11, 86]
#
# print(max(numbers, key=abs))


# from decimal import *
#
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
# # def round(x):
# #     print(decimal.Decimal(str(x)[0:4]))
#
# numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]
# #map(lambda x: print(Decimal(str(x)[0:4])), numbers)
# #map(lambda x: print(Decimal(x).quantize(Decimal('1.00'))), numbers)
# map(lambda x: print(round(x, 2)), numbers)

# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
# # def cub(x):
# #     print(x**3)
# #
# # def three_num(x):
# #     if len(str(x)) == 3 and x % 5 == 2:
# #         return x
#
#
# numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]
#
# #map(cub, filter(three_num, numbers))
# map(lambda x: print(x**3), filter(lambda x: len(str(x)) == 3 and x % 5 == 2, numbers))


# Напишите программу для вычисления и вывода суммы квадратов элементов списка numbers.
# def reduce(operation, items, initial_value):
#     acc = initial_value
#     for item in items:
#         acc = operation(acc, item)
#     return acc
#
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
# def kvadrat(x, y):
#     return x + y**2
#
# numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35, 11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36, 72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35, 7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]
#
# #print(reduce(kvadrat, numbers, 0))
# #print(sum(map(lambda x: x**2, numbers)))


# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
#
# numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99, 270, 219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260, -35, 152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229, 60, 254, -9, 5, 187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135, 29, 148, 242, 33, 35, 211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2, 79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234, 10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]
#
# asd = filter(lambda x: len(str(abs(x))) == 2 and x % 7 == 0, numbers)
# print(asd)
# asd = map(lambda x: x**2, asd)
# print(asd)
# asd = sum(asd)
# print(asd)
#
# print(sum(map(lambda x: x**2, filter(lambda x: len(str(abs(x))) == 2 and x % 7 == 0, numbers))))

# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result


# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
# def func_apply(func, lst):
#     return map(lambda x: func(x), lst)
#
# def add3(x):
#     return x + 3
#
# print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
# print(func_apply(str, [1, 2, 3, 4, 5, 6]))


# iterable = [1, 2, 3]
# result = list(map(len, iterable))
# print(result)

# random_list = [1, 'a', 0, False, True, '0', 7, '']
# filtered_list = list(filter(str, random_list))
# print(type(random_list[3]))
# print(filtered_list)
#
#
#
#
# print(False != None)


# from functools import reduce
#
# floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
# words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
# numbers = [4, 6, 9, 23, 5]
#
# # Исправьте этот код
# map_result = list(map(lambda num: round(num**2, 1), floats))
# filter_result = list(filter(lambda name: name if len(name) > 4 and name[::-1] == name else False, words))
# reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)
#
# print(map_result)
# print(filter_result)
# print(reduce_result)

# from functools import reduce
#
# data = [['Tokyo', 35676000, 'primary'],
#         ['New York', 19354922, 'nan'],
#         ['Mexico City', 19028000, 'primary'],
#         ['Mumbai', 18978000, 'admin'],
#         ['Sao Paulo', 18845000, 'admin'],
#         ['Delhi', 15926000, 'admin'],
#         ['Shanghai', 14987000, 'admin'],
#         ['Kolkata', 14787000, 'admin'],
#         ['Los Angeles', 12815475, 'nan'],
#         ['Dhaka', 12797394, 'primary'],
#         ['Buenos Aires', 12795000, 'primary'],
#         ['Karachi', 12130000, 'admin'],
#         ['Cairo', 11893000, 'primary'],
#         ['Rio de Janeiro', 11748000, 'admin'],
#         ['Osaka', 11294000, 'admin'],
#         ['Beijing', 11106000, 'primary'],
#         ['Manila', 11100000, 'primary'],
#         ['Moscow', 10452000, 'primary'],
#         ['Istanbul', 10061000, 'admin'],
#         ['Paris', 9904000, 'primary']]
#
# cities_filter = list(map(lambda x: x[0], filter(lambda x: 'primary' in x and x[1] > 10000000, data)))
# cities = reduce(lambda x, y: x + ', ' + y, sorted(cities_filter))
# print( 'Cities: ' + cities)


# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# result = list(filter(lambda x: True, primes))
# print(result)


# func = lambda x: x % 19 == 0 or x % 13 == 0
#
# print(func(19))

# func = lambda x: x[0].lower() == 'a' and x[-1].lower() == 'a'
#
# print(func('abcdA'))
# print('10.3'.replace('.', '1', 1).replace('-', '1', 1))

# is_non_negative_num = lambda x: x[0] != '-' and x.replace('.', '1', 1).isnumeric()
# is_num = lambda x: x.replace('.' and '-', '1', 1).isnumeric()
# #is_num = lambda x: x.replace('.', '1', 1).replace('-', '1', 1).isnumeric()
# #is_num = lambda x: lambda y: print(list(x)[y])
#
# print(is_num('10.34ab'))
# print(is_num('10.45'))
# print(is_num('-18'))
# print(is_num('-34.67'))
# print(is_num('987'))
# print(is_num('abcd'))
# print(is_num('123.122.12'))
# print(is_num('-123.122'))
# print(is_num('--13.2'))


# words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid', 'wednesday', 'able', 'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow', 'abound', 'absent', 'beware', 'abundant', 'abnormal', 'aboard', 'about', 'accelerate', 'abort', 'thursday', 'tuesday', 'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept', 'berry', 'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']
#
# new_words1 = list(filter(lambda w: len(w) == 6, sorted(words)))
# print(*new_words1)


# numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80, 93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]
# new_numbers = list(map(lambda x: x // 2 if x % 2 == 0 else x, list(filter(lambda x: x <= 47 or x > 47 and x % 2 == 0, numbers))))
# print(*new_numbers)

# data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'), (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'), (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'), (7029917, 'Massachusetts'), (6910840, 'Tennessee')]
#
# for i in sorted(data, key=lambda x: x[1][-1], reverse=True):
#     print(f'{i[1]}: {i[0]}')

# data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']
#
# print(*sorted((sorted(data)), key=lambda x: len(x)))

# mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878, 'sunday', 'about', 454805, 'saturday', 'abort', 2121919, 2552839, 977970, 1772933, 1564063, 'abduct', 901271, 2680434, 'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias', 'bestow', 1875665, 'besides', 'bewilder', 1586517, 375290, 1503450, 2713047, 'abnormal', 2286106, 242192, 701049, 2866491, 'benevolent', 'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280, 686008, 'beyond', 2415643, 'aboard', 'bet', 859105, 'accident', 2223166, 894187, 146564, 1251748, 2851543, 1619426, 2263113, 1618068, 'berth', 'abolish', 'beware', 2618492, 1555062, 'access', 'absent', 'abundant', 2950603, 'betray', 'beverage', 'abide', 'abandon', 2284251, 'wednesday', 2709698, 'thursday', 810387, 'friday', 2576799, 2213552, 1599022, 'accept', 'abuse', 'abound', 1352953, 'bid', 1805326, 1499197, 2241159, 605320, 2347441]
#
# print(max(list(filter(lambda x: type(x) == int, mixed_list))))
#
# print(max(mixed_list, key=lambda x: (type(x) == int, x)))


# mixed_list = ['a', 'ab', 3, 5, 1, 8, 0, 'c', 'ac', 'aab']
#
# print(*sorted(mixed_list, key=int and str))
# asd = [int(i) for i in input().split()]

# print(*list(map(lambda x: 255 - x, [int(i) for i in input().split()])))


# koef = [int(elem) for elem in '2 3 0 1'.split()]
# n = 3  # int(input()) - макс степень
#
# m = 2  # int(input()) - макс степень
# koef_x = [int(elem) for elem in '1 2 1'.split()]
# res_koef = [0] * (n + m + 1)
#
# for i in range(m + 1):
#     for j in range(n + 1):
#         res_koef[i + j] += koef[j] * koef_x[i]
#
# print(*res_koef)


# print((2*(10**2))+(4*10)+3)
#
# coef = [int(i) for i in input().split()]
# x = int(input())
#
# def evaluate(coefficient, x):
#     pass


# numbers = [1, 2, 3, 4]
# romans = ['I', 'II', 'III']
# words = ['one', 'two']
#
# result = zip(numbers, words, romans)
# print(list(result))


# def ignore_command(command):
#     ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
#     return any(map(lambda x: x in command, ignore))
#     # for word in ignore:
#     #     if word in command:
#     #         return True
#     # return False
#
# print(ignore_command('delete'))

# countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
# capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
# population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]
#
# tmp = zip(countries, capitals, population)
#
# #print(*tmp)
#
# for i in zip(countries, capitals, population):
#     print(f'{i[1]} is the capital of {i[0]}, population equal {i[2]} people.')


# coord = [[float(_) for _ in input().split()] for i in range(3)]
# abscissas = [float(_) for _ in input().split()]
# ordinates = [float(_) for _ in input().split()]
# applicates = [float(_) for _ in input().split()]
#
#
# print(all(map(lambda x: x[0]**2 + x[1]**2 + x[2]**2 <= 4, zip(abscissas, ordinates, applicates))))


# print(all(map(lambda x: int(x) <= 255 if x.isdigit() else False, [_ for _ in input().split('.')])))

# start, stop = int(input()), int(input())
#
# numbers = [i for i in range(start, stop + 1) if '0' not in str(i)]
#
#
# def asd(x):
#     s = list(str(x))
#     flag = True
#     for i in range(len(s)):
#         if x % int(s[i]) == 0:
#             pass
#         else:
#             flag = False
#     if flag:
#         return True
#     else:
#         return False
#
# #for i in numbers:
#     # if all(map(lambda x: asd(x), [i])):
#     #     print(i, end=' ')
#
# for i in numbers:
#     if all(i % int(x) == 0 for x in str(i)):
#         print(i, end=' ')

# import string
#
# tmp = string.ascii_letters + string.digits
#
# password = input()
#
# print('YES') if all([any(map(lambda x: x in string.ascii_lowercase, password)) and any(map(lambda x: x in string.ascii_uppercase, password)) and any(map(lambda x: x in string.digits, password)) and len(password) >= 7]) else print('NO')


# def check_class():
#     return any(map(lambda x: x[1] == '5', [input().split() for _ in range(int(input()))]))
#
# print('YES' if all(map(lambda x: check_class(), range(int(input())))) else 'NO')


# def check_class():
#     return any(map(lambda x: '5' in x, [input() for _ in range(int(input()))]))
#
# print('YES' if all(map(lambda x: check_class(), range(int(input())))) else 'NO')
#
#
#
#
# print(('NO', 'YES')[all([any(['5' in input() for _ in 'k'*int(input())]) for _ in 'n'*int(input())])])


# def generate_letter(mail, name, date, time, place, teacher='Тимур Гуев', number=17):
#     return f'''To: {mail}
# Приветствую, {name}!
# Вам назначен экзамен, который пройдет {date}, в {time}.
# По адресу: {place}.
# Экзамен будет проводить {teacher} в кабинете {number}.
# Желаем удачи на экзамене!'''
#
# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))
# print()
# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00',
#                       'Часова 23, корпус 2', 'Василь Ярошевич', 23))


# def pretty_print(data, side='-', delimiter='|'):
#     k = sum(map(len, map(str, data))) + 2 * len(data) + 2
#     print(' ', end='')
#     if str(data[0]).isdigit():
#         print(k * side + side*3, end='')
#     else:
#         print(k * side, end='')
#     print()
#     print(delimiter, end='')
#     for i in data:
#         print(f' {i} {delimiter}', end='')
#     print()
#     print(' ', end='')
#     if str(data[0]).isdigit():
#         print(k * side + side*3, end='')
#     else:
#         print(k * side, end='')
#     print()
#
#
#
# pretty_print([1, 2, 10, 23, 123, 3000])
# pretty_print(['abc', 'def', 'ghi', '12345'])
# pretty_print(['abc', 'def', 'ghi'], side='*')
# pretty_print(['abc', 'def', 'ghi'], delimiter='#')
# pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')


# data = [['p', 'y', 't', 'h', 'o', 'n'], ['s', 't', 'e', 'p', 'i', 'k']]
# result = list(map(lambda x: '.'.join(x), data))
# print(result[1])


# from functools import reduce
#
# result = reduce(lambda s, x: s + str(x), [1, 2, 3, 4, 5], '+')
# print(result)
#
#
# print([1] + [] + [2])


# def concat(*args, sep=' '):
#     tmp = ''
#     for i in args[0:-1]:
#         tmp += str(i)+sep
#     tmp += str(args[-1])
#     return tmp


# def concat(*args, sep=' '):
#     tmp = sep.join(map(str, args))
#     return tmp
#
#
# print(concat('hello', 'python', 'and', 'stepik'))
# print(concat('hello', 'python', 'and', 'stepik', sep='*'))
# print(concat('hello', 'python', sep='()()()'))
# print(concat('hello', sep='()'))
# print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))


# from functools import reduce
#
# def product_of_odds1(data):   # data - список целых чисел
#     result = 1
#     for i in data:
#         if i % 2 == 1:
#             result *= i
#     return result
#
# def product_of_odds(data):   # data - список целых чисел
#     return reduce(lambda a, b: a * b, filter(lambda x: x % 2 == 1, data), 1)
#
# print(product_of_odds([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# words = 'the world is mine take a look what you have started'.split()
# words = map(lambda x: f'"{x}"', words)
# print(*words)


# numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
# numbers = filter(lambda x: str(x) != str(x)[::-1], numbers)
# print(*numbers)


# numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12), (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]
#
# sorted_numbers = sorted(numbers, key=lambda x: sum(x) / len(x), reverse=True)
#
# print(sorted_numbers)


# def call(func, x, y=0, z=0):
#     if x and y and z:
#         return func(x, y, z)
#     elif x and y:
#         return func(x, y)
#     elif x:
#         return func(x)

# def call(func, *args):
#     return func(*args)
#
#
# def mul7(x):
#     return x * 7
#
#
# def add2(x, y):
#     return x + y
#
#
# def add3(x, y, z):
#     return x + y + z
#
#
# print(call(mul7, 10))
# print(call(add2, 2, 7))
# print(call(add3, 10, 30, 40))
# print(call(bool, 0))


# def compose(f, g):
#     def tmp(x):
#         return f(g(x))
#     return tmp
#
# def add3(x):
#     return x + 3
#
#
# def mul7(x):
#     return x * 7
#
# print(compose(mul7, add3)(1))
# print(compose(add3, mul7)(2))
# print(compose(mul7, str)(3))
# print(compose(str, mul7)(5))


# def arithmetic_operations(func):
#     compare = x + y
#     oper = {'-': x - y, }
#     def tmp(x, y):
#         return lambda

# def arithmetic_operation(operation):
#     def func(x, y):
#         oper = {'-': lambda x, y: x - y,
#                 '+': lambda x, y: x + y,
#                 '*': lambda x, y: x * y,
#                 '/': lambda x, y: x / y}
#         return oper[operation](x, y)
#     return func
#
#
# add = arithmetic_operation('+')
# div = arithmetic_operation('/')
# print(add(10, 20))
# print(div(20, 5))
#
# print(arithmetic_operation('+')(10, 20))


# txt = 'cate Frog cat FROGs bee CATERS mouse cATwalk dolphin mOus Cats CatAlo'
#
# print(sorted(txt.split(), key=str.lower))


#txt = 'BaSis'.upper()
# sas = []
# tmp = map(lambda x: ord(x) - 65, txt)
# print(sum(list(map(lambda x: ord(x) - 65, input().upper()))))

# txt = [input() for i in range(int(input()))]
# asd = []
# for i in txt:
#     asd.append([i, sum(list(map(lambda x: ord(x) - 65, str(i).upper())))])
# asd.sort(key=lambda x: x[0][0:4])
# asd.sort(key=lambda x: x[1])
# for i in asd:
#     print(i[0])

# adresses = [[i for i in input().split('.')] for i in range(int(input()))]
#
# sum_adresses = []
#
# for i in adresses:
#     summ = 0
#     for e in range(len(i)):
#         summ += int(i[e]) * 256**(3 - e)
#     sum_adresses.append(['.'.join(i), summ])
#
# sum_adresses.sort(key=lambda x: x[1])
# for i in sum_adresses:
#     print(i[0])

