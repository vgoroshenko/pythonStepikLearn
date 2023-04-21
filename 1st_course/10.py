#
# capitals = {'Франция': 'Париж', 'Россия': 'Москва', 'Чехия': 'Прага'}
# months = {1: 'Январь', 2: 'Февраль', 3: 'Март'}
#
# print('Минимальный ключ =', min(capitals))
# print('Максимальный ключ =', max(months))


#
# months1 = {1: 'Январь', 2: 'Февраль'}
# months2 = {1: 'Январь', 2: 'Февраль', 3: 'Март'}
# months3 = {3: 'Март', 1: 'Январь', 2: 'Февраль'}
#
# print('asd') if months1[1] in months2 else print('qq')


# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
#
# for key in capitals:
#     print(capitals[key])


# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
# sorted_user_lst = []
# for user in users:
#     if int(user['phone'][-1]) == 8:
#         sorted_user_lst.append(user['name'])
# print(*sorted(sorted_user_lst))

# asd = [user['name'] for user in users if user['phone'].endswith('8')]
# print(*sorted(asd))


# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
#
# sorted_user_lst = [user['name'] for user in users if len(user) < 3 or user['email'] == '' and len(user) == 3]
# print(*sorted(sorted_user_lst))


# numbers = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
#
# for n in input():
#     print(numbers[int(n)], end=' ')


# #cources = [(CS101 = '3004', 'Хайнс', '8:00')]
# cources_dict = {'CS101' : [3004, 'Хайнс', '8:00'],
#                 'CS102' : [4501, 'Альварадо', '9:00'],
#                 'CS103' : [6755, 'Рич', '10:00'],
#                 'NT110' : [1244, 'Берк', '11:00'],
#                 'CM241' : [1411, 'Ли', '13:00']}
# txt = input()
# #print(txt + ':', ', '.join(cources_dict[txt]))
# print('{}: {}, {}, {}'.format(txt, *cources_dict[txt]))

# buttons = {1: '.,?!:',
#            2: 'ABC',
#            3: 'DEF',
#            4: 'GHI',
#            5: 'JKL',
#            6: 'MNO',
#            7: 'PQRS',
#            8: 'TUV',
#            9: 'WXYZ',
#            0: ' '}
#
#
# txt = input().upper()
#
# for chr in txt:
#     for key, value in buttons.items():
#         if chr in value:
#             for c in value:
#                 if c == chr:
#                     print(key, end='')
#                     break
#                 else:
#                     print(key, end='')

# letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
# morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
# morse_dict = dict(zip(letters, morse))
# crypt_txt = input().upper()
# for c in crypt_txt:
#     if c in letters:
#         print(morse_dict[c], end=' ')
#
#
# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
#
# result = {}
# for num in numbers:
#     if num not in result:
#         result[num] = 1
#     else:
#         result[num] += 1
# print(result)



# result = {}
# result |= dict(zip([_ for _ in range(1, 16)], [_ ** 2 for _  in range(1, 16)]))
#
# print(result)

# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
# result = {}
# for i in dict1:
#     if i in dict2:
#         dict1[i] = dict1[i] + dict2[i]
# #result |= dict1
# result.update(dict2)
# result.update(dict1)
#
#
# print(result)


# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
#
# result = {}
#
# for c in text:
#     if c not in result:
#         result[c] = 1
#     else:
#         result[c] += 1
#
# print(result)

# s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
#
# s_list = s.split()
# words_count = {}
# for w in s_list:
#     if w not in words_count.items():
#         if s_list.count(w) in words_count:
#             words_count[s_list.count(w)] = min(words_count[s_list.count(w)], w)
#         else:
#             words_count[s_list.count(w)] = w
#     for _ in range(s_list.count(w)):
#         s_list.remove(w)
#
# print(words_count[max(words_count.keys())])
# #print([*sorted(words_count[max(words_count.keys())])][0])
#
# # for key in sorted(words_count, reverse=True):
# #     if isinstance(words_count[key], tuple):
# #         print(*sorted(words_count[key]), end=' ')
# #     else:
# #         print(words_count[key], end=' ')



# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]
#
# result = {}
#
# for card in pets:
#     if (card[1:]) not in result:
#             result[(card[1:])] = [card[0]]
#     else:
#             result[(card[1:])] = result[(card[1:])] + [card[0]]

#s = input()

# s_list = [w.strip('.,!?:;-') for w in input().lower().split()]
# words_count = {}
# for w in s_list:
#     if w not in words_count:
#         if s_list.count(w) in words_count:
#             words_count[s_list.count(w)] = min(words_count[s_list.count(w)], w)
#         else:
#             words_count[s_list.count(w)] = w
#
# print(words_count[min(words_count.keys())])


#s = input()

