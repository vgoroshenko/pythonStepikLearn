# matrix  = [[2, -5, -11, 0],
#            [-9, 4, 6, 13],
#            [4, 7, 12, -2]]
#
# print(matrix[1][2])


# def print_matrix(matrix, n, width=2):
#     for r in range(n):
#         for c in range(n):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()
#
# # n = int(input())
# # matrix = []
# # for i in range(n):
# #     temp = [int(num) for num in input().split()]
# #     matrix.append(temp)
#
# n = 4
# matrix = [[0]*n for _ in range(n)]
#
# for i in range(n):                     # заполняем главную диагональ единицами, а побочную двойками
#     matrix[i][i] = 1
#     matrix[i][n-i-1] = 2
#
# print_matrix(matrix, n)


# def print_matrix(matrix, n):
#     for i in range(int(input())):
#         for j in range(int(input())):
#             print(input(), end=' ')

# rows = int(input())
# cols = int(input())
#
# # for i in range(rows):
# #     for j in range(cols):
# #         print(*[_ for _ in input().split()], end=' ')
# #     print()
#
# def print_matrix(rows, cols):
#     matrix = []
#     for _ in range(rows):
#         temp = [input() for _ in range(cols)]
#         matrix.append(temp)
#     for r in range(rows):
#         for c in range(cols):
#             print(str(matrix[r][c]), end=' ')
#         print()
#
# print_matrix(rows, cols)

# rows = int(input())
# cols = int(input())
# matrix = []
# for _ in range(rows):
#     temp = [input() for _ in range(cols)]
#     matrix.append(temp)
#
# def print_matrix(row, col):
#     for r in range(row):
#         for c in range(col):
#             print(str(matrix[r][c]), end=' ')
#         print()
#     print()
#     print_revert_matrix(row, col)
#
# def print_revert_matrix(row, col):
#     for r in range(col):
#         for c in range(row):
#             print(str(matrix[c][r]), end=' ')
#         print()
#
# print_matrix(rows, cols)

#След матрицы
# rows = int(input())
# total = 0
# matrix = [input().split() for _ in range(rows)]
# for i in range(rows):
#     total += int(matrix[i][i])
# print(total)

#Больше среднего
# rows = int(input())
# matrix = [input().split() for _ in range(rows)]
# for i in range(rows):
#     sred_arifmed = sum([int(i) for i in matrix[i]]) // len(matrix[i])
#     total = 0
#     for j in range(len(matrix[i])):
#         if int(matrix[i][j]) > sred_arifmed:
#             total += 1
#     print(total)

#Максимальный в области 1
# rows = int(input())
# matrix = [input().split() for _ in range(rows)]
# temp = []
# for i in range(rows):
#     for j in range(rows):
#         temp.append(int(matrix[i][j]))
#         if i == j:
#             break
# print(max(temp))


# rows = int(input())
# matrix = [input().split() for _ in range(rows)]
# temp = []
# for i in range(rows):
#     for j in range(rows):
#         temp.append(int(matrix[i][j]))
#         if i == j and j == rows - i - 1:
#             break
# print(max(temp))

# rows = int(input())
# matrix = [input().split() for _ in range(rows)]
# temp = []
# for i in range(rows):
#     for j in range(rows):
#         if i > j and i < rows - 1 - j:
#             temp.append(int(matrix[i][j]))
#         if i < j and i > rows - 1 - j:
#             temp.append(int(matrix[i][j]))
#         if i == j or i == rows - j - 1:
#             temp.append(int(matrix[i][j]))
# print(max(temp))

