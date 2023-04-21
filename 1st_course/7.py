# for i in range(5):
#     num = int(input())
#     print('Квадрат вашего числа равен:', num * num)
# print('Цикл завершен')

# for i in range(10):
#     print('Python is awesome!')

# a = input()
# b = int(input())
#
# for i in range(b):
#      print(a)


# for i in range(5):
#     print('AAA')
# for i in range(5):
#     print('BBBB')
# print('E')
# for i in range(9):
#     print('TTTTT')
# print('G')

# a = input()
# for i in range(a):
#     print('*******************')

# a = input()
#
# for i in range(10):
#     print(i, a)

# a = int(input())
#
# for i in range(a + 1):
#     print('Квадрат числа', i, 'равен', i * i)

# a = int(input())
#
# for i in range(a):
#     print('*' * a)
#     a = a - 1

# a, b, c = int(input()), int(input()), int(input())
#
# for i in range(c):
#     print(i + 1, a)
#     a = (a * (b / 100)) + a

# a, b = int(input()), int(input())
#
# for i in range(a, b + 1):
#     print(i)

# a, b = int(input()), int(input())
#
# if a < b:
#     for i in range(a, b + 1):
#         print(i)
# elif a > b:
#     for i in range(a, b - 1, -1):
#         print(i)
# else:
#     print(a)

# a, b = int(input()), int(input())
#
# a = a % 2 + a - 1
# for i in range(a, b - 1, -2):
#     print(i)

# a, b = int(input()), int(input())
#
# for i in range(a, b + 1):
#     if i % 17 == 0 or i % 10 == 9 or (i % 3 == 0 and i % 5 == 0):
#         print(i)

# a = int(input())
#
# for i in range(10):
#     i += 1
#     total = a * i
#     print(a, 'x', i, '=', total)


# counter = 0
# for i in range(10):
#     num = int(input())
#     if num > 10:
#         counter = counter + 1
# print('Было введено', counter, 'чисел, больших 10.')

# total = 0
# for i in range(1, 101):
#     total = total + i
# print('Сумма равна', total)


# largest = -1
# for i in range(10):
#     num = int(input())
#     if num > largest:
#         largest = num
# print('Наибольшее число равно', largest)

# a, b = int(input()), int(input())
#
# total = 0
# for i in range(a, b):
#     if a == b:
#         if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
#             print(i)
#             total += 1
# print(total)

# a = int(input())
# count = 0
# for i in range(a):
#     a = int(input())
#     count += a
# print(count)


# import math
#
# a = int(input())
#
# total = 0
# for i in range(a):
#     summa = 1 / (i + 1)
#     total += summa
# print(total - math.log(a))


# a = int(input())
# summa = 0
# for i in range(a):
#     kvadrat = (i + 1) ** 2
#     if kvadrat % 10 == 2 or kvadrat % 10 == 5 or kvadrat % 10 == 8:
#         summa += (i + 1)
#     elif kvadrat == 0:
#         print('0')
# print(summa)

# a = int(input())
# total = 1
# for i in range(a):
#     total = (i + 1) * total
# print(total)

# a = int(input())
# total = 0
# for i in range(a):
#     total += ((-1) ** ((i + 1) + 1)) * (i + 1)
# print(total)

# a = input()
#
# while a != 'КОНЕЦ' and a != 'конец':
#     print(a)
#     a = input()

# a = input()
# count = 0
# while a != 'стоп' and a != 'хватит'  and a != 'достаточно':
#     count += 1
#     a = input()
# print(count)

# a = int(input())
#
# while a % 7 == 0:
#     print(a)
#     a = int(input())

# a = int(input())
# total = 0
# while a >= 0:
#     total += a
#     a = int(input())
# print(total)

# a = int(input())
# total = 0
# while a >= 0 and a <= 5:
#     if a == 5:
#         total += 1
#     a = int(input())
# print(total)


# a = int(input())
# count = 0
# while a >= 25:
#     count += 1
#     a -= 25
# while a >= 10:
#     count += 1
#     a -= 10
# while a >= 5:
#     count += 1
#     a -= 5
# while a >= 1:
#     count += 1
#     a -= 1
# print(count)


# num = int(input())
#
# while num != 0:
#     last_digit = num % 10
#     print(last_digit)
#     num = num // 10


# num = int(input())
#
# while num != 0:
#     last_digit = num % 10
#     print(last_digit, end='')
#     num = num // 10

