# import csv
#
# with open('grades.csv', encoding='utf-8') as csv_file:
#     # считываем содержимое файла
#     #text = csv_file.read()
#     # создаем reader объект и указываем в качестве разделителя символ ;
#     rows = csv.reader(csv_file, delimiter=';')
#     # выводим каждую строку
#     for row in rows:
#         print(row)
import csv


# import csv
#
# with open('writing_test.csv', 'w', encoding='utf-8', newline='') as csv_file:
#     # создаем writer объект и указываем названия столбцов
#     writer = csv.DictWriter(csv_file, fieldnames=['first_col', 'second_col'])
#     # записываем первую строку с названиями столбцов
#     writer.writeheader()
#     # записываем строку с данными
#     writer.writerow({'first_col': 'value1', 'second_col': 'value2'})

# import csv
#
# with open('sales.csv', 'r', encoding='utf-8') as file:
#     #data = file.read()
#     rows = list(csv.reader(file, delimiter=';'))
#     del rows[0]
#     for i in filter(lambda x: int(x[2]) < int(x[1]), rows):
#         print(i[0])


# import csv, numpy
#
# with open('salary_data.csv', 'r', encoding='utf-8') as f:
#     rows = list(csv.reader(f, delimiter=';'))[1:]
#     tmp = {}
#     for key, value in rows:
#         tmp[key] = tmp.get(key, []) + [int(value)]
#     tmp_sort = sorted(tmp, key=lambda x: (numpy.mean(tmp[x]), x))
#     # for key,value in tmp.items():
#     #     tmp[key] = numpy.mean(value)
#     # tmp = dict(sorted(tmp.items(), key=lambda x: x[1]))
#     print(*tmp, sep='\n')


# import csv
#
# with open('deniro.csv', 'r', encoding='utf-8') as f:
#     rows = list(csv.reader(f))
#     stolb = int(input()) - 1
#     rows = sorted(rows, key=lambda x: int(x[stolb]) if x[stolb].isdigit() else x[stolb])
#     for i in rows:
#         print(','.join(i))

# def csv_columns(file):
#     with open(file, 'r', encoding='utf-8') as f:
#         rows = csv.DictReader(f, delimiter=';')
#         tmp_key = []
#         tmp_value = []
#         for i in rows:
#             print(i.keys())
#         # rows[0]
#         # for i in rows[:]:
#         #     print(i.values())
#     pass
#
# csv_columns('grades.csv')


# import csv
#
# with open('date.csv', 'r', encoding='utf-8') as f:
#     rows = list(csv.reader(f), delimiter='@')[1:]
#     mail_list = {}
#     for i in rows:
#         domain = i[2][i[2].find('@') + 1:]
#         if domain in mail_list:
#             mail_list[domain] = mail_list[domain] + 1
#         else:
#             mail_list[domain] = 1
#     mail_list = dict(sorted(mail_list.items(), key=lambda x: x[1], reverse=True))
# with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as f:
#     write = csv.writer(f)
#     write.writerow(['domain', 'count'])
#     for key, value in mail_list.items():
#         write.writerow([key, value])


# import csv
#
# with open('wifi.csv', 'r', encoding='utf-8') as f:
#     rows = list(csv.reader(f, delimiter=';'))[1:]
#     location_list = {}
#     for i in rows:
#         loc = i[1]
#         num_loc = int(i[3])
#         if loc in location_list:
#             location_list[loc] = location_list[loc] + num_loc
#         else:
#             location_list[loc] = num_loc
#     location_list = dict(sorted(location_list.items(), key=lambda x: (-x[1],x[0])))
# for key, value in location_list.items():
#     print(f'{key}: {value}')

# import csv
#
# with open('titanic.csv', 'r', encoding='utf-8') as f:
#     rows = list(csv.reader(f, delimiter=';'))[1:]
#     asd = list(filter(lambda x: x[2] == 'male', rows)) + list(filter(lambda x: x[2] == 'female', rows))
#     for i in asd:
#         if i[0] == '1' and float(i[3]) < 18:
#             print(i[1])

# import csv
# from datetime import datetime
#
# with open('name_log.csv', 'r', encoding='utf-8') as f:
#     rows = list(csv.reader(f))[1:]
#     rows = list(map(lambda x: [x[0], x[1], datetime.strptime(x[2], '%d/%m/%Y %H:%M')], rows))
#     tmp = {}
#     for i in rows:
#         email = i[1]
#         if email not in tmp:
#             tmp[email] = i
#         else:
#             if tmp[email][2] < i[2]:
#                 tmp[email] = i
#     tmp = dict(sorted(tmp.items()))
# with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as f:
#     writes = csv.writer(f)
#     writes.writerow(['username','email','dtime'])
#     writes.writerows([[i[0], i[1], i[2].strftime("%d/%m/%Y %H:%M")] for i in tmp.values()])


# def csv_columns(file):
#     with open(file, 'r', encoding='utf-8') as f:
#         tmp = {}
#         rows = list(csv.reader(f))
#         first_row = list(rows[0])
#         for i in range(len(first_row)):
#             tmp_lst = []
#             for j in rows[1:]:
#                 tmp_lst.append(j[i])
#             tmp[first_row[i]] = tmp_lst
#         return tmp
#
# print(csv_columns('test.csv'))

# def condense_csv(file):
#     with open(file, 'r', encoding='utf-8') as f:
#         rows = csv.reader(f)
#         value_rows = [i[::2] for i in rows]
#         column_rows = []
#         for i in rows:
#             if i[1] not in column_rows:
#                 column_rows.append(i[1])
#
#     with open('condensed.csv', 'w', encoding='utf-8') as f:
#         writer = csv.writer(f)
#         writer.writerow(['ID'] + column_rows)
#         writer.writerows(value_rows)