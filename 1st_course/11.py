# text = 'Python rocks!'
# text1 = ''
# for c in range(0, len(text), 3):
#     text1 += text[c - 2]
#     text = text.replace(text[c], ' ')
# print(text.strip())
# print(text1)


# s = 'qwertyuiop'
#
# for c in range(0, len(s)):
#     if c % 3 == 0:
#         continue
#     print(s[c], end='')


# num = input()
#
# if '1' in num:
#     print(num.replace('1', 'one', num.count('1')))



# num = input()
#
# print(num.replace('@', '', num.count('@')))


# text = input()
#
# char_count = text.count('f')
#
# if char_count > 1:
#     char_start = text.find('f')
#     print(text.find('f', char_start + 1))
# elif char_count == 1:
#     print('-1')
# elif char_count == 0:
#     print('-2')


# start, end = int(input()), int(input())
#
# for i in range(start, end + 1):
#     print(chr(i), end=' ')
#
# text = input()
#
# for i in range(len(text)):
#     print(ord(text[i]), end=' ')




# text = input()
#
# start = text.find('h')
# end = text.rfind('h')
#
# seredina = text[end - 1:start:-1]
#
# print(text[:start + 1] + seredina + text[end:])


# for i in range(start + 1, end):
#     for s in range(len(seredina)):
#         total = total.replace(text[i], seredina[s])
#         break
# print(seredina)
# print(total)





# text = input()
# all_char = len(text)
# first_char_index = text.find('h')
# last_char_index = text.rfind('h')
#
# for i in range(first_char_index):
#     print(text[i], end='')
# for i in range(last_char_index + 1, all_char):
#     print(text[i], end='')


# num = int(input())
# print(list(range(1, num + 1)))

# num = int(input())
# total = ''
# for i in range(97, 97 + num):
#     total += chr(i)
# total = list(total)
# print(total)

# text = ['asd', 'dsa', 'dsa', 'asdd', 'asd']
# if 'asd' in text:
#     print('yes')


# evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# average = sum(evens) / len(evens)
#
# print(average)

# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# rainbow[3] = 'Зеленый'
# rainbow[-1] = 'Фиолетовый'
#
# print(rainbow)

# languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
# print(languages[::-1])

# numbers1 = [1, 2, 3]
# numbers2 = [6]
# numbers3 = [7, 8, 9, 10, 11, 12, 13]
#
# numbers1 += numbers1
# numbers2 *= 9
#
# print(numbers1 + numbers2 + numbers3)


# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
#
# print(len(numbers))
# print(numbers[-1])
# print(numbers[::-1])
# if 5 and 17 in numbers:
#     print('YES')
# else:
#     print('NO')
# numbers = numbers[1:len(numbers) - 1]
# print(numbers)


# num = int(input())
# total = []
# for i in range(num):
#     text = input()
#     total.append(text)
# print(total)


# total = []
# for i in range(97, 97 + 26):
#     total.append(chr(i) * (i - 97 + 1))
# print(total)

# num = int(input())
# total = []
# for i in range(num):
#     total.append(int(input()) ** 3)
# print(total)

# num = int(input())
# total = []
# for i in range(1, num + 1):
#     if num % i == 0:
#         total.append(i)
# print(total)

# num = int(input())
# total = []
# summa = 0
# last_digit = 0
# for i in range(num):
#     digit = int(input())
#     summa = digit + last_digit
#     last_digit = digit
#     if summa > digit or digit < 0 and summa < digit:
#         total.append(summa)
# print(total)



# num = int(input())
# total = []
# for i in range(num):
#     digital = int(input())
#     total.append(digital)
# del total[1::2]
# print(total)

# num = int(input())
# total_list = []
# for i in range(num):
#     text = input()
#     total_list.extend(text)
# print(total_list)

# num = int(input())
# start_list = []
# for i in range(num):
#     text = input()
#     start_list.append(text)
# digit_num = int(input())
# for i in range(num):
#     if len(start_list[i]) < digit_num:
#         continue
#     print(start_list[i][digit_num - 1], end='')


# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for i in range(len(numbers)):
#     print(numbers[i])

# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# total = 0
# for num in numbers:
#     total += num ** 2
# print(total)

# num = int(input())
# digit = []
# for i in range(num):
#     digit.append(int(input()))
# print(*digit, sep='\n')
# print()
# f = []
# for i in range(num):
#     f.append((digit[i] ** 2 + 2 * digit[i]) + 1)
# print(*f, sep='\n')


# num = int(input())
# digits_list = []
# digit = 0
# for i in range(num):
#     old_digit = digit
#     digit = int(input())
#     digits_list.append(digit)
# del  digits_list[digits_list.index(min(digits_list))]
# del  digits_list[digits_list.index(max(digits_list))]
# print(*digits_list, sep='\n')


# num = int(input())
# word_list = []
# for i in range(num):
#     word = input()
#     if word not in word_list:
#         word_list.append(word)
# print(*word_list, sep='\n')

# num = int(input())
# word_list = []
# for i in range(num):
#     word = input()
#     word_list.append(word)
# search_word = input()
# for word_index in word_list:
#     if search_word.lower() in word_index.lower():
#         print(word_index, sep='\n')



# num = int(input())
#
# minus_digit_list = []
# zero_digit_list = []
# plus_digit_list = []
#
# for i in range(num):
#     digit = int(input())
#     if digit < 0:
#         minus_digit_list.append(digit)
#     elif digit == 0:
#         zero_digit_list.append(digit)
#     elif digit > 0:
#         plus_digit_list.append(digit)
# print(*minus_digit_list, *zero_digit_list, *plus_digit_list, sep='\n')