# largest = -1
# for i in range(10):
#     num = int(input())
#     if num > largest:
#         largest = num
# print('Наибольшее число равно', largest)


# num = int(input())
# n = 7645897791
#
#
# lowest = 0
# largest = 0
# last = 0
# before_largest = 0
#
#
# while num > 0:
#     last = num % 10
#     if num > 10:
#         before_last = num % 100 // 10
#     if last >= largest:
#         largest = last
#         if before_last < largest:
#             last = before_last
#     elif last < before_last:
#         lowest = last
#     num //= 10
# print('Макс', largest)
# print('Мин', lowest)

# n = int(input("Enter a number:"))
#
# sd = 9
# ld = 0
#
# while n > 0:
#     r = n % 10
#     if sd > r:
#         sd = r
#     if ld < r:
#         ld = r
#     n = int(n / 10)
#
# print("Максимальная цифра равна", ld)
# print("Минимальная цифра равна", sd)


# num = int(input())
#
# summa = 0
# count_digit = 0
# umnojenie = 1
# num2 = num
#
#
# while num != 0:
#     last = num % 10
#     summa += last
#     count_digit += 1
#     umnojenie *= last
#     sr_arifmet = summa / count_digit
#     first_digit = last
#     num //= 10
#
# last_digit = num2 % 10
# summa_first_last_digit = first_digit + last_digit
#
# print(summa)
# print(count_digit)
# print(umnojenie)
# print(sr_arifmet)
# print(first_digit)
# print(summa_first_last_digit)


# num = int(input())
# last = 0
# while num > 9:
#     last = num % 10
#     num //= 10
# print(last)

# num = int(input())
# flag = True
# last_digit = num % 10
#
# while num != 0:
#     last_digit_in_loop = num % 10
#     if last_digit != last_digit_in_loop:
#         flag = False
#     num //= 10
#
# if flag == True:
#     print('YES')
# else:
#     print('NO')

# num = int(input())
# flag = True
#
# while num != 0:
#     last_digit_in_loop = num % 10
#     if num > 10:
#          before_last = num % 100 // 10
#     if before_last < last_digit_in_loop:
#         flag = False
#     num //= 10
#
# if flag == True:
#     print('YES')
# else:
#     print('NO')


# a = 1934234249
# i = 2
# for i in range(2, a + 1):
#     if a % i == 0 and i > 1:
#         break
# print(i)


# num = int(input())
#
# for i in range(1, num + 1):
#     if i > 4 and i <= 9:
#         continue
#     if i > 16 and i <= 37:
#         continue
#     if i > 77 and i <= 87:
#         continue
#     print(i)


# count = 0
# product = 1
# product_count = 0
# for i in range(1, 10 + 1):
#     num = int(input())
#     if num > 0:
#         product *= num
#         product_count += 1
#     else:
#         count += 1
# if count > 0:
#     print(product_count)
#     print(product)
# else:
#     print('NO')

# count = 0
# p = 1
# for i in range(1, 11):
#     x = int(input())
#     if x >= 0:
#         p = p * x
#         count = count + 1
# if count > 0:
#     print(count)
#     print(p)
# else:
#     print('NO')


# mx = -999999
# s = 0
# for i in range(1, 11):
#     x = int(input())
#     if x < 0:
#         s += x
#     if x > mx and x < 0:
#         mx = x
# if s < 0:
#     print(s)
#     print(mx)
# else:
#     print('NO')


# summa = 0
# for i in range(1, 8):
#     num = int(input())
#     if num % 2 == 0:
#         summa += num
# if summa > 0:
#     print(summa)
# else:
#     print('0')

# num = int(input())
# max_digit = -1
# while num > 0:
#     digit = num % 10
#     if digit % 3 == 0:
#         if digit > max_digit:
#             max_digit = digit
#     num //= 10
# if max_digit == -1:
#     print('NO')
# else:
#     print(max_digit)

# num = int(input())
# last_num = 0
# while num > 0:
#     if num != 0:
#         last_num = num
#     num //= 10
# print(num)

# num = int(input())
# while num // 10 != 0:
#     num //= 10
# print(num)

#
# num = int(input())
# total = 1
# while num // 10 != 0:
#     digit = num % 10
#     total *= digit
#     num //= 10
# print(total)


# for minutes in range(60):
#     for seconds in range(60):
#         print(minutes, ':', seconds)

# for i in range(1, 4):
#     for j in range(3, 5):
#         print(i + j, end='')
# num = int(input())
# for s in range(num):
#     for i in range(3):
#         print(num, end=' ')
#     print()

