# def my_func():
#     return 17
#
# asd = input
#
# input = my_func
# num = input
# print(num())
# # input = input
#
# input = asd
#
# print(input('asd'))


# def numbers_sum(numbers):
#     '''Принимает список и возвращает сумму его чисел (int, float),
# игнорируя нечисловые объекты. 0 - если в списке чисел нет.'''
#     return sum([i for i in numbers if isinstance(i, (int, float))])
#
#
# print(numbers_sum([1, '2', 3, 4, 'five']))
# print(numbers_sum(['beegeek', 'stepik', '100']))





# def up(q):
#     return q.upper() if isinstance(q, str) else q
#
# old_print = print
# def nop(*rest, sep=None, end=None):
#     return old_print(*map(up, rest),
#                      sep=up(sep),
#                      end=up(end))
#
# print = nop

#words = ('black', 'white', 'grey', 'black-1', 'white-1', 'python')
#print(*words, sep=' to ', end=' LOVE')
#print('bee', 'geek', sep=' and ', end=' wow')
# print('beegeek', [1, 2, 3], 4)


# def polynom(x):
#     tmp = x**2 + 1
#     polynom.values.add(tmp)
#     return tmp
# polynom.values = set()
#
# for _ in range(10):
#     polynom(10)
#
# print(polynom.values)


def remove_marks(text, marks):
    remove_marks.count += 1
    for i in marks:
        text = text.replace(i, '', text.count(i))
    return text

remove_marks.count = 0

text = 'Hi! Will we go toge!ther?'

print(remove_marks(text, '!?'))
print(remove_marks.count)