#Поиск по словам в строках *******************

# num = int(input())
#
# string_list = []
# search_word_list = []
# find_word_list = []
# for i in range(num):
#     word = input()
#     string_list.append(word)
#
# search_word_count = int(input())
#
# for i in range(search_word_count):
#     search_word = input()
#     search_word_list.append(search_word)
#
#
# for string in string_list:


#     word_count = 0
#     for word in search_word_list:
#         if word.lower() in string.lower():
#             word_count += 1
#             if word_count == len(search_word_list):
#                 find_word_list.append(string)
#
# print(*find_word_list, sep='\n')

# words = 'Python is the most powerful language'.split()
# words_list = 'Python is the most powerful language'
# digit = ['1', '2', '3', '4', '5']
# s = 'total'.join(words)
# print(digit)
# print('.'.join(digit))
# print(words)
# print(list(words_list))


# s = 'BEEGEEK'
# chars = list(s)
# s = '**'.join(chars)
# print(s)


# print(*input().split(), sep='\n')

# string = input()
# for i in range(len(string)):
#     if string[i].isupper():
#         print(''.join(string[i]), end='.')


# string = input().split('\\')
# print('\n'.join(string))

# string = input().split()
# for i in range(len(string)):
#     string[i] = int(string[i]) * '+'
#
# print('\n'.join(string))

# string = input().split('.')
# flag = True
# for i in range(len(string)):
#     if int(string[i]) > 255:
#         flag = False
# if flag == True:
#     print('ДА')
# else:
#     print('НЕТ')

# string = list(input())
# digital = input()
# print(digital.join(string))


# string = input().split()
# pair_count = 0
# for i in range(len(string)):
#     for j in range(i + 1, len(string)):
#         asd = int(string[i])
#         asd1 = int(string[j])
#         if asd == asd1:
#             pair_count += 1
# print(pair_count)

# names = ['Gvido', 'Roman' , 'Timur']
# names_copy1 = list(names)             # создаем поверхностную копию с помощью функции list()
# names_copy2 = names[:]
#
# print(names_copy1)


# numbers = [8, 9, 10, 11]
# numbers.remove(numbers[1])
# numbers.insert(1, 17)
# numbers.extend([4, 5, 6])
# numbers.remove(numbers[0])
# numbers = numbers * 2
# numbers.insert(3, 25)
# print(numbers)

# text = input().split()
# if len(text) > 1:
#     for i in range(len(text)):
#         text[i] = int(text[i])
#     min_text = min(*text)
#     max_text = max(*text)
#     min_index = text.index(min_text)
#     max_index = text.index(max_text)#
#     text[min_index] = max_text
#     text[max_index] = min_text
#
#     # text.pop(min_index)
#     # text.insert(min_index, max_text)
#     # text.pop(max_index)
#     # text.insert(max_index, min_text)
# print(*text)


# text = input().lower().split()
#
# need_found_text = ['a', 'an', 'the']
# total = 0
# for i in need_found_text:
#     total += text.count(i)
# print('Общее количество артиклей:', total)

# text = '1'
# while len(text) > 0:
#     text = input().split()
#     if text.count('#') > 0:
#         text = text[:text.index('#')]
#         print(*text)
#     else:
#         print(*text)

# string_number = input().split('#')
# string_number.remove('')
#
# for i in range(int(*string_number)):
#     text = input()
#     if '#' in text:
#         text = text.split('#')
#         text = text[0]
#         print(text.rstrip())
#     else:
#         print(text.rstrip())

# text = 'print("Здравствуйте, рыцарь", name) #долой Макнамару'.split()
# #text = text[:' '.join(text).find('#')]
# index = ' '.join(text).find('#')
# text = ' '.join(text)[:' '.join(text).find('#')]
# print(text.rstrip())


# text = input().split()
# text = [int(x) for x in text]
# text.sort()
# print(*text)
# text.sort(reverse = True)
# print(*text)

# numbers = [i for i in range(10)]
# #print(int(*numbers))
# print(1)

# chars = [c for c in 'abcdefg']
# print(chars)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# new_keywords = [c[1:] for c in  keywords]
# lengths = [len(s) for s in keywords]
#
# print(new_keywords)

# palindromes = [i for i in range(100, 1000) if str(i) == str(i)[::-1]]
#
# print(palindromes)

# print(*[i ** 2 for i in range(1, int(input()) + 1)], sep='\n')

# print(*[int(i) for i in input().split()])

# print(*[i for i in input().split()], sep='\n')

# print(''.join([i for i in list(input()) if i.isdigit() == True]))

# print(*[int(i) ** 2 for i in input().split() if int(i) % 2 == 0 and str(int(i) ** 2)[-1:] != '4'])

# a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17, 36, 88, -61, -97, -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25, 79, 97, 0, -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26, 63, -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84]
#
# n = len(a)
# flag = True
# i = 0
# while flag:
#     flag = False
# #for i in range(n - 1):
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#             flag = True
# print(a)

# a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]
#
# n = len(a)
#
# b = []
# # for i in range(n):
# #     min_digit = min(a[i:])
# #     min_index = a[i:].index(min(a[i:]))
# #     a.pop(min_index)
# #     a.insert(i, min_digit)
# # print(a)
#
#
# while n > 0:
#     b.append(min(a))
#     a.remove(min(a))
#     n -= 1
# print(b)



