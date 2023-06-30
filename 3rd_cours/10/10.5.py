# def generate_ints(n):
#     for num in range(n):
#         yield num
#
# gen1 = generate_ints(5)
#
# print(*gen1)


# def generate_AB():
#     print('start')
#     yield 'A'
#     print('continue')
#     yield 'B'
#     print('end')
#
# asd = generate_AB()
#
# print(next(asd))
# print(next(asd))
# print(next(asd))

# def bee():
#     yield 'b'
#     yield 'e'
#     yield 'e'
#
# # print(next(bee()))
# # print(next(bee()))
# # print(next(bee()))
#
# asd = bee()
#
# print(next(asd))
# print(next(asd))
# print(next(asd))


# def simple_sequence():
#     num = 1
#     while True:
#         for i in range(num):
#             yield num
#         num += 1
#
# generator = simple_sequence()
#
# print(next(generator))
# print(next(generator))
#
# generator = simple_sequence()
# numbers = [next(generator) for _ in range(10)]
#
# print(*numbers)


# def alternating_sequence(count = None):
#     if count:
#         tmp_count = 1
#         for i in range(1, count + 1):
#             yield tmp_count if tmp_count % 2 else -tmp_count
#             tmp_count += 1
#     else:
#         count = 1
#         while True:
#             yield count if count % 2 else -count
#             count += 1
#
# generator = alternating_sequence()
#
# print(next(generator))
# print(next(generator))
#
#
# generator = alternating_sequence(10)
#
# print(*generator)


# def primes(left, right):
#     for num in range(left, right + 1):
#         if all(num % i != 0 for i in range(2, num)) and num != 1:
#             yield num
#
# generator = primes(1, 15)
#
# print(*generator)


# def reverse(sequence):
#     for i in sequence[::-1]:
#         yield i
#
# print(*reverse([1, 2, 3, 4, 5]))
#
# generator = reverse('beegeek')
#
# print(type(generator))
# print(*generator)

# from datetime import date, timedelta
#
# def dates(start, count = None, n = 0):
#     while n != count:
#         try:
#             n += 1
#             yield start
#             start += timedelta(days=1)
#         except StopIteration:
#             yield start
#
#
#
# generator = dates(date(2022, 3, 8))
#
# print(next(generator))
# print(next(generator))
# print(next(generator))
#
# generator = dates(date(2022, 3, 8), 5)
#
# print(*generator)


# mast = ("пик", "треф", "бубен", "червей")
# card = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз")
# cards = []
# [[cards.append((j, i)) for j in card] for i in mast]
#
# def card_deck(suit):
#     while True:
#         for i in cards:
#             if suit not in i:
#                 yield ' '.join(i)
#
# generator = card_deck('пик')
#
# print(next(generator))
# print(next(generator))
# print(next(generator))
#
# generator = card_deck('треф')
# cards = [next(generator) for _ in range(40)]
#
# print(*cards)


# def matrix_by_elem(matrix):
#     for row in matrix:
#         yield from row
#
#
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
#
# print(*matrix_by_elem(matrix))


def flatten(nested_list):
    for i in nested_list:
        yield from flatten(i)

generator = flatten([[1, 2], [[3]], [[4], 5]])

print(*generator)










