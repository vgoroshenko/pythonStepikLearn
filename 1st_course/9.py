# s = 'abcdef'
# for c in s:
#     print(c)

# s = '01234567891011121314151617'
# for i in range(0, len(s), 5):
#     print(s[i], end='')

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
#
# print(s[7])

# text = input()
#
# for i in range(0, len(text), 2):
#     print(text[i], end='\n')


# text = input()
#
# for i in range(len(text), 0, -1):
#     print(text[i - 1], end='\n')


# text = 1
#
# while text > 0:
#     text = input()
#     print(text[0])
#     text = len(text)

# a, b, c = input(), input(), input()
#
# print(b[0], a[0], c[0], sep='')

# num = input()
# total = 0
# for c in num:
#     total += int(c)
# print(total)

# n = input()
# flag = True
# for i in range(len(n)):
#     if n[i] in '0123456789':
#         flag = True
#         break
#     else:
#         flag = False
# if flag == True:
#     print('Цифра')
# else:
#     print('Цифр нет')

# text = input()
# total_plus = 0
# total_mnoj = 0
# for i in range(len(text)):
#     if text[i] in '+':
#         total_plus += 1
#     if text[i] in '*':
#         total_mnoj += 1
# print('Символ + встречается', total_plus, 'раз')
# print('Символ * встречается', total_mnoj, 'раз')


# text = input()
# char = ''
# total = 0
# for c in range(len(text)):
#     if text[c] in char:
#         total += 1
#     char = text[c]
# print(total)

# text = input()
# total_glasn = 0
# total_soglasn = 0
# glasn = 'ауоыиэяюёе'
# soglasn = 'бвгджзйклмнпрстфхцчшщ'
# for c in range(len(text)):
#     if text[c] in glasn or text[c] in glasn.upper():
#         total_glasn += 1
#     if text[c] in soglasn or text[c] in soglasn.upper():
#         total_soglasn += 1
# print('Количество гласных букв равно', total_glasn)
# print('Количество согласных букв равно', total_soglasn)


#Перевод из десятичной в двоичную систему
# num = int(input())
# total = ''
# while num > 0:
#     b = num % 2
#     total += str(b)
#     num = num // 2
# for c in range(len(total), 0, -1):
#     print(total[c - 1], end='')

# text = input()
#
# if text == text[::-1]:
#     print('YES')
# else:
#     print('NO')

# text = input()
#
# print(len(text))
# print(text * 3)
# print(text[0])
# print(text[:3])
# print(text[-3:])
# print(text[::-1])
# print(text[1:-1])

# text = input()
#
# print(text[2:3])
# print(text[-2:-1])
# print(text[:5])
# print(text[:-2])
# print(text[::2])
# print(text[1::2])
# print(text[::-1])
# print(text[::-2])

# import math
# text = input()
#
# text_first = text[:math.ceil(len(text) / 2)]
# text = text[math.ceil(len(text) / 2):] + text_first
# print(text)

# text = input()
#
# text_check = text.title()
#
# if text == text_check:
#     print('YES')
# else:
#     print('NO')

# text = input()
#
# print(text.swapcase())



# text = input()
# check = 'хорош'
# if check in text.lower():
#     print('YES')
# else:
#     print('NO')


# text = input()
# total = 0
# for c in range(len(text)):
#     if 'a' <= text[c] <= 'z':
#         total += 1
# print(total)

# text = input()
# print(text.count(' ') + 1)


# text = input()
# text = text.lower()
#
# print('Аденин:', text.count('а'))
# print('Гуанин:', text.count('г'))
# print('Цитозин:', text.count('ц'))
# print('Тимин:', text.count('т'))



# text = input()
# text = text.lower()
# adenadin = 0
# for c in range(len(text)):
#     if 'a' in text[c]:
#         adenadin += 1
#     if 'a' in text[c]:
#         adenadin += 1

# num = int(input())
# total = 0
# for i in range(num):
#     text = input()
#     if text.count('11') >= 3:
#         total += 1
# print(total)


# text = input()
# total = 0
# for c in range(len(text)):
#     if text[c] in '0123456789':
#         total += 1
# print(total)

# text = input()
# if text.endswith('.com') or text.endswith('.ru'):
#     print('YES')
# else:
#     print('NO')

# text = input()
#
# old_char_count = 0
# old_char = ''
# for c in range(len(text)):
#     char_count = text.count(text[c])
#     char = text[c]
#     if char_count > old_char_count:
#         old_char_count = char_count
#         old_char = char
# print(old_char)


# text = input()
# char_count = text.count('f')
# start_char = text.find('f')
# if char_count > 1:
#     end_char = text.rfind('f')
#     print(start_char, end_char)
# elif char_count == 1:
#     print(start_char)
# else:
#     print('NO')


# text = input()
# all_char = len(text)
# first_char_index = text.find('h')
# last_char_index = text.rfind('h')
#
# for i in range(first_char_index):
#     print(text[i], end='')
# for i in range(last_char_index + 1, all_char):
#     print(text[i], end='')

# s = 'In {0}, someone paid {1} {2} for two pizzas.'
#
# print(s.format('2010', '10k', 'Bitcoin'))

# year = 2010
# amount = '10K'
# currency = 'Bitcoin'
#
# print(f'In {year}, someone paid {amount} {currency} for two pizzas.')


# start, end = int(input()), int(input())
#
# for i in range(start, end + 1):
#     print(chr(i), end=' ')

# text = input()
#
# for i in range(len(text)):
#     print(ord(text[i]), end=' ')


# расшифровка код цезаря
# move_on = int(input())
# text = input()
# for i in range(len(text)):
#     num_char = ord(text[i])
#     if num_char - move_on < 97:
#         char = num_char - move_on
#         total_char = 97 - (char + 1)
#         total = ord(chr(122)) - total_char
#         print(chr(total), end='')
#     else:
#         print(chr(ord(text[i]) - move_on), end='')


