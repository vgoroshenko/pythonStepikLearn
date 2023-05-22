# def convert(num):
#     return (bin(num)[2:], oct(num)[2:], hex(num)[2:].upper(), '%X' % num) if num >= 0 else ('-'+bin(num)[3:], '-'+oct(num)[3:], '-'+hex(num)[3:])

# def convert(n):
#     return f'{n:b}', f'{n:o}', f'{n:X}'
#
# print(convert(15))
# print(convert(-24))
# print(convert(1))

# films = {'Spider-Man: No Way Home': {'imdb': 8.8, 'kinopoisk': 8.3},
#          'Don"t Look Up': {'imdb': 7.3, 'kinopoisk': 7.6},
#          'Encanto': {'imdb': 7.3, 'kinopoisk': 7.4},
#          'The Witcher': {'imdb': 8.2, 'kinopoisk': 7.3},
#          'Ghostbusters: Afterlife': {'imdb': 7.3, 'kinopoisk': 8},
#          'Harry Potter 20th Anniversary: Return to Hogwarts': {'imdb': 8.1, 'kinopoisk': 8.2},
#          'Shingeki no Kyojin': {'imdb': 9.0, 'kinopoisk': 8.3},
#          'The Matrix': {'imdb': 8.7, 'kinopoisk': 8.5},
#          'The Dark Knight': {'imdb': 9.0, 'kinopoisk': 8.5},
#          'The Shawshank Redemption': {'imdb': 9.3, 'kinopoisk': 9.1},
#          'Avengers: Endgame': {'imdb': 8.4, 'kinopoisk': 7.7}}
#
# [print(k) for k, v in films.items() if v == min(films.values(), key=lambda x: (x['imdb'] + x['kinopoisk']) / 2)]
#
# print(min(films, key=lambda x: (films[x]['imdb'] + films[x]['kinopoisk']) / 2))


# def non_negative_even(numbers):
#     return all(map(lambda x: True if x % 2 == 0 and x >= 0 else False, numbers))
#
#
# print(non_negative_even([2, 4, 8, 16]))
# print(non_negative_even([-8, -4, -2, 0, 2, 4, 8]))


# def is_greater(list, number):
#     return any(map(lambda x: True if sum(x) > number else False, list))
#
# data = [[-3, 4, 0, 1], [1, 1, -4], [0, 0], [9, 3]]
#
# print(is_greater(data, 10))
#
# data = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
#
# print(is_greater(data, 2))


# def custom_isinstance(object, typeinfo):
#     return len([i for i in object if isinstance(i, typeinfo)])
#
# numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
# print(custom_isinstance(numbers, (int, float)))
#
# numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
# print(custom_isinstance(numbers, int))


# numbers = [-7724, 5023, 3197, -102, -4129, -880, 5857, -2866, -8913, 1195, 9809, 5347, -8071, 903, 3030, -4347, -3354, 1024, 8670, 4210, -5228, 8900, 4823, -2002, 4900, 9520, -3658, 1104, -9554, 3064, 9632, -8701, 3384, 4370, 2034, 7822, -9694, 3347, 7440, -8459, 3238, -5193, -3381, 5281, 9022, 5559, 7593, -6540, -6204, -2483, 8729, 5810, -8254, -9846, -1801, 4882, 3838, -3140, 7609, -3325, 6026, 2994, -1677, 1266, -1893, -4408, -5722, -2841, 9812, 5837, -7474, 4624, -664, 6998, 7888, -971, 8810, 3812, -5396, 2593, 512, -4634, 9735, -3062, 9031, -9300, 3657, 6332, 7552, 8125, -725, 4392, 1727, 8194, -2828, -4314, -8967, -7912, -1363, -5957]
#
# print(numbers.index(max(numbers)))


# def my_pow(numbers):
#     my_len = len(str(numbers))
#     if my_len == 1:
#         return numbers
#     else:
#         return (numbers % 10) ** my_len + my_pow(numbers // 10)
#
#
# print(my_pow(139))
# print(my_pow(123))
# print(my_pow(0))

# names = ['Moana', 'Cars', 'Zootopia', 'Ratatouille', 'Coco', 'Inside Out', 'Finding Nemo', 'Frozen']
# budgets = [150000000, 120000000, 150000000, 150000000, 180000000, 175000000, 94000000, 150000000]
# box_offices = [643331111, 462216280, 1023784195, 620702951, 807082196, 857611174, 940335536, 1280802282]
#
# [print(f'{i[0]}: {i[2]-i[1]}$') for i in sorted(zip(names, budgets, box_offices))]


# def zip_longest(*args, fill=None):
#     [i.extend([fill] * (len(max(args, key=len)) - len(i))) for i in args if len(i) < len(max(args, key=len))]
#     return list(zip(*args))
#
#
# print(zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_'))
#txt = sorted('n0tEast3rEgg')
print(''.join(sorted(sorted(input()), key=lambda x: (x.islower(), x.isupper(), int(x) % 2 if x.isdigit() else False), reverse=True)))

















