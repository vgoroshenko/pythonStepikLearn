# n, X, Y, A, B = map(int, input().split())
#
# lst = list(range(1, n+1))
# lst[X-1:Y] = lst[X-1:Y][::-1]
# lst[A-1:B] = lst[A-1:B][::-1]
# print(*lst)

# def hide_card(a):
#     return '*' * 8 + ''.join(a.split(' '))[-4::]

# def same_parity(numbers):
#     return [i for i in numbers if i % 2 == numbers[0] % 2]

# def is_valid(pin):
#     return all(map(lambda x: x.isnumeric(), pin)) and len(pin) in range(4,7)

# def print_given(*args, **kwargs):
#     for i in args:
#         print(i, type(i))
#     for k, v in sorted(kwargs.items()):
#         print(k, v, type(v))


# def convert(str):
#     flag = 0
#     for i in str:
#         if i.isupper() and i.isalpha():
#             flag += 1
#         elif i.islower() and i.isalpha():
#             flag -= 1
#     return str.upper() if flag > 0 else str.lower()


# def filter_anagrams(word, *args):
#     return list(filter(lambda x: sorted(x.lower()) == sorted(word.lower()), *args))

# answers = (f'Никто не оценил данную запись',
#            'оценил(а) данную запись',
#            'оценили данную запись',
#            'других оценили данную запись')
#
#
# def likes(names):
#     if len(names) == 0:
#         tmp = answers[0]
#         return tmp
#     elif len(names) == 1:
#         tmp = *names, answers[1]
#         return ' '.join(tmp)
#     elif len(names) == 2:
#         tmp = *[i + ' и' for i in names[:-1]], names[-1], answers[2]
#         return ' '.join(tmp)
#     elif len(names) > 2:
#         if len(names) == 3:
#             tmp = f'{names[0]}, {names[1]}', f'и {names[-1]}', answers[2]
#             return ' '.join(tmp)
#         else:
#             tmp = f'{names[0]}, {names[1]}', f'и {len(names) - 2}', answers[3]
#             return ' '.join(tmp)


# def index_of_nearest(lst, num):
#     if lst == []:
#         return -1
#     tmp = list(map(lambda x: abs(num - x), lst))
#     return tmp.index(min(tmp))



# def spell(*args):
#     dct = {}
#     for i in args:
#         if i[0].lower() not in dct:
#             dct[i[0].lower()] = 0
#     for key in dct.keys():
#         for word in args:
#             if word[0].lower() == key and len(word) > dct[key]:
#                 dct[key] = len(word)
#     return dct

# def choose_plural(num, words):
#     if num % 100 in range (10, 20):
#         return f'{num} {words[2]}'
#     else:
#         tnum = num % 10
#         if tnum in range(5, 20) or tnum == 0:
#             return f'{num} {words[2]}'
#         elif tnum in range(2, 5):
#             return f'{num} {words[1]}'
#         elif tnum == 1:
#             return f'{num} {words[0]}'


# import random
# from functools import reduce
#
# def get_biggest(numbers):
#     if numbers == []:
#         return -1
#     else:
#         new_lst = []
#         len_num = range(1, len(numbers) + 1)
#         count_num = reduce(lambda a, b: a * b, len_num, 1)
#         while len(new_lst) != count_num:
#             random.shuffle(numbers)
#             tmp_num = ''.join(map(str, numbers))
#             if tmp_num not in new_lst:
#                 new_lst.append(tmp_num)
#         return max(new_lst)
# print(get_biggest([1, 2, 3]))
# print(get_biggest([61, 228, 9, 3, 11]))
# print(get_biggest([7, 71, 72]))
# print(get_biggest([13, 221, 423, 53, 1, 2, 33, 58, 78554, 34, 65, 65, 2, 1]))

# en = 'AaBCcEeHKMOoPpTXxy'
# ru = 'АаВСсЕеНКМОоРрТХху'
#
# tmp = [int(*['1' if i in en else '0' for i in input()]) for i in range(3)]
# if sum(tmp) == 3:
#     print('en')
# elif sum(tmp) == 0:
#     print('ru')
# else:
#     print('mix')


# nums = list(map(int, input().split()))
# print(set(nums))
# tmp = []
# for i in nums:
#     if nums.count(i) > 1 and i not in tmp:
#         tmp.append(i)
# print(*sorted(tmp))

# n = [_ for _ in range(1, int(input()) + 1)]
# #tmp = map(lambda x: [i for i in x.split()] if len(str(x)) > 1 else (x), n)
# tmp = []
# for i in n:
#     if len(str(i)) < 10:
#         tmp.append([i])
#     for j in n:
#         j = str(j)
#         sm = sum(map(int, list(j)))
#         if len(j) > 1 and sm == i:
#             tmp[i - 1].append(j)
# print(len(max(tmp, key=len)))

# n = [_ for _ in range(1, int(input()) + 1)]
# #tmp = map(lambda x: [i for i in x.split()] if len(str(x)) > 1 else (x), n)
# tmp = []
# for i in n:
#     if len(str(i)) > 1:
#         tmp.append(sum(map(int, list(str(i)))))
# asd = n + tmp
# asd = list(map(str, asd))
# tmp_dct = dict()
# print(tmp)
# print(asd)
# for i in set(asd):
#      tmp_dct[i] = asd.count(i)
# print(max(tmp_dct.values()))


# langs = [input().split(', ') for i in range(int(input()))]
# tmp = []
# for i in langs[0]:
#     if all(i in x for x in langs):
#         tmp.append(i)
# if tmp:
#     print(', '.join(sorted(tmp)))
# else:
#     print('Сериал снять не удастся')


# registered = [input() for i in range(int(input()))]
# new = [input() for i in range(int(input()))]
#
#
# for i in new:
#     new_count = 0
#     for j in registered:
#         if i in j:
#             num = j[len(i)].isnumeric()
#     if new_count > 0:
#         print(f'{i}{new_count}@beegeek.bzz')
#     else:
#         print(f'{i}@beegeek.bzz')


def digit_sum(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum

n = int(input())
numbers = list(range(1, n+1))
d = {}

for num in numbers:
    sum = digit_sum(num)
    if sum not in d:
        d[sum] = [num]
    else:
        d[sum].append(num)
max_len = 0

for key in d:
    if len(d[key]) > max_len:
        max_len = len(d[key])

for key in d:
    if len(d[key]) == max_len:
        print(len(d[key]))
        break
