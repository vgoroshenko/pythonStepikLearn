# # объявление функции
# def draw_box():
#     for s in range(14):
#         print('*', end='')
#         for c in range(8):
#             if s < 1 or s > 12:
#                 print('*', end='')
#             else:
#                 print(' ', end='')
#         print('*', end='\n')
#
# # основная программа
# draw_box()  # вызов функции


# # объявление функции
# def draw_triangle():
#     print(*[i * '*' for i in range(1, 11)], sep='\n')
#
#     # for i in range(1, 11):
#     #     print('*' * i)
#
# # основная программа
# draw_triangle()  # вызов функции


# def draw_box(height, width):
#     height = 2
#     width = 10
#     for i in range(height):
#         print('*' * width)
#
# n = 5
# m = 7
# draw_box()
# print(n, m)

# fill = input()
# base = int(input())
#
# def draw_triangle(fill, base):
#     for i in range(base):
#         if i < base / 2:
#             print(fill * (i + 1))
#         else:
#             print(fill * (base - i))
#
# draw_triangle(fill, base)

# объявление функции
# def print_fio(name, surname, patronymic):
#     print(surname[0].upper(), end='')
#     print(name[0].upper(), end='')
#     print(patronymic[0].upper(), end='')
#
#
# # считываем данные
# name, surname, patronymic = input(), input(), input()
#
# # вызываем функцию
# print_fio(name, surname, patronymic)

# # объявление функции
# def print_digit_sum(n):
#     print(sum([int(i) for i in n]))
#
#
#
# # считываем данные
# n = list(input())
#
# # вызываем функцию
# print_digit_sum(n)

# def get_sum(x, y, z):
#     return x + y + z
#     print('Сумма равна', x + y + z)
# print(get_sum(1, 2 ,3))

# def convert_to_miles(km):
#     return km * 0.6214
# # считываем данные
# num = int(input())
#
# # вызываем функцию
# print(convert_to_miles(num))

# def get_days(month):
#     month_list = [31,28,31,30,31,30,31,31,30,31,30,31]
#     return month_list[month - 1]
# month = int(input())
#
# print(get_days(month))

# # объявление функции
# def get_factors(num):
#     return [int(i) for i in range(1, num + 1) if num % i == 0]
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(get_factors(n))

# # объявление функции
# def get_factors(num):
#     return len([_ for _ in range(1, num + 1) if num % _ == 0])
#
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(get_factors(n))

# # объявление функции
# def find_all(target, symbol):
#     return [i for i in range(len(target)) if target[i] == symbol]
#
# # считываем данные
# s = input()
# char = input()
#
# # вызываем функцию
# print(find_all(s, char))

# # объявление функции
# def merge(list1, list2):
#     return sorted(list1 + list2)
#
# # считываем данные
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]
#
# # вызываем функцию
# print(merge(numbers1, numbers2))

# def quick_merege(strings):
#     num1 = []
#     for i in range(strings):
#         num = [int(i) for i in input().split()]
#         num1.extend(num)
#     num1.sort()
#     return print(*num1)
#
#
# s = int(input())
#
# quick_merege(s)

# # объявление функции
# def is_valid_triangle(side1, side2, side3):
#     if (a < b + c) and (b < c + a) and (c < a + b):
#         return True
#     else:
#         return False
#
# # считываем данные
# a, b, c = int(input()), int(input()), int(input())
#
# # вызываем функцию
# print(is_valid_triangle(a, b, c))


# start, stop = int(input()), int(input())
#
# for digit in range(start, stop + 1):
#     flag = True
#     for i in range(2, digit):
#         if digit % i == 0:  # если исходное число делится на какое-либо отличное от 1 и самого себя
#             flag = False
#     if flag == True and digit != 1:
#         print(digit, end='\n')

# # объявление функции
# def is_prime(num):
#     flag = True
#     for i in range(2, num):
#         if num % i == 0:
#             flag = False
#
#     if flag == True and num != 1:
#         return True
#     else:
#         return False
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(is_prime(n))

# def is_prime(num):
#     flag = True
#     for i in range(2, num):
#         if num % i == 0:
#             flag = False
#
#     if flag == True and num != 1:
#         return True
#     else:
#         return False
#
# def get_next_prime(num):
#     num += 1
#     while is_prime(num) != True:
#         num += 1
#     return num
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(get_next_prime(n))

