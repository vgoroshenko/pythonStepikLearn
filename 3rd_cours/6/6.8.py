# from collections import Counter
#
# print(Counter(input().lower().split()).most_common()[0][0])
import json
# from collections import Counter
#
# txt = Counter(input().lower().split()).most_common()
# print(*sorted([i[0] for i in txt if i[1] == txt[0][1]]), sep=', ')


# from collections import Counter
#
# txt = Counter(input().lower().split()).most_common()
# print(max([i[0] for i in txt if i[1] == txt[0][1]]), sep=', ')

# from collections import Counter
#
# tmp = {}
# [tmp.setdefault(len(i), []).append(i) for i in input().split()]
# tmp = sorted(tmp.items(), key=lambda x: len(x[1]))
# [print(f'Слов длины {i[0]}: {len(i[1])}') for i in tmp]
#print(tmp)

# import sys
# from collections import Counter
#
# print(sorted(Counter({i.split()[0]: int(i.split()[1]) for i in sys.stdin}).most_common(), key=lambda x: x[1])[1][0])


# from collections import Counter
#
# data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')
#
# data.min_values = lambda: [*filter(lambda x: x[1] == min(data.values()), data.items())]
# data.max_values = lambda: [*filter(lambda x: x[1] == max(data.values()), data.items())]
#
# print(data.max_values())
# print(data.min_values())

# from collections import Counter
# import csv
#
# with open('name_log.csv', 'r', encoding='utf-8') as f:
#     file = list(csv.reader(f))[1:]
#     [print(f'{key}: {value}') for key, value in Counter(sorted(list(map(lambda x: x[1], file)))).items()]


# from collections import Counter
# def scrabble(symbols, word):
#     symbols_word = Counter(symbols.lower())
#     return  symbols_word >= Counter(word.lower())

# from collections import Counter
#
# def print_bar_chart(data, mark):
#     tmp = Counter(data)
#     [print(f'{key}{(max(map(lambda x: len(x), tmp)) - len(key)) * " "} |{value * mark}') for key, value in sorted(tmp.items(), key=lambda x: -x[1])]
#
# print_bar_chart('beegeek', '+')
#
# languages = ['java', 'java', 'python', 'C++', 'assembler', 'java', 'C++', 'C', 'pascal', 'C++', 'pascal', 'java']
#
# print_bar_chart(languages, '#')

# from collections import Counter
# import csv
# import json
#
# asd = {}
#
# for i in range(4):
#     with open(f'quarter{i + 1}.csv', 'r', encoding='utf-8') as f:
#         file = csv.DictReader(f)
#         for row in file:
#             asd.update(row)
#             if i == 3:
#                 print(Counter(asd).total())
#                 print(asd)
#         print(asd)
#     print(file)
#print(asd)


# from collections import Counter, defaultdict
#
# books_count = Counter(defaultdict(int))
# for i in input().split():
#     books_count[i] += 1
#
# summ = 0
# for j in range(int(input())):
#     book = input().split()
#     if books_count[book[0]] != 0:
#         books_count.subtract(Counter({book[0] : 1}))
#         summ += int(book[1])
#
# print(summ)











