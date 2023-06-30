# from sys import getsizeof
# range_object = iter(range(1000000))
# print(getsizeof(range_object))

# def cubes_of_odds(iterable):
#     return (i ** 3 for i in iterable if i % 2)
#
# evens = [2, 4, 6, 8, 10]
#
# print(*cubes_of_odds(evens))


# def is_prime(number):
#     if number == 1:
#         return False
#     else:
#         generator = (i for i in range(2, number) if number % i == 0)
#     try:
#         next(generator)
#         return False
#     except StopIteration:
#         return True
#
# print(is_prime(8))


# def count_iterable(iterable):
#     return sum(1 for _ in iterable)
#
# numbers = iter([1, 2, 3, 4, 5, 6, 7])
#
# print(count_iterable(numbers))


# def all_together(*iterables):
#     return (i for it in iterables for i in it)
#
# objects = [range(3), 'bee', [1, 3, 5], (2, 4, 6)]
#
# print(*all_together(*objects))


def interleave(*args):
    return (i for it in zip(*args) for i in it)

print(*interleave('bee', '123'))