# num = int(input())
#
# for i in range(num):
#     for s in range(5):
#         print(i + 1, end=' ')
#     print()


# num = int(input())
#
# for i in range(1, num // 2 + 2):
#     print(i * '*', end='\n')
#     if i == num // 2 + 1:
#         for s in range(num // 2, 0, -1):
#             print(s * '*', end='\n')


# for i in range(num):
#     for j in range(i + 1):
#         print('*', end='')
#     print()
# num = int(input())
# for i in range(num + 1):
#     print(str(i) * i, end='')
#     print()

# total = 0
# for x in range(1, 13):
#     for y in range(1, 12):
#         for z in range(1, 11):
#             if x * 28 + y * 30 + z * 31 == 365:
#                 total += 1
#                 print('x =', x, 'y =', y, 'z =', z)

# total = 0
# for x in range(1, 10):
#     for y in range(1, 20):
#         for z in range(1, 200):
#             if x * 10 + y * 5 + z * 0.5 == 100 and x + y + z == 100:
#                 total += 1
#                 print('x =', x, 'y =', y, 'z =', z)
# print('Общее количество натуральных решений =', total)


# num = 5

# for a in range(1, 150):
#     for b in range(1, 150):
#         for c in range(1, 150):
#             for d in range(1, 150):
#                 for e in range(1, 150):
#                     # summ = (((a ** num) + (b ** num) + (c ** num) + (d ** num)) ** 0.5) ** 5
#                     summ = (a ** num) + (b ** num) + (c ** num) + (d ** num)
#                     total = e ** num
#                     if total == summ and total != 0:
#                         break
# print(a + b + c + d + e)


# for a in range(2):
#     for b in range(6):
#         for c in range(6):
#             print('asd')

# for a in range(1, 150):
#     for b in range(a + 1, 150):
#         for c in range(b + 1, 150):
#             for d in range(c + 1, 150):
#                 # print(a, ':', b, ':', c, ':', d, ':', e )
#                 summ = int((a ** 5) + (b ** 5) + (c ** 5) + (d ** 5))
#                 e = int(summ ** 0.2)
#                 total = e ** 5
#                 if total == summ:
#                     s = a + b + c + d + e
#                     print(s)

# num = int(input())
# for line in range(1, num + 1):
#     for digit in range(1, line + 1):
#         print(digit, end='')
#     for invers_digit in range(line - 1, 0, -1):
#         print(invers_digit, end='')
#     print()

# num_start, num_end = int(input()), int(input())
# max_divider = 0
# summ_max_divider = 0
# for digit in range(num_start, num_end + 1):
#     summ_divider = 0
#     for num in range(1, digit + 1):
#         if digit % num == 0:
#             summ_divider += num
#         if summ_divider >= summ_max_divider and num > max_divider:
#             max_divider = num
#             summ_max_divider = summ_divider
# print(max_divider, summ_max_divider)


# num = int(input())
# for digit in range(1, num + 1):
#     total = 0
#     for divider in range(1, digit + 1):
#         if digit % divider == 0:
#             total += 1
#     print(str(digit) + total * '+')


# num = int(input())
# while num > 9:
#     summa = 0
#     while num > 0:
#         last_digit = num % 10
#         summa += last_digit
#         num //= 10
#     num = summa
# print(num)

# import math
# num = int(input())
# summa = 0
# for digit in range(1, num + 1):
#     summa += math.factorial(digit)
# print(summa)

# ДОДЕЛАТЬ!!!!!!!!!!!!!!!!!  7.9.6 !!!!!!!!!!!!!!!!

# num = int(input())
# summa = 0
# total = 0
# for n in range(1, num + 1):
#     summa += total
#     total = 1
#     for digit in range(n, num):
#         total = (digit + 1) * total
# print(summa)


# Факториал
# num = int(input())
# total = 1
# for digit in range(num):
#     total = (digit + 1) * total
# print(total)

# простое или составное число
# start, stop = int(input()), int(input())
#
# for digit in range(start, stop + 1):
#     flag = True
#     for i in range(2, digit):
#         if digit % i == 0:  # если исходное число делится на какое-либо отличное от 1 и самого себя
#             flag = False
#     if flag == True and digit != 1:
#         print(digit, end='\n')

# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
# if min(b1, b2) < max(a1, a2):
#     print('пустое множество')
# elif min(b1, b2) == max(a1, a2):
#     print(min(b1, b2))
# else:
#     print(max(a1, a2), min(b1, b2))