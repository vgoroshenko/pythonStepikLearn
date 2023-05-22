# months = {
#     1: "January",
#     2: "February",
#     3: "March",
#     4: "April",
#     5: "May",
#     6: "June",
#     7: "July",
#     8: "August",
#     9: "September",
#     10: "October",
#     11: "November",
#     12: "December"
# }
#
# try:
#     print(months[int(input())])
# except KeyError:
#     print('Введено число из недопустимого диапазона')
# except ValueError:
#     print('Введено некорректное значение')


# def add_to_list_in_dict(data, key, element):
#     try:
#         data[key].append(element)
#     except KeyError:
#         data.update({key: [element]})
#     finally:
#         return None
#
# data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [4, 5, 6]}
# add_to_list_in_dict(data, 'a', True)
# add_to_list_in_dict(data, 'a', -90)
# add_to_list_in_dict(data, 'b', False)
# add_to_list_in_dict(data, 'b', 'beegeek')
# add_to_list_in_dict(data, 'b', None)
# add_to_list_in_dict(data, 'c', [])
#
# print(data)



# try:
#     with open(f'{input()}', encoding='utf-8') as f:
#         for row in f.readlines():
#             print(row.strip())
# except FileNotFoundError:
#     print('Файл не найден')


# week = { 1: "Понедельник", 2: "Вторник", 3: "Среда", 4: "Четверг", 5: "Пятница", 6: "Суббота", 7: "Воскресенье", }
#
# def get_weekday(number):
#     try:
#         if not isinstance(number, int):
#             raise TypeError('Аргумент не является целым числом')
#         elif number in range(1, len(week) + 1):
#             return week[number]
#         else:
#             raise ValueError('Аргумент не принадлежит требуемому диапазону')
#     except (TypeError, ValueError) as err:
#         print(err)
#         return (type(err))
#
# print(get_weekday(7))
#
# try:
#     print(get_weekday('hello'))
# except Exception as err:
#     print(err)
#     print(type(err))
#
# try:
#     print(get_weekday(8))
# except ValueError as err:
#     print(err)
#     print(type(err))


# def get_id(names, name):
#     try:
#         if not isinstance(name, str):
#             raise TypeError('Имя не является строкой')
#         elif not name.isalpha() or not name.istitle():
#             raise ValueError('Имя не является корректным')
#         else:
#             return len(names) + 1
#     except (TypeError, ValueError) as e:
#         return e
#
#
#
#
# names = ['Timur', 'Anri', 'Dima']
# name = 'Arthur'
#
# print(get_id(names, name))
#
# names = ['Timur', 'Anri', 'Dima', 'Arthur']
# name = 'Ruslan1337'
#
# try:
#     print(get_id(names, name))
# except ValueError as e:
#     print(e)
#
# names = ['Timur', 'Anri', 'Dima', 'Arthur', 'Ruslan']
# name = ['E', 'd', 'u', 'a', 'r', 'd']
#
# try:
#     print(get_id(names, name))
# except TypeError as e:
#     print(e)

# import json
#
# try:
#     try:
#         with open(f'{input()}', encoding='utf-8') as f:
#             print(json.load(f))
#     except FileNotFoundError:
#         raise FileNotFoundError('Файл не найден')
#     except:
#         raise ValueError('Ошибка при десериализации')
# except (ValueError, FileNotFoundError) as e:
#     print(e)