#s_list = [w.strip('.,!?:;-') for w in input().lower().split()]
# s_list = 'a b c a a d c'.split() #input().split()
# words_dict = {}
#
# for w in s_list:
#     for key in range(1, len(s_list) + 1):
#         if w not in words_dict:
#             words_dict[key] = w
#             print(w)
#         else:
#             words_dict[key] = w + s_list.count(w)
# print(words_dict.values())

# txt_dict = {}
# for _ in range(int(input())):
#     txt = input().split(':')
#     txt_dict[txt[0].lower()] = txt[1].strip()
# for i in range(int(input())):
#     txt_found = input().lower()
#     print(txt_dict[txt_found]) if txt_found in txt_dict else print('Не найдено')
# dsa =('asd', 'dsa')
# asd = {x: y for x, y in zip(*dsa)}
# print(asd)


#

#asd = {x: list(input()) for x in range(2)}
# asd = {x: set(input()) for x in range(2)}
# print(asd)
# print('YES') if sorted(asd[0]) == sorted(asd[1]) else print('NO')

#txt = list(input().lower())
# txt = [c for c in input().lower() if c not in '.,!?:;- ']
#
# print(txt)
#
# txt_dict = {x: sorted(txt[x]) for x in range(2)}
#
# print(txt_dict)

# txt_dict = {tuple(sorted(c for c in input().lower() if c not in '.,!?:;- ')): value for value in range(2)}
#
# print('YES') if len(txt_dict) == 1 else print('NO')



# txt_dict = dict(input().split() for _ in range(int(input())))
# #txt_dict.update(dict([value, key] for key, value in txt_dict.items()))
# txt_dict.update({value: key for key, value in txt_dict.items()})
# print(txt_dict[input()])
# print(txt_dict)



# 4
# Awful Terrible
# Beautiful Pretty
# Great Excellent
# Generous Bountiful


# city_dict = {tuple(value): key for key, value in [[i[0], i[1:]] for i in [input().split() for _ in range(int(input()))]]}
# for _ in range(int(input())):
#     txt = input()
#     for i in city_dict:
#         if txt in i:
#             print(city_dict[i])

# asd = dict(name = ['qwe'])
# print(asd)
# asd.update(name = [*asd['name'], 'wewe'])
#
# print(asd)

# abonent_lst = [input().lower().split() for _ in range(int(input()))]
#
# num_d = dict()
# for i in abonent_lst:
#     i.reverse()
#     if i[0] not in num_d:
#         num_d.setdefault(i[0], [i[1]])
#     else:
#         num_d[i[0]] = [*num_d[i[0]], i[1]]
# #print(num_d)
#
#
# for _ in range(int(input())):
#     search_name = input().lower()
#     print(num_d[search_name]) if search_name in num_d else print('абонент не найден')

# search_word = input()
#
# search_word_dict = {key: value for key, value in [[c, search_word.count(c)] for c in search_word]}
# code_dict = {int(value): key for key, value in [input().split(': ') for _ in range(int(input()))]}
#
# for c in search_word:
#     print(code_dict[search_word_dict[c]], end='')

# numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
#
# result = {key: numbers[key] ** 2 for key in range(len(numbers))}



# colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange', 'c8': None, 'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold', 'c13': None, 'c14': 'Amber', 'c15': 'Azure', 'c16': 'Beige', 'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl', 'c21': None, 'c22': 'Sand', 'c23': None}
#
# result = {key: value for key, value in colors.items() if len(value) == 2}


# favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62, 'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654, 'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271, 'anna': 55, 'madlen': 876}
#
# result = {key: value for key, value in favorite_numbers.items() if len(value) == 2}


# s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
#
# result = {int(key): value for key, value in [i.split(':') for i in s.split()]}


# numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
#
# result = {key: [i for i in range(1, key + 1) if key % i == 0] for key in numbers}



# words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
#
# result = {key: [ord(c) for c in key] for key in words}


# letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'}
#
# remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
#
# result = {key: value for key, value in letters.items() if key not in remove_keys}


# students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70), 'Madlen': (160, 50), 'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78), 'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80), 'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}
#
# result = {key: value for key, value in students.items() if value[0] > 167 and value[1] < 75}


# tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]
#
# result = {i[0]: i[1:] for i in tuples}


# student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
# student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
# student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]

#print({key: value for key, value in dict(zip(student_names, student_grades)).items()}.items())
#print([key for key in student_ids])
#asd = dict(zip(student_ids, student_names, student_grades))
#asd = [{x: {y: z}} for x, y, z in zip(student_ids, student_names, student_grades)]
#asd = dict(zip(student_names, student_grades))
#asd = dict(zip(student_ids, [{key: value} for key, value in dict(zip(student_names, student_grades)).items()]))
#asd = [{key: value} for key, value in dict(zip(student_ids, [{key: value} for key, value in dict(zip(student_names, student_grades)).items()])).items()]

#print(asd)