# rows = int(input())
# matrix = [input().split() for _ in range(rows)]
# temp_1 = []
# temp_2 = []
# temp_3 = []
# temp_4 = []
# for i in range(rows):
#     for j in range(rows):
#         if i < j and i < rows - 1 - j:
#             temp_1.append(int(matrix[i][j]))
#         if i < j and i > rows - 1 - j:
#             temp_2.append(int(matrix[i][j]))
#         if i > j and i < rows - 1 - j:
#             temp_3.append(int(matrix[i][j]))
#         if i > j and i > rows - 1 - j:
#             temp_4.append(int(matrix[i][j]))
# print(f'Верхняя четверть: {sum(temp_1)}')
# print(f'Правая четверть: {sum(temp_2)}')
# print(f'Нижняя четверть: {sum(temp_4)}')
# print(f'Левая четверть: {sum(temp_3)}')

#Таблица умножения
# rows, cols = int(input()), int(input())
# matrix = [[_] * cols for _ in range(rows)]
#
# for i in range(rows):
#     for j in range(cols):
#         matrix[i][j] = i * j
#
# def print_matrix(matrix, row, col):
#     for r in range(row):
#         for c in range(col):
#             print(str(matrix[r][c]), end=' ')
#         print()
#
# print_matrix(matrix, rows, cols)

#Максимум в таблице
# rows, cols = int(input()), int(input())
# matrix = [input().split() for _ in range(rows)]
# max_lst = [0, 0]
#
# def print_matrix(matrix, row, col):
#     max_temp = matrix[0][0]
#     for r in range(row):
#         for c in range(col):
#             if int(matrix[r][c]) > int(max_temp):
#                 max_temp = matrix[r][c]
#                 max_lst.clear()
#                 max_lst.extend([r, c])
#     print(*max_lst)
#
#
# print_matrix(matrix, rows, cols)


# rows, cols = int(input()), int(input())
# matrix = [input().split() for _ in range(rows)]
# exp_cols = [int(i) for i in input().split()]
#
# # def expand_matrix(matrix, row, col):
# #     for r in range(row):
# #         for c in range(col):
# #             matrix[c][r] = 1
# #     print(matrix)
#
# for r in range(exp_cols[0]):
#     for c in range(exp_cols[1]):
#         matrix[r][c] = matrix[c][r]
#
# def print_matrix(matrix, row, col):
#     for r in range(row):
#         for c in range(col):
#             print(str(matrix[r][c]), end=' ')
#         print()
#
# #expand_matrix(matrix, exp_cols[0], exp_cols[1])
# print_matrix(matrix, rows, cols)

# n, m = int(input()), int(input())    # считываем значения n и m
#
# my_list = [[0] * m for _ in range(n)]
# my_list[0][0] = 17
# print(my_list)

#сложение матриц
# rows_cols = [int(_) for _ in input().split()]
# rows = rows_cols[0]
# cols = rows_cols[1]
#
# matrix = [[int(_) for _ in input().split()] for _ in range(rows)]
# matrix1 = [[int(_) for _ in input().split()] for _ in range(rows + 1)]
# matrix1.remove([])
#
# def addition_matrix(matrix, matrix1, row, col):
#     for r in range(row):
#         for c in range(col):
#             print(matrix[r][c] + matrix1[r][c], end=' ')
#         print()
#
# addition_matrix(matrix, matrix1, rows, cols)

#умножение матриц
# rows_cols_one = [int(_) for _ in input().split()]
# matrix = [[int(_) for _ in input().split()] for _ in range(rows_cols_one[0])]
# input()
# rows_cols_two = [int(_) for _ in input().split()]
# matrix1 = [[int(_) for _ in input().split()] for _ in range(rows_cols_one[0])]
# print(rows_cols_one, matrix, rows_cols_two, matrix1, sep='\n')
#
# rows = rows_cols_one[0]
# cols = rows_cols_one[1]
#
#
# def multiplication_matrix(matrix, matrix1, row, col):
#     for r in range(row):
#         for c in range(col):
#             print(matrix[r][c] * matrix1[c][r], end=' ')
#         print()
#
# multiplication_matrix(matrix, matrix1, rows, cols)


print(22 // 3 + 22 % 3)
