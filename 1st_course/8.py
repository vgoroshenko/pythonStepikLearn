# myset = set(['aaa', 'bbbb', 'cc'])
#
# print(myset)

# numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
# summ = 0
# for num in numbers:
#     summ += num ** 2
# print(summ)

# fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
# sorted_fruits = sorted(fruits, reverse=True)
# for fruit in sorted_fruits:
#     print(fruit)

# print(len(set(input())))

# a = input()
# print('YES') if len(a) == len(set(a)) else print('NO')

# a = [int(_) for _ in input()]
# b = [int(_) for _ in input()]
# q = set(a + b)
# flag = 1
# for i in range(10):
#     if i not in q:
#         flag = 0
#         break
# print('YES') if flag == True else print('NO')

# print('YES') if set(input()) == set(input()) else print('NO')
# a = input()
# list_a = a.split()
# print(set(a), set(list_a[1]+' '))
# print('YES') if set(list_a[1]+' ') == set(a) else print('NO')

# myset = {'python'}
#
# item = myset.pop()
# print(item, len(myset))

# myset = set()
# for i in range(10):
#     if i % 2 == 0:
#         myset.add('even')
#     else:
#         myset.add('odd')
# print(len(myset))


# for i in range(int(input())):
#     print(len(set(input().lower())))


# myset = set()
#
# for i in range(int(input())):
#     tmp_set = set(input().lower())
#     for letter in tmp_set:
#         myset.add(letter)
# myset = set(''.join(myset))
# print(len(myset))


# txt = input().lower()
#
# for c in '.,;:-?!':
#     if c in txt:
#         txt = txt.replace(c, '')
# print(txt)
# myset = set(txt.split())
# print(len(myset))


# char_list = input().split()
# tmp_list = []
# for c in char_list:
#     c = int(c)
#     if c not in tmp_list:
#         print('NO')
#         tmp_list.append(c)
#     else:
#         print('YES')


# set1 = set(input().split())
# set2 = set(input().split())
# set3 = set1 & set2
# print(len(set3))

# print(*(sorted(set([int(_) for _ in input().split()]) & set([int(_) for _ in input().split()]))))

# set1 = set(input().split())
# set2 = set(input().split())
# set3 = set(set1 & set2)
# print(sorted(set3))

# print(*(sorted(set([int(_) for _ in input().split()]) - set([int(_) for _ in input().split()]))))

# num = int(input())
# myset_list = []
# for _ in range(num):
#     myset_list += [set(int(_) for _ in input())]
# mytestset = myset_list[0]
# for i in range(1, num):
#     mytestset.intersection_update(myset_list[i])
# print(*sorted(mytestset))


# set1 = {2, 3}
# set2 = {1, 2, 3, 4, 5, 6}
#
# print(set1.issubset(set2))

# word = 'beegeek'
# set1 = set(word*3)
# set2 = set(word[::-1]*2 + 'stepik')
# print(word[::-1]*2)
# print(set1 < set2)

# set1 = {1, 2, 3, 4, 5}
# #set1 = {5, 6, 7}
# set2 = {5, 6, 8}
# set3 = {7, 8, 9}
# #
# # print(set1.isdisjoint(set2))
# # print(set1.isdisjoint(set3))
# # print(set2.isdisjoint(set3))
#
# print(set1 <= set2)

# set1 = {2, 3}
# set2 = {2, 3, 4, 5, 6}
#
# print(set1 < set2)


# print('NO') if set(input()).isdisjoint(set(input())) else print('YES')


# print('YES') if set(input()) > (set(input())) else print('NO')

# set1 = [int(_) for _ in input().split()]
# set2 = [int(_) for _ in input().split()]
# set3 = [int(_) for _ in input().split()]
#
# tmp = set(set1) & set(set2) - set(set3)
#
# print(*sorted(tmp, reverse=True))


