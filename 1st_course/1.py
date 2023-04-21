# a, b = int(input()), int(input())
#
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print((a ** 10 + (b ** 10)) ** 0.5)
#
# asd = ['+', '-', '*', '/', '//', '%']

# #[(a int(i) b) for i in asd]
# for i in asd:
#     #k = int(i)
#     print(eval(f'{a} {i} {b}'))

# for i in range(len(asd)):
#     print((a int(asd[i]) b))

#print(a, int(asd[0]), b)


# a, b = float(input()), float(input())
# imt = a / b ** 2
# if imt < 18.5:
#     print('Недостаточная масса')
# elif imt > 25:
#     print('Избыточная масса')
# else:
#     print('Оптимальная масса')

# txt = len(input())
# txt *= 60
# print((txt // 100), 'р.', (txt % 100), 'коп.')

#print(len(input().split()))

# znak = ['Дракон', 'Змея', 'Лошадь', 'Овца', 'Обезьяна', 'Петух', 'Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр', 'Заяц']
#
# year = {0:"Обезьяна", 1:"Петух", 2:"Собака", 3:"Свинья", 4:"Крыса", 5:"Бык", 6:"Тигр", 7:"Заяц", 8:"Дракон", 9:"Змея", 10:"Лошадь", 11:"Овца"}
#
# animals = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца"]
#
# num = int(input())
# print(animals[num % 12])
# if num > 1000:
#     print(animals[num // 100 % 12])
# elif num > 100:
#     print(animals[num // 10 % 12])
# else:
#     print(animals[num % 12])


# num = input()
#
# if len(num) == 5:
#     print(int(num[-1::-1]))
# else:
#     print(num[:len(num) - 5], num[-1:len(num) - 6:-1], sep='')

# num = list(input())
# num.reverse()
# for i in range(0, len(num), 3):
#     num[i] = num[i] + ','
# num.reverse()
# print(''.join(num)[:-1])



# start_num = [_ for _ in range(1, int(input()) + 1)]
# del_count = int(input())
# while len(start_num) != 1:
#     if len(start_num) == 2:
#         start_num = start_num[-1]
#         break
#     start_num = start_num[::del_count]
#     start_num.insert(0, start_num[-1])
#     start_num = start_num[:-1]
# print(start_num)

# n, k = int(input()), int(input())
# asd = 0
#
# for i in range(1, n + 1):
#     asd = (asd + k) % i
# print(asd + 1)



#Координатные четверти
# one_quart = 0
# two_quart = 0
# three_quart = 0
# four_quart = 0
# quart_count = 0
#
# coord_list = [input().split() for _ in range(int(input()))]
#
# for i in coord_list:
#     x = int(i[0])
#     y = int(i[1])
#     if x > 0 and y > 0:
#         one_quart += 1
#     elif x < 0 and y > 0:
#         two_quart += 1
#     elif x < 0 and y < 0:
#         three_quart += 1
#     elif x > 0 and y < 0:
#         four_quart += 1
#
# print(f'Первая четверть: {one_quart}', f'Вторая четверть: {two_quart}', f'Третья четверть: {three_quart}', f'Четвертая четверть: {four_quart}', sep='\n')
# digit_list = input().split()
# digit_count = 0
# big_digit = digit_list[0]
#
# for i in range(len(digit_list)):
#     if digit_list[i] > big_digit:
#         digit_count += 1
#         big_digit = digit_list[i]
#     # elif digit_list[i] == big_digit:
#     #     digit_count += 1
# print(digit_count)

# digit_list = [int(i) for i in input().split()]
# digit_count = 0
#
# for i in range(1, len(digit_list)):
#     if digit_list[i] > digit_list[i - 1]:
#         digit_count += 1
# print(digit_count)

# def test():
#     for i in range(1, len(digit_list)):
#         if i % 2 != 0:
#             asd = 's' * 2

