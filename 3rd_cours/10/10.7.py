# from collections import namedtuple
#
# Person = namedtuple('Person', ['name', 'nationality', 'sex', 'birth', 'death'])
#
# persons = [Person('E. M. Ashe', 'American', 'male', 1867, 1941),
#            Person('Goran Aslin', 'Swedish', 'male', 1980, 0),
#            Person('Erik Gunnar Asplund', 'Swedish', 'male', 1885, 1940),
#            Person('Genevieve Asse', 'French', 'female', 1949, 0),
#            Person('Irene Adler', 'Swedish', 'female', 2005, 0),
#            Person('Sergio Asti', 'Italian', 'male', 1926, 0),
#            Person('Olof Backman', 'Swedish', 'male', 1999, 0),
#            Person('Alyson Hannigan', 'Swedish', 'female', 1940, 1987),
#            Person('Dana Atchley', 'American', 'female', 1941, 2000),
#            Person('Monika Andersson', 'Swedish', 'female', 1957, 0),
#            Person('Shura_Stone', 'Russian', 'male', 2000, 0),
#            Person('Jon Bale', 'Swedish', 'male', 2000, 0)]
#
# live = (i for i in persons if i.death == 0)
# male = (i for i in live if i.sex == 'male')
# country = (i for i in male if i.nationality == 'Swedish')
#
# print(max(country, key=lambda x: x.birth).name)


# def parse_ranges(range_list: str):
#     text_filter = (i.split('-') for i in range_list.split(',') )
#     range_filter = ([j for j in range(int(i[0]), int(i[1]) + 1)] for i in text_filter)
#     return (i for it in range_filter for i in it)
#
# print(*parse_ranges('1-10,2-10'))


# def filter_names(names: list, ignore_char: str, max_names: int):
#     char_digit_filter = (i for i in names if i[0].lower() != ignore_char.lower() and all(map(lambda x: x.isalpha(), i)))
#     tmp_filter = (i[1] for i in enumerate(char_digit_filter, 1) if not i[0] > max_names)
#     return tmp_filter
#
#
# data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']
#
# print(*filter_names(data, 't', 20))


# def invest(file):
#     with open(file, 'r', encoding='UTF-8') as f:
#         file_lines = (line for line in f)
#         line_values = (line.rstrip().split(',') for line in file_lines)
#         file_hader = next(line_values)
#         line_dicts = (dict(zip(file_hader, data)) for data in line_values)
#         sum_invest = sum(int(i['raisedAmt']) for i in line_dicts if i['round'] == 'a')
#         print(sum_invest)
#
# invest('data.csv')

# from datetime import date, timedelta
#
# def years_days(year):
#     def check_year(year):
#         return 366 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 365
#     return (date(year, 1, 1) + timedelta(days=i) for i in range(check_year(year)))
#
#
# dates = years_days(2022)
#
# print(next(dates))
# print(next(dates))
# print(next(dates))
# print(next(dates))

# def nonempty_lines(file):
#     with open(file, 'r', encoding='UTF-8') as f:
#         lines = (i for i in f.readlines() if len(i.strip()) > 0)
#         strip_lines = (i.strip() for i in lines)
#         return (i if len(i) <= 25 else '...' for i in strip_lines)
#
# lines = nonempty_lines('file1.txt')
#
# print(next(lines))
# print(next(lines))
# print(next(lines))
# print(next(lines))


# def txt_to_dict():
#     with open('planets.txt', 'r', encoding='UTF-8') as f:
#         list_lines = (i.split('\n') for i in f.read().split('\n\n'))
#         tuple_planets = (tuple(j.split(' = ') for j in i) for i in list_lines)
#         return (dict(i) for i in tuple_planets)
#
#
#
# planets = txt_to_dict()
#
# print(next(planets))

# from collections import Counter
# def unique(iterable):
#     return (i for i in Counter(iterable))
#
# iterator = iter('111222333')
# uniques = unique(iterator)
#
# print(next(uniques))
# print(next(uniques))
# print(next(uniques))


# def stop_on(iterable, obj):
#     for i in iterable:
#         if i == obj:
#             break
#         else:
#             yield i
#
# iterator = iter('beegeek')
#
# print(*stop_on(iterator, 'a'))


# def with_previous(iterable):
#     j = None
#     for i in iterable:
#         yield (i, j)
#         j = i
#
# iterator = iter('stepik')
#
# print(*with_previous(iterator))



# def pairwise(iterable):
#     if not iterable:
#         return iterable
#     it = iter(iterable)
#     j = it.__next__()
#     while True:
#         i = next(it, None)
#         yield (j, i)
#         if i is None:
#             break
#         j = i
#
# print(list(pairwise([])))


def around(iterable):
    if not iterable:
        return iterable
    it = iter(iterable)
    j = None
    x = it.__next__()
    while True:
        i = next(it, None)
        s = x
        yield (j, x, i)
        if i is None:
            break
        x = i
        j = s


numbers = [1, 2, 3, 4, 5]

print(*around(numbers))