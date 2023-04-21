# tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
# # while () in tuples:
# #     tuples.remove(())
# non_empty_tuples = [_ for _ in tuples if _ != ()]
#
# print(non_empty_tuples)


# tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
# for i in range(len(tuples)):
#     tuples[i] = list(tuples[i])
#     tuples[i][-1] = 100
#     tuples[i] = tuple(tuples[i])
# #new_tuples =
# print(tuples)

# poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
# poet_data = tuple(list(poet_data[:2]) + ['Москва'])
#
# print(poet_data)

# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
# arith_num = []
# for tupl in numbers:
#     tmp = sum(tupl) / len(tupl)
#     arith_num.append(tmp)
# print(arith_num)


# a, b, c = int(input()), int(input()), int(input())
# x = -b / (2 * a)
# y = (a * x ** 2) + (b * x) + c
# tmp = [x, round(y, 1)]
# print(tuple(tmp))


# n = int(input())
# study_tupl = []
# for i in range(n):
#     tmp_list = [_ for _ in input().split()]
#     tmp_list[1] = int(tmp_list[1])
#     study_tupl.append(tuple(tmp_list))
#     print(*tmp_list)
# study_tupl = tuple(study_tupl)
#
# print()
# for i in range(len(study_tupl)):
#     if study_tupl[i][1] == 4 or study_tupl[i][1] == 5:
#         print(*study_tupl[i])

# n = int(input())
# f1, f2 = 1, 1
# for i in range(n):
#     print(f1)
#     f1, f2 = f2, f1 + f2


# n = int(input())
# f1, f2, f3 = 1, 1, 1
# for i in range(n):
#     print(f1, end=' ')
#     f1, f2, f3 = f2, f3, f1 + f2 + f3

# b, c = 4, 5
# a = ((c ** 2) - (b ** 2)) ** 0.5
# print(a)

a = 47
b = 35
x = 23

q = a - x
z = b - x

t = q + z + x

print(t)