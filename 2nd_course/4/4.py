# num = int(input())
# if num > -3 and num < 7:     # num >= 100 and num <= 999
#     print('Не принадлежит')
# else:
#     print('Принадлежит')

# num = int(input())
# if num > -30 and num <= -2 or num > 7 and num <= 25:     # num >= 100 and num <= 999
#     print('Принадлежит')
# else:
#     print('Не принадлежит')

# num = int(input())
# if (num > 999 and num <= 9999) and (num % 7 !=0 or num % 17 !=0):     # num >= 100 and num <= 999
#     print('YES')
# else:
#     print('NO')

# a = int(input())
# b = int(input())
# c = int(input())
# if (a < b + c) and (b < c + a) and (c < a + b):
#     print('YES')
# else:
#     print('NO')

# num = int(input())
# if ((num % 4 == 0) and not (num % 100 == 0)) or (num % 400 == 0):     # num >= 100 and num <= 999
#     print('YES')
# else:
#     print('NO')

# x = int(input())
# y = int(input())
# x1 = int(input())
# y1 = int(input())
# if x == x1 or y == y1:     # num >= 100 and num <= 999
#     print('YES')
# else:
#     print('NO')


# x = int(input())
# y = int(input())
# x1 = int(input())
# y1 = int(input())
#
# a = x - x1
# b = y - y1
# if (a <= 1 and a > -2) and (b <= 1 and b > -2):     # num >= 100 and num <= 999
#     print('YES')
# else:
#     print('NO')

# a = int(input())
# b = int(input())
#
# if a > b:
#     print('NO')
# elif a < b:
#     print('YES')
# else:
#     print("Don't know")

# a = int(input())
# b = int(input())
# c = int(input())
#
# if a == b and b != c or a == c and c != b or b == c and a != c:
#     print('Равнобедренный')
# elif a == b ==c:
#     print('Равносторонний')
# elif a != b and b != c and a != c:
#     print('Разносторонний')

# a = int(input())
# b = int(input())
# c = int(input())
#
#
# if (a < b and a > c) or (a > b and a < c):
#     print(a)
# elif (b < a and b > c) or (b > a and b < c):
#     print(b)
# else:
#     print(c)

# a = int(input())
#
# if a == 2:
#     print('28')
# elif a % 2 == 0 and a != 10 and a != 12 and a != 8 or a == 9 or a == 11:
#     print('30')
# elif a % 2 != 0 or a == 10 or a == 12 or a == 8:
#     print('31')

# a = int(input())
#
# if a < 60:
#     print('Легкий вес')
# elif a > 59 and a <= 63:
#     print('Первый полусредний вес')
# elif a > 63 and a < 69:
#     print('Полусредний вес')

# a = int(input())
# b = int(input())
# mnoj = input()
#
# if mnoj == '+':
#     print(a + b)
# elif mnoj == '-':
#     print(a - b)
# elif mnoj == '*':
#     print(a * b)
# elif mnoj == '/' and b == 0:
#     print('На ноль делить нельзя!')
# elif mnoj == '/':
#     print(a / b)
# elif mnoj != '/' or mnoj != '*' or mnoj != '+' or mnoj != '-':
#     print('Неверная операция')

# a1 = 'красный'
# b1 = 'синий'
# c1 = 'желтый'
#
# a = input()
# b = input()
# #c = input()
#
# # a1 = a and b #  == 'фиолетовый'
# # b1 = a and c # == 'оранжевый'
# # c1 = b and c # == 'зеленый'
#
# if (a == a1 and b == b1) or (b == a1 and a == b1):
#     print('фиолетовый')
# elif (a == a1 and b == c1) or (b == a1 and a == c1):
#     print('оранжевый')
# elif (a == b1 and b == c1) or (b == b1 and a == c1):
#     print('зеленый')
# elif a == a1 and b == a1:
#     print(a1)
# elif a == b1 and b == b1:
#     print(b1)
# elif a == c1 and b == c1:
#     print(c1)
# elif (a != a1 or a != b1 or a != c1) or (b != a1 or b != b1 or b != c1):
#     print('ошибка цвета')

# a = int(input())
#
# if a == 0:
#     print('зеленый')
# elif a > 36 or a < 0:
#     print('ошибка ввода')
# elif a <= 10 and a % 2 != 0:
#     print('красный')
# elif a <= 10 and a % 2 == 0:
#     print('черный')
# elif a > 10 and a <= 18 and a % 2 != 0:
#     print('черный')
# elif  a > 10 and a <= 18 and a % 2 == 0:
#     print('красный')
# elif a > 18 and a <= 28 and a % 2 != 0:
#     print('красный')
# elif  a > 18 and a <= 28 and a % 2 == 0:
#     print('черный')
# elif a > 28 and a <= 36 and a % 2 != 0:
#     print('черный')
# elif  a > 28 and a <= 36 and a % 2 == 0:
#     print('красный')


# a1 = -150
# b1 = -49
# a2 = -100
# b2 = -50
#
# if a2 == b1:
#     print(a2)
# elif a2 < b1 and b2 < b1:
#     print(a2, b2)
# elif a2 < b1:
#     print(a2, b1)
# else:
#     print('пустое множество')


# def pascal_triangle_row(n):
#     pascal_triangle = [[1]*(i+1) for i in range(n+1)]
#     for i in range(2, n+1):
#         for j in range(1, i):
#             pascal_triangle[i][j] = pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j]
#     return pascal_triangle[n]
#
# def pascal_triangle(n):
#     for i in range(n):
#         row = pascal_triangle_row(i)
#         print(" ".join(map(str, row)))
#
# pascal_triangle(int(input()))

# def get_sublists(lst):
#     if not lst:
#         return [[]]
#     else:
#         res = get_sublists(lst[1:])
#         return res + [[lst[0]] + x for x in res]
#
# # пример использования
# s = input() # считываем строку
# lst = s.split() # разбиваем строку на отдельные слова (элементы списка)
# sublists = get_sublists(lst) # получаем все подсписки
# result = [list(map(str, sublist)) for sublist in sublists] # преобразуем все элементы подсписков в строки
# print(result) # выводим результат


# n, m = map(int, input().split())
#
# matrix = []
# for i in range(n):
#     row = list(map(int, input().split()))
#     matrix.append(row)
#
# i, j = map(int, input().split())
#
# for k in range(n):
#     matrix[k][i-1], matrix[k][j-1] = matrix[k][j-1], matrix[k][i-1]
#
# for row in matrix:
#     print(*row)


# n = int(input())
# matrix = []
# for i in range(n):
#     row = list(map(int, input().split()))
#     matrix.append(row)
#
# is_symmetric = True
# for i in range(n):
#     for j in range(i, n):
#         if matrix[i][j] != matrix[j][i]:
#             is_symmetric = False
#             break
#
# if is_symmetric:
#     print("YES")
# else:
#     print("NO")


n = int(input())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

temp_row = matrix[0]
matrix[0] = matrix[n-1]
matrix[n-1] = temp_row

for row in matrix:
    print(" ".join(str(x) for x in row))



