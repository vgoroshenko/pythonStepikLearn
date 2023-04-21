# # объявление функции
# def func(num1, num2):
#     return num1 % num2 == 0
#
# # считываем данные
# num1, num2 = int(input()), int(input())
#
# # вызываем функцию
# if func(num1, num2):
#     print('делится')
# else:
#     print('не делится')

#Треугольник Паскаля 1
# def pascal(n):
#     for i in range(n):

##Упаковка дубликатов 🌶️
# s = 'a a a b c d'.split()
#
# from itertools import groupby
#
# print([[*v] for k,v in groupby(s)])

# str="aaaaabbbbbbbbbbbbbbccccccccccc"
# p = [0]
# for i, c in enumerate(zip(str, str[1:])):
#     if c[0] != c[1]:
#         p.append(i + 1)
# print(p)



#Разбиение на чанки 🌶️
# txt = input().split()
# n = int(input())
# new_lst = []

# def chunked(lst, num):
#     # for i in range(len(lst)):
#     #     if i % num:
#     #         new_lst.append([txt[i - 1], txt[i]])
#     # return new_lst

# def chunked1(lst, count):
#     start = 0
#     for i in range(count):
#         stop = start + len(lst[i::count])
#         yield lst[start:stop]
#         start = stop
#     return lst
#
#
# def chunked(lst, n):
#     return [lst[i:i + n] for i in range(0, len(lst), n)]
#
# a = chunked(txt, n)
#
# print(a)