# digit_list = [int(i) for i in input().split()]
# if len(digit_list) % 2 != 0:
#     for i in range(1, len(digit_list), 2):
#         if i % 2 != 0:
#             digit_list.insert(i + 1, digit_list[i - 1])
#             del digit_list[i - 1]
# else:
#     for i in range(1, len(digit_list) + 1, 2):
#         if i % 2 != 0:
#             digit_list.insert(i + 1, digit_list[i - 1])
#             del digit_list[i - 1]
# print(*digit_list)


# digits = [int(i) for i in input().split()]
# digits.insert(0, digits.pop())
# print(*digits)

# digits = [int(i) for i in input().split()]
# d_count = 1
# for i in range(1, len(digits)):
#     if digits[i] != digits[i - 1]:
#         d_count +=1
# print(d_count)
# digits = [int(input()) for _ in range(int(input()))]
# total = int(input())
# flag = False
#
# # for i in digits:
# #     for s in range(1, len(digits)):
# #         if i * digits[s] == total:
# #             flag = True
# #             break
#
# for i in range(len(digits)):
#     for s in range(len(digits)):
#         if i != s and digits[i] * digits[s] == total:
#             flag = True
#             break
#
# if flag == True:
#     print('ДА')
# else:
#     print('НЕТ')

#Камень, ножницы, бумага
# first_person = input()
# second_person = input()
#
# asd = ['камень', 'ножницы', 'бумага']
#
# if first_person == asd[0] and second_person == asd[1] or first_person == asd[1] and second_person == asd[2] or first_person == asd[2] and second_person == asd[0]:
#     print('Тимур')
# elif first_person == second_person:
#     print('ничья')
# else:
#     print('Руслан')



# x, y = input(), input()
# var = ['камень', 'ножницы', 'бумага', 'ящерица', 'Спок']
# ans = ['ничья', 'Руслан', 'Тимур']
# print('ничья' if x == y else ans[(var.index(x) - var.index(y)) - 2])

# txt = [i for i in input().split('О') if i != '']
# print(len(max([_ for _ in txt if len(_) > 1])) if len(txt) > 1 else len(*txt))

# Орел и решка
# txt = [i for i in input().split('О') if i != '']
# print(len(max(txt)) if len(txt) > 0 else len(txt))

#Антон
# from itertools import groupby
# strings = int(input())
# word_search = 'anton'
# new = []
# # for i in range(strings):
# #     asd = [i for i in list(input()) if i in word_search]
# #     for s in asd:
# #         if s not in new:
# #             new.append(s)
# #     if ''.join(asd) == word_search:
# #         print(i + 1, end=' ')
#
# # for i in range(strings):
# #     for c in list(input()):
# #         if not c.isalpha():
# #             continue
# #         for s in word_search:
# #             if s == c and s not in new and new.count('n') < 2:
# #                 new.append(s)
# #                 break
# #     if ''.join(new) == word_search:
# #         print(i + 1)
#
#
# # for i in range(strings):
# #     asd = [i for i in list(input()) if i in word_search]
# #     print(list(set(asd)))
# #     new_asd = [el for el, _ in groupby(asd)]
# #     #y = sorted(set(asd), key=lambda d: asd.index(d))
# #     print(new_asd)
# #     qwe = ''.join(new_asd)
# #     if ''.join(new_asd) == word_search:
# #         new.append(i + 1)
# # print(*new)

# Роскомнадзор запретил букву а
# word = input() + ' запретил букву'
# char = [chr(_) for _ in range(1072, 1104)]
#
# for c in char:
#     if c in word:
#         print(word.strip(), c)
#         word = word.replace(c, '', word.count(c))
#         if '  ' in word.strip():
#             word = word.replace(' ', '', 1)

# string = list(input() + ' запретил букву')
# chars = [chr(_) for _ in range(1072, 1104)]
#
# for c in chars:
#     print(''.join(string).strip(), c)
#     while c in string or string in chars:
#         string.remove(c)
#     if '  ' in ''.join(string).strip():
#         string.remove(' ')

