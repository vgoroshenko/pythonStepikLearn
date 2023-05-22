# from datetime import date, time, datetime, timedelta
#
# data = [('07:14', '08:46'),
#         ('09:01', '09:37'),
#         ('10:00', '11:43'),
#         ('12:13', '13:49'),
#         ('15:00', '15:19'),
#         ('15:58', '17:24'),
#         ('17:57', '19:21'),
#         ('19:30', '19:59')]
#
# tmp = 0
#
# for i in data:
#     times = list(map(lambda x: datetime.strptime(x, '%H:%M'), i))
#     asd = int((times[1] - times[0]).seconds / 60)
#     tmp += asd
# print(tmp)



# from datetime import date, time, datetime, timedelta
#
# current_date = date(1, 1, 1)
#
# my_dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
#
# while current_date != date(9999, 12, 31):
#     if current_date.day == 13:
#         weekday = int(current_date.weekday())
#         my_dict[weekday] = my_dict[weekday] + 1
#     current_date += timedelta(days=1)
#
# print(my_dict)
#
# for i in range(len(my_dict)):
#     print(my_dict[i])


# from datetime import date, time, datetime, timedelta
#
# times = [('09:00', '21:00'),
#         ('09:00', '21:00'),
#         ('09:00', '21:00'),
#         ('09:00', '21:00'),
#         ('09:00', '21:00'),
#         ('10:00', '18:00'),
#         ('10:00', '18:00')]
#
# current_date = datetime.strptime(input(), '%d.%m.%Y %H:%M')
# start_time = datetime.strptime(times[current_date.weekday()][0], '%H:%M')
# end_time = datetime.strptime(times[current_date.weekday()][1], '%H:%M')
#
# if current_date.time() >= start_time.time() and current_date.time() < end_time.time():
#     tmp = list(map(int, str(end_time - current_date).split(', ')[1].split(':')))
#     print(int(timedelta(hours=tmp[0], minutes=tmp[1]).total_seconds() / 60))
# else:
#     print('Магазин не работает')


# from datetime import date, time, datetime, timedelta
#
# dates = list(map(lambda x: datetime.strptime(x, '%d.%m.%Y'), [input() for i in range(2)]))
#
# curr_date = dates[0]
#
# def first_date_check(curr_date):
#     if (curr_date.day + curr_date.month) % 2 == 0:
#         dates[0] = dates[0] + timedelta(days=1)
#         curr_date = dates[0]
#         first_date_check(curr_date)
#
# first_date_check(curr_date)
#
# curr_date = dates[0]
# count_day = 0
#
# while curr_date <= dates[1]:
#     if count_day % 3 == 0:
#         if curr_date.weekday() != 0 and curr_date.weekday() != 3:
#             print(curr_date.date().strftime('%d.%m.%Y'))
#     count_day += 1
#     curr_date += timedelta(days=1)


# from datetime import date, time, datetime, timedelta
#
# personal = [input().split(' ') for i in range(int(input()))]
# qq = []
# for i in personal:
#     qq.append(i[2])
# min_date = min(list(map(lambda x: datetime.strptime(x, '%d.%m.%Y'), qq))).date().strftime('%d.%m.%Y')
# #print(min_date)
# min_personal = []
# for i in personal:
#     if min_date in i:
#         min_personal.append(i)
#         persone = i
# if len(min_personal) > 1:
#     print(min_date, len(min_personal))
# else:
#     print(persone[2], *persone[0:2])


# from datetime import date, time, datetime, timedelta
#
# personal = [input().split(' ') for i in range(int(input()))]
# date_list = []
# for i in personal:
#     date_list.append(i[2])
#
# dates = sorted(list(map(lambda x: datetime.strptime(x, '%d.%m.%Y').date(), date_list)))
# min_personal = []
# min_personal_tmp = []
#
#
# for i in dates:
#     i = i
#     min_personal_tmp.append(i.strftime('%d.%m.%Y'))
#     dc = dates.count(i)
#     if dc > 1:
#         if i.strftime('%d.%m.%Y') not in min_personal:
#             min_personal.append(i.strftime('%d.%m.%Y'))
# if len(min_personal) == 0:
#     min_personal = min_personal_tmp
# print(*min_personal, sep='\n')


