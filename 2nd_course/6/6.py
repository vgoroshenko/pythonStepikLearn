# a = float(input())
# b = float(input())
#
# s = 1/2 * a * b
#
# print(s)


# s = float(input())
# v1 = float(input())
# v2 = float(input())
#
# v = v1 + v2
# t = s/v
#
# print(t)

# a = float(input())
#
# a = 1 / a
#
# if a == 0:
#     print('Обратного числа не существует')
#
# print(a)

# f = float(input())
#
# c = 5/9*(f - 32)
#
# print(c)


# a = float(input())
#
# if a <= 2 and a > 0:
#     a = a * 10.5
#     if a == 10.5:
#         print(float(a))
#     else:
#         print(int(a))
# else:
#     a = ((a - 2) * 4) + 21
#     print(int(a))

# a = float(input())
#
# a = a * 10
# a = a % 10
#
# print(int(a))

# a = float(input())
#
# a1 = int(a)
#
# b = a - a1
#
# print(b)

# a1 = int(input())
# a2 = int(input())
# a3 = int(input())
# a4 = int(input())
# a5 = int(input())
#
# print('Наименьшее число =', min(a1, a2, a3, a4, a5))
# print('Наибольшее число =', max(a1, a2, a3, a4, a5))

# a1 = int(input())
# a2 = int(input())
# a3 = int(input())
#
# print(max(a1, a2, a3))
# if (a1 < a2 and a1 > a3) or (a1 > a2 and a1 < a3) or (a1 == a2):
#     print(a1)
# elif (a2 < a1 and a2 > a3) or (a2 > a1 and a2 < a3) or (a2 == a3):
#     print(a2)
# else:
#     print(a3)
# print(min(a1, a2, a3))

# a = int(input())
#
# a1 = a // 100
# a2 = (a // 10) % 10
# a3 = a % 10
#
# b1 = min(a1, a2, a3)
# b2 = 0
# b3 = max(a1, a2, a3)
#
# if (a1 < a2 and a1 > a3) or (a1 > a2 and a1 < a3) or (a1 == a2):
#     b2 = a1
# elif (a2 < a1 and a2 > a3) or (a2 > a1 and a2 < a3) or (a2 == a3):
#     b2 = a2
# else:
#     b2 = a3
#
# if b3 - b1 == b2:
#     print('Число интересное')
# else:
#     print('Число неинтересное')

# a1 = int(input())
# a2 = int(input())
# a3 = int(input())
# a4 = int(input())
# a5 = int(input())
#
# total = abs(a1) + abs(a2) + abs(a3) + abs(a4) + abs(a5)
#
# print(total)


# a1, a2 = int(input()), int(input())
# b1, b2 = int(input()), int(input())
#
# total = (abs(a1 - b1))+(abs(a2 - b2))
#
# print(total)

# from math import sqrt
#
# a1, b1 = float(input()), float(input())
# a2, b2 = float(input()), float(input())
#
# a1 = (a1 - a2) ** 2
# b1 = (b1 - b2) ** 2
#
# p = sqrt(a1 + b1)
#
# print(p)

# import math
#
# a1 = float(input())
#
# s = math.pi * a1 ** 2
#
# c = 2 * math.pi * a1
#
# print(s, c, sep=('\n'))
import math
#
# a, b = float(input()), float(input())
#
# ar = (a + b) / 2
# geo = math.sqrt(a * b)
# gar = (2 * (a * b)) / (a + b)
# kv = math.sqrt((a ** 2 + b ** 2) / 2)
#
# print(ar, geo, gar, kv, sep='\n')

# x = float(input())
#
# x = math.radians(x)
#
# x = math.sin(x) + math.cos(x) + math.tan(x) ** 2
#
# print(x)

# x = float(input())
#
# x = math.floor(x) + math.ceil(x)
#
# print(x)


# a, b, c = input(), input(), input()
#
# a1, b1, c1 = len(a), len(b), len(c)
#
# if min(a1, b1, c1) == a1:
#     print(a)
# elif min(a1, b1, c1) == b1:
#     print(b)
# elif min(a1, b1, c1) == c1:
#     print(c)
#
# if max(a1, b1, c1) == a1:
#     print(a)
# elif max(a1, b1, c1) == b1:
#     print(b)
# elif max(a1, b1, c1) == c1:
#     print(c)

# a, b, c = input(), input(), input()
# a1, b1, c1 = len(a), len(b), len(c)
#
# a = min(a1, b1, c1)
# c = max(a1, b1, c1)
#
# if (a1 < b1 and a1 > c1) or (a1 > b1 and a1 < c1):
#     b = a1
# elif (b1 < a1 and b1 > c1) or (b1 > a1 and b1 < c1):
#     b = b1
# else:
#     b = c1
#
# if c - b == b - a:
#     print('YES')
# else:
#     print('NO')


# a = input()
#
# if 'синий' in a:
#     print('YES')
# else:
#     print('NO')

# a = input()
#
# if '@' in a and '.' in a:
#     print('YES')
# else:
#     print('NO')