# set1 = [int(_) for _ in input().split()]
# set2 = [int(_) for _ in input().split()]
# set3 = [int(_) for _ in input().split()]
# tmp = set()
# for i in set1:
#     if i in set2 and i not in set3:
#         tmp.add(i)
# print(*sorted(tmp, reverse=True))


# set1 = set([int(_) for _ in input().split()])
# set2 = set([int(_) for _ in input().split()])
# set3 = set([int(_) for _ in input().split()])
#
# print(*sorted((set1 | set2 | set3) - (set1 & set2 & set3)))


# set1 = set([int(_) for _ in input().split()])
# set2 = set([int(_) for _ in input().split()])
# set3 = set([int(_) for _ in input().split()])
#
# print(*sorted(set3 - (set1 | set2), reverse=True))


# set1 = {int(_) for _ in input().split()}
# set2 = set([int(_) for _ in input().split()])
# set3 = set([int(_) for _ in input().split()])
# set_m = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#
# print(*sorted(set_m - (set1 | set2 | set3)))


# words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
# myset = {c[0].lower() for c in words}
# print(*sorted(myset))

# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
#
# word_set = {word.strip('.,;:-?!()').lower() for word in sentence.split()}
#
# print(*sorted(word_set))


# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
#
# word_set = {word.strip('.,;:-?!()').lower() for word in sentence.split() if len(word.strip('.,;:-?!()').lower()) < 3}
#
# print(*sorted(word_set))


# files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']
#
# words = {word.lower() for word in files if '.png' in word.lower()}
#
# print(*sorted(words))


# n = input().split()
#
# set_n = set(n)
#
# print(len(n) - len(set_n))

# n = int(input())
#
# cities = {input() for _ in range(n)}
#
# if input() in cities:
#     print('REPEAT')
# else:
#     print('OK')


# home_n, summer_n = int(input()), int(input())
#
# home_set = {input() for _ in range(home_n)}
# #summer_set = {input() for _ in range(summer_n)}
#
# #asdhome_set = {{input() for _ in range(home_n)} for _ in input()}
# for i in range(summer_n):
#     if input() in home_set:
#         print('YES')
#     else:
#         print('NO')

# set1, set2 = {int(_) for _ in input().split()}, {int(_) for _ in input().split()}
#
# if set1.isdisjoint(set2):
#     print('BAD DAY')
# else:
#     print(*sorted(set1 & set2, reverse=True))


# set1, set2 = {int(_) for _ in input().split()}, {int(_) for _ in input().split()}
#
# print('YES') if set1 == set2 else print('NO')


# m = int(input())
# n = int(input())
#
# set1, set2 = {input() for _ in range(m)}, {input() for _ in range(n)}
#
# print(len(set1 - set2))

# m = int(input())
# n = int(input())
#
# set1, set2 = {input() for _ in range(m)}, {input() for _ in range(n)}
#
# print(len(set1 ^ set2)) if len(set1 ^ set2) > 0 else print('NO')


# set1, set2 = set(input().split()), set(input().split())
# print(*sorted(set1 | set2))


# m = int(input())
# n = int(input())
#
# list1 = [input() for _ in range(m + n)]
#
# set1 = set(list1) - list1
#
# print(len(set1)) if len(set1) > 0 else print('NO')

# m = int(input())
# n = int(input())
# list1 = [input() for _ in range(m + n)]
# set1 = set(list1)
# if len(list1) == len(set1):
#     print(len(list1))
# elif len(set1) * 2 == len(list1):
#     print('NO')
# else:
#     print(len(list1) - ((len(list1) - len(set1)) * 2))

# lessons = int(input())
#
# #fst_les = int(input())
# pustoy_array = []
# for i in range(lessons):
#     #pustoy_array[i] = {input() for _ in range(int(input()))}
#     pustoy_array.append({input() for _ in range(int(input()))})
#     #pustoy_set.add({input() for _ in range(int(input()))})
#
# pustoy_set = pustoy_array[0]
# for i in range(lessons):
#     pustoy_set = pustoy_set & pustoy_array[i]
#
# print(*sorted(pustoy_set), sep='\n')






