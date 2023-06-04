# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# it = iter(numbers)
# print(next(it))
# numbers.clear()
# print(next(it))


# def filterfalse(fnc, obj):
#     return filter(lambda x: fnc(x) is False, obj)
#
# objects = [0, 1, True, False, 17, []]
#
# print(*filterfalse(None, objects))
#
#
# numbers = (1, 2, 3, 4, 5)
#
# print(*filterfalse(lambda x: x % 2 == 0, numbers))

# def transpose(matrix):
#     return list(map(list, zip(*matrix)))
#
# matrix = [['1', '2'],
#           ['4', '5'],
#           ['7', '8'],
#           ['3', 4],
#           [True, None],
#           [9, 80],
#           [1, -1]]
#
# print(transpose(matrix))
#
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
#
# for row in transpose(matrix):
#     print(row)


# def get_min_max(data):
#     return (data.index(min(data)), data.index(max(data))) if data else None
#
# data = [1, 1, 2, 3, 8, 8]
#
# print(get_min_max(data))


# def starmap(fnc, iterable):
#     return map(fnc, *zip(*iterable))
#
#
# pairs = [(1, 3), (2, 5), (6, 4)]
#
# print(*starmap(lambda a, b: a + b, pairs))

import copy

def get_min_max(iterable):
    min_it = copy.deepcopy(iterable)
    max_it = copy.deepcopy(iterable)
    try:
        next(iter(iterable))
    except:
        return None
    return (min(min_it), max(max_it))


iterable = iter(range(10))

print(get_min_max(iterable))

iterable = [6, 4, 2, 33, 19, 1]

print(get_min_max(iterable))

iterable = iter([])

print(get_min_max(iterable))

data = iter(range(100_000_000))

print(get_min_max(data))






