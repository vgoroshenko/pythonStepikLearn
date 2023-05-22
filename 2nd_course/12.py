# import random
#
# random.seed(17)   # явно устанавливаем начальное значение для генератора случайных чисел
#
# for _ in range(10):
#     print(random.randint(1, 100))


# import random
#
# n = int(input())    # количество попыток
#
# for _ in range(n):
#     print('Орел') if random.randint(0, 1) else print('Решка')


# import random
#
# n = int(input())    # количество попыток
#
# for _ in range(n):
#     print(random.randint(1, 6))


# import random
#
# length = int(input())    # длина пароля
#
# for _ in range(length):
#     print(chr(random.choice([random.randint(65, 90), random.randint(97, 122)])), end='')


# import random
# # txt = {}
# # while len(txt) != 7:
# nums = []
#
# while len(nums) != 7:
#     num = random.randint(1, 49)
#     if num not in nums:
#         nums.append(num)
#
# print(*sorted(nums))
#
# random.sample()


# import random
#
#
# def generate_ip():
#     num = [str(random.randint(0, 255)) for _ in range(4)]
#     return '.'.join(num)
#
#
# generate_ip()

# import random
# import string
#
#
# def generate_index():
#     tmp = []
#     for i in range(5):
#         if i == 2:
#             tmp.append('_')
#         elif i == 1 or i == 3:
#             tmp.append(str(random.randint(0, 99)))
#         else:
#             tmp.append(''.join(random.sample(string.ascii_uppercase, 2)))
#
#     return ''.join(tmp)


# import random
#
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
#
# for i in range(len(matrix)):
#     random.shuffle(matrix[i])
#
# print(matrix)


# import random
#
# bilets = set()
#
# while len(bilets) < 100:
#     bilets.add(''.join([str(random.randint(1, 9)) for _ in range(7)]))
#
# print(*bilets, sep='\n')

# import random
# txt = list(input())
# random.shuffle(txt)
# print(''.join(txt))


# import random
#
# matrix = [[0]*5 for _ in range(5)]
# nums = [_ for _ in range(1, 76)]
# rnd_nums = random.sample(nums, 25)
#
# for i in range(5):
#     for j in range(5):
#         num = random.choice(rnd_nums)
#         matrix[i][j] = num
#         rnd_nums.remove(num)
#
#
# matrix[2][2] = 0
#
# for r in range(5):
#     for c in range(5):
#         print(str(matrix[r][c]).ljust(3), end=' ')
#     print()
# import random

# fio_dict = {key: input() for key in range(int(input()))}
# fio_dict_cp = fio_dict.copy()
#
# for key in fio_dict:
#     tmp = random.choice(fio_dict)
#     while tmp in fio_dict_cp[key] and tmp == '0':
#      tmp = random.choice(fio_dict)
#
#     fio_dict_cp[key] = f'{fio_dict_cp[key]} - {tmp}'
#     for key, value in fio_dict.items():
#         if tmp == value:
#             fio_dict[key] = '0'
#     #[print(fio_dict[key]) for key, value in fio_dict.items() if value == tmp]
#
#
# print(fio_dict_cp)


# import random
#
# fio_lst = [input() for _ in range(int(input()))]
# fio_cp = fio_lst.copy()
#
# for i in range(len(fio_cp)):
#     tmp = random.choice(fio_lst)
#     while tmp in fio_cp[i]:
#         tmp = random.choice(fio_lst)
#     fio_cp[i] = f'{fio_cp[i]} - {tmp}'
#     fio_lst.remove(tmp)
#     print(fio_cp[i])

# print(*fio_cp)


# import string
# import random
#
# chars_lst = (string.ascii_lowercase, string.ascii_uppercase, string.digits)
#
# ban_chars = ('l', 'L', 'i', 'I', 'o', 'O', '0', '1')
#
# def generate_pass(lenght):
#     txt = []
#     while len(txt) < lenght:
#         char = random.choice(random.choice(chars_lst))
#         if char not in ban_chars:
#             txt.append(char)
#     return  txt   #[random.choice(random.choice(chars_lst)) for _ in range(int(lenght))]
#
# def generate_passwords(count, length):
#     for _ in range(count):
#         password = generate_pass(length)
#         lower, upper, digits = False, False, False
#         while not lower and not upper and not digits:
#             for c in password:
#                 if c.isdigit() and not digits:
#                     digits = True
#                 elif c.islower() and not lower:
#                     lower = True
#                 elif c.isupper() and not upper:
#                     upper = True
#                 if lower and upper and digits:
#                     break
#             if lower and upper and digits:
#                 break
#             password = generate_pass(length)
#             lower, upper, digits = False, False, False
#         if lower and upper and digits:
#             print(''.join(password))
#
# generate_passwords(count = int(input()), length = int(input()))


# import random
#
# n = 10 ** 6
# k = 0
# s0 = 4
# for _ in range(n):
#     x = random.uniform(-1, 1)  # случайное число с плавающей точкой от 0 до 1
#     y = random.uniform(-1, 1)  # случайное число с плавающей точкой от 0 до 1
#
#     if x ** 2 + y ** 2 <= 1:  # если попадает в нужную область
#         k += 1
#
# print((k / n) * s0)


# import random
#
# def is_sort(nums):                   # отсортирован ли список?
#     for i in range(len(nums) - 1):
#         if nums[i] > nums[i + 1]:
#             return False
#     return True
#
# def bogosort(nums):                  # реализация алгоритма болотной сортировки
#     while not is_sort(nums):
#         random.shuffle(nums)
#     return nums
#
# numbers = list(range(10))
# random.shuffle(numbers)              # перемешиваем начальный список
# print(numbers)                       # выводим начальный список
#
# sorted_numbers = bogosort(numbers)
#
# print(sorted_numbers)
