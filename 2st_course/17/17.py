# my_txt = open('123.txt', 'w', encoding='utf-8')
# my_txt.write('asdqwdqq')
# my_txt.close()


# file = open('languages.txt', 'r', encoding='utf-8')
#
# line = file.readline()
# print(line)
# while line != '':              # пока не конец файла
#     print(line.strip())        # обрабатываем считанную строку
#     line = file.readline()     # читаем новую строку
#
# file.close()


# file = open('languages.txt', 'r+', encoding='utf-8')
#
# for line in file:
#     print(line.strip() + '1', end=' ')
#     file.writelines(line.strip() + '1')
# file.close()

# file_name = input()
#
# file = open(file_name, 'r', encoding='utf-8')
# txt = file.readline()[-1]
# print(file.read())
#
# file.close()

#
# file_name = input()
#
# file = open(file_name, 'r', encoding='utf-8')
# #txt = file.readlines()
# print(file.readlines()[-2])
#
# file.close()
# import random
#
# file = open('lines.txt', encoding='utf-8')
# file = file.readlines()
# print(''.join(random.choices(file)).rstrip())


# file = open('numbers.txt')
# numbers = file.readlines()
# print(sum(map(int, numbers)))


# file = open('nums.txt')
# numbers = file.readlines()
# #numbers = [i.strip().rstrip() for i in numbers if i != ' ']
# print(sum(map(int, filter(lambda x: x.strip().rstrip().isdigit(), numbers))))


# file = open('prices.txt', encoding='utf-8')
# file_list = [i.split('\t') for i in file.read().split('\n') if i != '']
# summ = sum(map(lambda x: int(x[1]) * int(x[2]), file_list))
# print(summ)
# file.close()


# with open('input.txt', encoding='utf-8') as file:
#     print('Repeat after me:', file.readline().strip())
#     for line in file:
#         print(line + '!')

# with open('text.txt', encoding='utf-8') as file:
#     for line in file:
#         print(line[::-1])

# with open('lines.txt', encoding='utf-8') as file:
#     file_list = file.readlines()
#     newlist = filter(lambda x: len(x) == len(max(file_list, key=len)) and x.strip(), file_list)
#     print(*newlist, sep='')
#     # for line in newlist:
#     #     print(line.strip())

# with open('numbers.txt', encoding='utf-8') as file:
#     for line in file:
#         print(sum(map(int, line.strip().split())))

# with open('nums.txt', encoding='utf-8') as file:
#     total = 0
#     for line in file:
#         total_string = ''
#         for c in line:
#             if c.isalpha():
#                 c = ' '
#             total_string += c
#         total += sum(map(int, total_string.strip().split()))
#
# print(total)

#import string
# my_punc = r',. '
# file_dict = dict()
# with open('file.txt', encoding='utf-8') as file:
#     file_dict['lines'] = len(file.readlines())
#     file_dict['words'] = 0
#     file_dict['letters'] = 0
#     file.seek(0)
#     for line in file:
#         file_dict['words'] = file_dict['words'] + len(line.split())
#         #file_dict['letters'] = file_dict['letters'] + sum(map(len, line.strip().translate(str.maketrans('', '', my_punc))))
#         file_dict['letters'] = file_dict['letters'] + sum(map(len, filter(lambda x: x.isalpha(),line.strip().translate(str.maketrans('', '', my_punc)))))
#
# print(f'''Input file contains:
# {file_dict['letters']} letters
# {file_dict['words']} words
# {file_dict['lines']} lines
# ''')
#print(f'Input file contains: \n{file_dict["letters"]} letters \n{file_dict["words"]} words \n{file_dict["lines"]} lines')


# with open('first_names.txt') as fn_file:
#     with open('last_names.txt') as ln_file:
#         for i in range(3):
#             fn_file.seek(0)
#             ln_file.seek(0)
#             print(random.choice(fn_file.readlines()).strip(), random.choice(ln_file.readlines()).strip())

# with open('population.txt') as file:
#     for line in file:
#         country = line.strip().split('\t')
#         if line[0] == 'G' and int(country[1]) > 500000:
#             print(country[0])


# def read_csv():
#     with open('data.csv') as file:
#         keys = file.readlines()[0].strip().split(',')
#         file.seek(0)
#         total_list = []
#         for line in file:
#             if keys[0] not in line:
#                 total_list.append(dict(zip(keys, line.strip().split(','))))
#         return total_list
#
# print(read_csv())

# strings = int(input())
# word_search = 'anton'
# # for i in range(strings):
# #     asd = [i for i in list(input()) if i in word_search]
# #     if ''.join(asd) == word_search:
# #         print(i + 1, end=' ')
#
# for i in range(strings):
#     word = input()
#     txt = ''
#     for c in word:
#         if c in word_search and c not in txt:
#             txt += c
#     print(txt)
#     if txt == word_search:
#         print(i + 1, end=' ')


# with open('words.txt', 'w') as output:
#     print('stepik', 'beegeek', 'iq-option', sep='*', end='+\n', file=output)
#     print('python', file=output)


# with open('output.txt', 'w', encoding='utf-8') as output:
#     #print(input(), file=output)
#     output.write(input())
# import random
# with open('random.txt', 'w') as output:
#     for _ in range(25):
#         output.write(f'{random.randrange(111, 777)}\n')


# with open('input.txt', 'r') as input, open('output.txt', 'w') as output:
#     line_count = 0
#     for line in input:
#         line_count += 1
#         output.write(f'{line_count}) {line}')


