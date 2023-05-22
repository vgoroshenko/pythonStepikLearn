# positive = [1, 2, 3, 4, 5]
# negative = [-1, -2, -3]
# combined = [1, 2, -3, 4]
#
# result = map(lambda a, b, c: a + b + c, positive, negative, combined)
#
# print(*result)
#
# print(positive + negative + combined)


# data = ['Timur', -16.648911695768902, 'six', -202, 883.0093275936454, -765, (3, 4), -105.10718000213546, 976, -308.96857946288094, 458, ['one', 'two'], 479.92207220345927, -87, -71, 'twelve', 112, -621, -715.0179551194733, 'seven', 229, 729, -358, [1, 2, 3], -974, 882, -894.4709033242768, '', 323.7720806756133, 'beegeek', -224, 431, 170.6353248658936, -343.0016746052049, 'number', 104.17133679352878, [], -353.5964777099863, 'zero', -113, 288, None, -708.3036176571618]
#
# print(*list(map(lambda x: int(x), filter(lambda x: isinstance(x, (int, float)), data))), sep='\n')


# numbers = [4754, -4895, -364, -4764, 4683, 1639, -43, 228, -2701, -1503, 1223, 4340, -1296, 3939, -345, 623, -3275, 1003, 4367, -1739, 550, -1217, -1334, 1526, -4359, -3028, -4663, 3356, 3887, 4297, -1982, 1013, 3299, 3556, -3324, 417, 3531, -3134, 1782, 4439, 1652, -985, 4327, 1517, 1225, -915, 2808, -3851, -1005, 3396, 2842, -3879, -3824, -3805, 1609, -4741, -3072, 3573, 4680, 588, -1430, 2378, -1095, -343, 4357, -2164, -3304, 4354, 4926, -352, -1187, -3313, 2741, 4786, -2689, 741, 4558, 1442, 62, -1099, -2201, -16, -3115, 1862, 2384, 4072, -90, 204, 1158, -3134, -2512, 756, 4148, 4370, 1756, 3609, -1148, -3909, 4123, -2906, 69, 96, 1111]
#
# print(sum(list(map(lambda x: x**2, filter(lambda x: len(str(abs(x))) == 2 and x % 9 == 0, numbers)))))


# names = ['ульяна', 'арина', 'Дмитрий', 'Сергей', 'Яна', 'мила', 'Ольга', 'софья', 'семён', 'Никита', 'маргарита', 'Василиса', 'Кирилл', 'александр', 'александра', 'Иван', 'андрей', 'Родион', 'максим', 'алиса', 'Артём', 'софия', 'владимир', 'дамир', 'Валерий', 'степан', 'Алексей', 'Марк', 'олег', 'ирина', 'Милана', 'мия', 'денис', 'Фёдор', 'Елизавета', 'айлин', 'Варвара', 'валерия', 'Алёна', 'Николь', 'юлия', 'Ксения', 'пётр', 'георгий', 'Мария', 'глеб', 'илья', 'Захар', 'Дарья', 'Евгения', 'матвей', 'Серафим', 'екатерина', 'Тимофей', 'виктор', 'Егор', 'Ника', 'анна', 'даниил', 'тихон', 'вера', 'кира', 'Эмилия', 'Виктория', 'Игорь', 'полина', 'алина', 'Давид', 'анастасия', 'Вероника', 'ярослав', 'Руслан', 'татьяна', 'Демид', 'амелия', 'Элина', 'Арсен', 'евгений', 'мадина', 'дарина', 'Савелий', 'Платон', 'Аделина', 'диана', 'Айша', 'павел', 'Стефания', 'Тимур', 'Ева', 'Елисей', 'Артемий', 'григорий', 'Мирон', 'Мирослава', 'Мира', 'Марат', 'Лилия', 'роман', 'владислав', 'Леонид']
#
# print(*sorted(list(map(lambda x: x.title(), filter(lambda x: len(x) > 4 and x.lower()[0] in ('а', 'м'), names)))))


# def fib(n):
#     return (lambda x: 1 if x <= 2 else fib(x - 1) + fib(x - 2))(n)
#
# print(fib(2))


# def print_operation_table(operation, rows, cols):
#     mat = [[operation(j,i) for i in range(1, cols + 1)] for j in range(1, rows + 1)]
#     for i in mat:
#         for j in i:
#             print(str(j).ljust(3), end=' ')
#         print()
#
# print_operation_table(lambda a, b: a * b, 5, 5)
# print_operation_table(pow, 5, 4)
# print_operation_table(pow, 5, 10)

import string as s
def verification(login, password, success, failure):

    d = {0: 'в пароле нет ни одной буквы',
         1: 'в пароле нет ни одной заглавной буквы',
         2: 'в пароле нет ни одной строчной буквы',
         3: 'в пароле нет ни одной цифры'}

    if not any(map(lambda x: True if x in s.ascii_letters else False, list(password))):
        return failure(login, d[0])
    elif not any(map(lambda x: True if x.isupper() else False, list(password))):
        return failure(login, d[1])
    elif not any(map(lambda x: True if x.islower() and x in s.printable else False, list(password))):
        return failure(login, d[2])
    elif not any(map(lambda x: True if x.isdigit() else False, list(password))):
        return failure(login, d[3])
    success(login)



def success(login):
    print(f'Здравствуйте, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Arthur_Davletov', 'мойпарольBEE123', success, failure)







