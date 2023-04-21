# if input()[-2:] == '00':
#     print('YES')
# else:
#     print('NO')


# x = [1, 2, 3 ,4 ,5 ,6 ,7, 8]
# y = [1, 2, 3 ,4 ,5 ,6 ,7, 8]
#
# a, a1 = int(input()), int(input())
# b, b1 = int(input()), int(input())

# if (a + a1 + b + b1) % 2 == 0:
#     print('YES')
# else:
#     print('NO')

# a, b = int(input()), input()
#
# if a > 9 and a < 16 and b == 'f':
#     print('YES')
# else:
#     print('NO')

# rims = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VII', 'IX', 'X']
#
# a = int(input())
#
# if 0 >= a < 11:
#     print(rims[a])
# else:
#     print('ошибка')

# digit = int(input())
#
# if digit % 2 != 0:
#     print('YES')
# elif digit % 2 == 0 and digit >= 2 and digit <= 5:
#     print('NO')
# elif digit % 2 == 0 and digit >= 6 and digit <= 20:
#     print('YES')
# elif digit % 2 == 0 and digit > 20:
#     print('NO')

#Ход слона
# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# if (x1 - y1) == (x2 - y2) or (x1 + y1) == (x2 + y2):
#     print ('YES')
# else:
#     print ('NO')

#Ход коня
# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
#
#
# if abs(x1 - x2) == 1 and abs(y1 - y2) == 2 or abs(x1 - x2) == 2 and abs(y1 - y2) == 1:
#     print('YES')
# else:
#     print('NO')

#Ход ферзя шахматы
# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
#
# if (x1 == x2 and y1 != y2) or (x1 != x2 and y1 == y2) or abs(x1 - x2) == abs(y1 -y2):
#     print('YES')
# else:
#     print('NO')