# from datetime import date, time, datetime, timedelta
#
# start_date = datetime.strptime(input(), '%d.%m.%Y')
# start_date_list = [start_date + timedelta(days=i) for i in range(7)]
#
# print(start_date_list)
#
# personal = [input().split(' ') for i in range(int(input()))]
#
# date_list = []
# for i in personal:
#     date_list.append(i[2])
#
# date_list = dates = sorted(list(map(lambda x: datetime.strptime(x, '%d.%m.%Y').date(), date_list)))


# from datetime import datetime, timedelta
#
# # Шаг 1
# now = datetime.strptime(input(), '%d.%m.%Y')
#
# # Шаг 2
# n = int(input())
#
# # Шаг 3
# employees = []
# for i in range(n):
#     e = input().split()
#     e[2] = datetime.strptime(e[2], '%d.%m.%Y')
#     employees.append(e)
#
# print(employees)
#
# # Шаг 4
# ages = []
# for e in employees:
#     age = (now - e[2]).days
#     if now.month < e[2].month or (now.month == e[2].month and now.day < e[2].day):
#         age -= 365
#     ages.append(age)
# print(ages)
# # Шаг 5
# min_age = min(ages)
# index = ages.index(min_age)
# if min_age <= 7:
#     print(employees[index][1], employees[index][0])
# else:
#     print('Нет сотрудников, чей день рождения празднуется в течение ближайших семи дней')

# from datetime import datetime, timedelta
#
# # Шаг 1
# date_string = input()
# date = datetime.strptime(date_string, '%d.%m.%Y')
#
# # Шаг 2
# n = int(input())
#
# # Шаг 3
# employees = []
# for i in range(n):
#     e = input().split()
#     e[2] = datetime.strptime(e[2], '%d.%m.%Y')
#     employees.append(e)
#
# # Шаг 4 и Шаг 5
# closest_birthdays = []
# for e in employees:
#     if e[2].month < date.month or (e[2].month == date.month and e[2].day < date.day):
#         next_birthday = datetime(date.year + 1, e[2].month, e[2].day)
#     else:
#         next_birthday = datetime(date.year, e[2].month, e[2].day)
#     days_to_birthday = (next_birthday - date).days
#     closest_birthdays.append(days_to_birthday)
#
# # Шаг 6
# min_index = closest_birthdays.index(min(closest_birthdays))
# print(employees[min_index][1], employees[min_index][0])


from datetime import datetime, timedelta

# Шаг 1
date_string = input()
date = datetime.strptime(date_string, '%d.%m.%Y')

# Шаг 2
n = int(input())

# Шаг 3
employees = []
for i in range(n):
    e = input().split()
    e[2] = datetime.strptime(e[2], '%d.%m.%Y')
    employees.append(e)

# Шаг 4 и Шаг 5
closest_birthdays = []
for e in employees:
    if e[2].month < date.month or (e[2].month == date.month and e[2].day < date.day):
        next_birthday = datetime(date.year + 1, e[2].month, e[2].day)
    else:
        next_birthday = datetime(date.year, e[2].month, e[2].day)
    days_to_birthday = (next_birthday - date).days
    if days_to_birthday <= 7 and days_to_birthday != 0:
        closest_birthdays.append(days_to_birthday)
    else:
        closest_birthdays.append(None)

# Шаг 6
min_index = None
min_age = timedelta(days=1000000)
print(closest_birthdays)
for i in range(len(closest_birthdays)):
    if closest_birthdays[i] is not None and closest_birthdays[i] < min_age:
        min_age = closest_birthdays[i]
        min_index = i

if min_index is not None:
    print(employees[min_index][1], employees[min_index][0])
else:
    print('Никто не отмечает свой день рождения в течение ближайших семи дней от введённой даты')





