# with open('class_scores.txt', 'r', encoding='utf-8') as input_file, open('new_scores.txt', 'w', encoding='utf-8') as output_file:
#     for line in input_file:
#         line = line.strip().split()
#         score = int(line[1])
#         print(line[0], f'{score + 5 if score < 96 else (100 - score) + score}', file=output_file)

# def percentage(part, whole):
#   percentage = 100 * float(part)/float(whole)
#   return percentage
#
# print(percentage(3, 5))

# with open('goats.txt', 'r') as goats_file, open('answer.txt', 'w') as output:
#     goats_color_dict = dict([[i[0], 0] for i in [line.strip().split() for line in goats_file] if 'COLOURS' not in i and 'GOATS' not in i])
#     goats_file.seek(0)
#     color_list = [line.strip().split()[0] for line in goats_file][len(goats_color_dict)+2:]
#     for i in color_list:
#         goats_color_dict[i] += 1
#     tmp = sorted([key for key, value in goats_color_dict.items() if float(value) > 7 * len(color_list) / 100])
#     for i in tmp:
#         print(i, 'goat')
#
# print(color_list)
# print(goats_color_dict)

# for i in range(int(input())):
#     with open(input(), 'r', encoding='utf-8') as read_file, open('output.txt', 'a', encoding='utf-8') as output_file:
#         for line in read_file:
#             output_file.write(line)


# with open('logfile.txt', 'r', encoding='utf-8') as log_file, open('output.txt', 'w', encoding='utf-8') as output:
#     for line in log_file:
#         h1 = int(line.strip().split(', ')[1].split(':')[0])
#         h2 = int(line.strip().split(', ')[2].split(':')[0])
#         m1 = int(line.strip().split(', ')[1].split(':')[1])
#         m2 = int(line.strip().split(', ')[2].split(':')[1])
#         if (h2 * 60 + m2) - (h1 * 60 + m1) > 59:
#             print(line.strip().split(', ')[0], file=output)



# with open(input(), 'r', encoding='utf-8') as file:
#     print(len(file.readlines()))

# with open('ledger.txt', 'r', encoding='utf-8') as file:
#     print('$', sum(map(lambda x: int(x.strip().lstrip('$')), file)), sep='')


# with open('grades.txt', 'r', encoding='utf-8') as file:
#     total = 0
#     for line in file:
#         total += 1 if all(int(x) >= 65 for x in line.split()[1:]) else 0
# print(total)


# with open('words.txt', 'r', encoding='utf-8') as file:
#     file = file.read().split()
#     print(*filter(lambda x: len(x) == max(map(len, file)), file), sep='\n')


# with open(input(), 'r', encoding='utf-8') as file:
#     myfile = file.readlines()
#     if len(myfile) > 10:
#         print(*myfile[len(myfile)-10:], sep='')
#     else:
#         print(*myfile, sep='')

# import re
# with open('stepik.txt', 'r', encoding='utf-8') as file, open('forbidden_words.txt', 'r') as f_words_file:
#     f_words = f_words_file.read().split()
#     file1 = file.read().lower().split(' ')
#     file.seek(0)cu
#     file2 = file.read().split(' ')
#     for i in range(len(file1)):
#         for word in f_words:
#             if word in file1[i]:
#                 file2[i] = file1[i].replace(word, len(word) * '*')
#                 file1[i] = file1[i].replace(word, len(word) * '*')
#                 #print(file1[i])
#                 continue
#
# print(*file2)
#
#
# #     f_words = f_words_file.read().split()
# #     file = file.read()
# #     for word in f_words:
# #         #if word in file:
# #             file = re.sub(word, len(word) * '*', file, flags=re.I)
# #
# # print(file)
#
# *********** ******************* ******** ************ ************. ***********     confusio  ********* and *******************.
# ********* and math ******* ***********...... ****** ****** PyToN




# mydict = dict()
# qwe = dict([[i for i in input().strip().split('\t')] for i in range(33)])
# print(qwe)
# for key, value in mydict.items():
#     print(key)


#mydict = dict([[i for i in input().strip().split('\t')] for i in range(33)])

#ТРАНСЛИТ

# with open('cyrillic.txt', 'r', encoding='utf-8') as text, open('transliteration.txt', 'w', encoding='utf-8') as output:
#     my_char_dict = {'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch', 'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*', 'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je', 'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya'}
#     newtxt = ''
#     for line in text:
#         for c in line:
#             if c.lower() in my_char_dict:
#                 if c.isupper():
#                     newtxt += my_char_dict[c.lower()].upper() if len(my_char_dict[c.lower()]) == 1 else my_char_dict[c.lower()].upper()[0] + my_char_dict[c.lower()][1:]
#                 else:
#                     newtxt += my_char_dict[c]
#             else:
#                 newtxt += c
#     print(newtxt, file=output)

#безкомментариев

# with open(input(), 'r', encoding='utf-8') as file:
#     prev_line = ''
#     count = 0
#     for line in file:
#         if 'def ' in line and '# ' not in prev_line:
#             print(line[4:line.find('(')])
#             count += 1
#         prev_line = line.strip()
#     if count == 0:
#         print('Best Programming Team')



# year = int(input())
# print(year % 4 == 0)



with open('input.txt', 'r', encoding='utf-8') as file:
    print(file.read())
    print()
    print(file.tell())






