#import sys
#from datetime import datetime

# data = [print(i) for i in [line.strip()[::-1] for line in sys.stdin]]


# dates = [datetime.strptime(line.strip(), '%Y-%m-%d') for line in sys.stdin]
# print((max(dates) - min(dates)).days)

# import sys
# data = [int(line.strip()) for line in sys.stdin]
# if data[-1] % 2 == 0:
#     if len(data) % 2 == 0:
#         print('Дима')
#     else:
#         print('Анри')
# else:
#     if (len(data) - 1) % 2 == 0:
#         print('Дима')
#     else:
#         print('Анри')

# import sys, numpy
#
# data = [int(line.strip()) for line in sys.stdin]
# if data:
#     print(f'Рост самого низкого ученика: {min(data)}')
#     print(f'Рост самого высокого ученика: {max(data)}')
#     print(f'Средний рост: {int(numpy.average(data))}')
# else:
#     print('нет учеников')


# import sys
# print(len([line for line in [line.strip() for line in sys.stdin] if line[0] == '#']))


# import sys
#
# print(*[line.rstrip() for line in sys.stdin if line.strip('   ')[0] != '#'], sep='\n')

# import sys
#
# tmp = [line.strip().split('/') for line in sys.stdin]
# category = tmp.pop(-1)[0]
# [print(i[0].strip()) for i in sorted(tmp, key=lambda x: (x[2], x[0][0])) if category in i[1]]

# import sys
# from datetime import datetime
#
# tmp = [datetime.strptime(line.strip(), '%d.%m.%Y') for line in sys.stdin]
# if sorted(tmp) == tmp and len(tmp) == len(set(tmp)):
#     print('ASC')
# elif sorted(tmp, reverse=True) == tmp and len(tmp) == len(set(tmp)):
#     print('DESC')
# else:
#     print('MIX')


# import sys
#
# def is_arithmetic_sequence(numbers):
#     differences = [numbers[i+1] - numbers[i] for i in range(len(numbers)-1)]
#     return all(x == differences[0] for x in differences)
#
# def is_geometrical_sequence(numbers):
#     for i in range(len(numbers) - 1):
#         num = numbers[i]
#         if num + num != numbers[i + 1]:
#             return False
#     return True
#
# tmp = [int(line.strip()) for line in sys.stdin]
#
#
# if is_arithmetic_sequence(tmp):
#     print('Арифметическая прогрессия')
# elif is_geometrical_sequence(tmp):
#     print('Геометрическая прогрессия')
# else:
#     print('Не прогрессия')






