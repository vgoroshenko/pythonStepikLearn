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


# def range_sum(numbers, start, end):
#     if start == end:
#         return numbers[start]
#     else:
#         return numbers[start] + range_sum(numbers, start + 1, end)
#
#
# print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))


# def get_pow(a, n):
#     if n == 0:
#         return 1
#     else:
#         return a * get_pow(a, (n - 1))
#
# print(get_pow(2, 10))


# def get_fast_pow(a, n):
#     if n == 0:
#         return 1
#     else:
#         if n % 2 == 0:
#             return get_fast_pow(a * a, n / 2)
#         else:
#             return a * get_fast_pow(a, n - 1)
#
#
# print(get_fast_pow(2, 10))
# print(get_fast_pow(5, 2))
# print(get_fast_pow(2, 100))


# def recursive_sum(a, b):
#     if b == 0:
#         return 0
#     else:
#         return a + recursive_sum(a + 1, b - 1)
#
#
# print(recursive_sum(10, 22))
# print(recursive_sum(99, 0))
# print(recursive_sum(0, 0))


# def is_power(number: int, ch = 2) -> bool:
#     if number == 1 or number == ch:
#         return True
#     else:
#         if ch <= number:
#             return is_power(number, ch*2)
#         else:
#             return False
#
# print(is_power(512))
# print(is_power(15))


cache = {1: 1, 2: 1, 3: 1}


# def tribonacci(n):
#     res = cache.get(n)
#     if res is None:
#         res = tribonacci(n - 3) + tribonacci(n - 2) + tribonacci(n - 1)
#         cache[n] = res
#     return res
#
# print(tribonacci(7))
# print(tribonacci(4))


#def is_palindrome(string):











