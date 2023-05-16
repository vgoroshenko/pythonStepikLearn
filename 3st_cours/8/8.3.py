# def factorial(n):
#     if n == 0:
#         return 1                        # базовый случай
#     else:
#         return n * factorial(n-1)       # рекурсивный случай
#
# print(factorial(4))
#
#
# def sum_to(n):
#     if n == 0:
#         return 0                       # базовый случай
#     else:
#         return n + sum_to(n - 1)
#
# print(sum_to(5))


# def sum_to(n):
#     n = list(map(int, n))
#     if not n:
#         return 0                       # базовый случай
#     else:
#         return n[0] + sum_to(n[1:])
#
# print(sum_to(input()))

# def number_of_frogs(year):
#     f = 1
#     if year == 1:
#         return 77
#     else:
#         return 3 * ((f * number_of_frogs(year - 1)) - 30)
#
# print(number_of_frogs(10))


def range_sum(numbers, start, end):
    if start == end:
        return numbers[start]
    else:
        return numbers[start] + range_sum(numbers, start + 1, end)


print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))