# import string
# # объявление функции
# def is_password_good(password):
#     flag = 0
#     if len(password) > 8:
#         flag += 1
#     for i in range(len(password)):
#         if password[i] in string.ascii_lowercase:
#             flag += 1
#             break
#     for i in range(len(password)):
#         if password[i] in string.ascii_uppercase:
#             flag += 1
#             break
#     for i in range(len(password)):
#         if password[i] in string.digits:
#             flag += 1
#             break
#     if flag == 4:
#         return True
#     else:
#         return False
#
# # считываем данные
# txt = list(input())
#
# # вызываем функцию
# print(is_password_good(txt))


# # объявление функции
# def is_one_away(word1, word2):
#     count = 0
#     if word1 == word2:
#         return False
#     if len(word1) != len(word2):
#         return False
#     for i in range(len(word1)):
#         if word1[i] != word2[i]:
#             count += 1
#     if count > 1:
#         return False
#     else:
#         return True
# # считываем данные
# txt1 = input()
# txt2 = input()
#
# # вызываем функцию
# print(is_one_away(txt1, txt2))


# # объявление функции
# import string
#
#
# def is_palindrome(text):
#     [text.remove(i) for i in text if i in string.punctuation or i in string.whitespace]
#     [text.remove(i) for i in text if i in string.punctuation or i in string.whitespace]
#     text_revert = text[::-1]
#     count_false = 0
#     for c in range(len(text)):
#         if text[c] != text_revert[c]:
#             count_false += 1
#     if count_false != 0:
#         return False
#     else:
#         return True
#
# # считываем данные
# txt = list(input().lower())
#
# # вызываем функцию
# print(is_palindrome(txt))


# объявление функции
#import math
import string


# def is_valid_password(password):
#     def is_prime(num):
#         flag = True
#         for i in range(2, num):
#             if num % i == 0:
#                 flag = False
#
#         if flag == True and num != 1:
#             return True
#         else:
#             return False
#     def is_palindrome(text):
#         text = list(str(text))
#         text_revert = text.copy()
#         text_revert.reverse()
#         count_false = 0
#         for c in range(len(text)):
#             if text[c] != text_revert[c]:
#                 count_false += 1
#         if count_false != 0:
#             return False
#         else:
#             return True
#     def is_even(num):
#         if num % 2 == 0:
#             return True
#         else:
#             return False
#
#     if is_palindrome(password[0]) == True and is_prime(password[1]) == True and is_even(password[2]) == True and len(psw) < 4:
#         return True
#     else:
#         return False
#
# # считываем данные
# psw = [int(i) for i in input().split(':')]
#
# # вызываем функцию
# print(is_valid_password(psw))


# # объявление функции
# def convert_to_python_case(text):
#     result =[]
#     for i in range(len(text)):
#         char = str(text[i])
#         if i == 0:
#             result.insert(i * 10, char.lower())
#         if char.isupper():
#             result.insert(i * 10, '_')
#             result.insert(i * 10, char.lower())
#         if char.islower() or char.isdigit():
#             result.insert(i * 10, char)
#     return print(*result, sep='')
#
# # считываем данные
# txt = list(input())
#
# # вызываем функцию
# convert_to_python_case(txt)

# # объявление функции
# def get_middle_point(x1, y1, x2, y2):
#     return (x1 + x2) / 2, (y1 + y2) / 2
#
# # считываем данные
# x_1, y_1 = int(input()), int(input())
# x_2, y_2 = int(input()), int(input())
#
# # вызываем функцию
# x, y = get_middle_point(x_1, y_1, x_2, y_2)
# print(x, y)

# import math
# # объявление функции
# def get_circle(radius):
#     return 2 * math.pi * radius, math.pi * r ** 2
#
# # считываем данные
# r = float(input())
#
# # вызываем функцию
# length, square = get_circle(r)
# print(length, square)




# объявление функции
def solve(a, b, c):
    #a, b, c = float(a), float(b), float(c)

    d = (b ** 2) - (4 * a * c)

    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        if x1 < x2:
            return x1, x2
        elif x1 > x2:
            return x2, x1
    elif d == 0:
        x = -b / (2 * a)
        return x, x

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)