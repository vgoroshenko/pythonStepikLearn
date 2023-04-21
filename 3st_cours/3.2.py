# from datetime import time
#
# alarm = time(7, 30, 25)
#
# print('Часы:', alarm.strftime('%H'))
# print('Минуты:', alarm.strftime('%M'))
# print('Секунды:', alarm.strftime('%S'))

# from datetime import time, date
#
# florida_hurricane_dates = [date(1987, 11, 15), date(1988, 3, 12), date(1976, 5, 12)]
# # присваиваем самую раннюю дату урагана в переменную first_date
# first_date = min(florida_hurricane_dates)
#
# # конвертируем дату в ISO и RU формат
# iso = 'Дата первого урагана в ISO формате: ' + str(first_date)
# ru = 'Дата первого урагана в RU формате: ' + first_date.strftime('%d.%m.%y')
# us = 'Дата первого урагана в US формате: ' + first_date.strftime('%m/%d/%y')
#
# print(iso)
# print(ru)
# print(us)



# from datetime import date
#
# andrew = date(1992, 8, 24)
#
# print(andrew.strftime('%Y-%m'))   # выводим дату в формате YYYY-MM
# print(andrew.strftime('%B (%Y)'))   # выводим дату в формате month_name (YYYY)
# print(andrew.strftime('%Y-%j'))   # выводим дату в формате YYYY-day_number

# from datetime import date
#
# dates = [date.fromisoformat(input()) for i in range(2)]
#
# print(min(dates).strftime('%d-%m (%Y)'))


# from datetime import date
#
# dates = sorted([date.fromisoformat(input()) for i in range(int(input()))])
# for i in dates:
#     print(i.strftime('%d/%m/%Y'))

# from datetime import date
#
# interest = []
#
# def print_good_dates(dates):
#     for i in dates:
#         tmp = list(map(int, str(i).split('-')))
#         if sum(tmp[1:]) == 29 and tmp[0] == 1992:
#             interest.append(i)
#     for i in sorted(interest):
#         print(i.strftime('%B %d, %Y'))
#
#
#
# dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
# print_good_dates(dates)

# from datetime import date
#
# def is_correct(d, m ,y):
#     try:
#         date(int(y), int(m), int(d))
#         return 'Корректная'
#     except:
#         return 'Некорректная'
#
#
# #print(is_correct(*input().split('.')))
#
# n = input()
# correct_count = 0
# while n != 'end':
#     print(is_correct(*n.split('.')))
#     if is_correct(*n.split('.')) == 'Корректная':
#         correct_count += 1
#     n = input()
# print(correct_count)

# from datetime import datetime
#
# text = 'Уважаемый пациент, доктор готов принять Вас 15.07.2022 в 08:30'
#
# dt = datetime.strptime(text, 'Уважаемый пациент, доктор готов принять Вас %d.%m.%Y в %H:%M')
#
# print(dt)


# from datetime import datetime
#
# seconds = 2483228800
# dt = datetime(2011, 11, 4)
#
# print(datetime.fromtimestamp(seconds))
# print(dt.timestamp())


# from datetime import datetime
#
# times_of_purchases = [datetime(2017, 10, 1, 12, 23, 25), datetime(2017, 10, 1, 15, 26, 26),
#                       datetime(2017, 10, 1, 15, 42, 57), datetime(2017, 10, 1, 17, 49, 59),
#                       datetime(2017, 10, 2, 6, 37, 10), datetime(2017, 10, 2, 6, 42, 53),
#                       datetime(2017, 10, 2, 8, 56, 45), datetime(2017, 10, 2, 9, 18, 3),
#                       datetime(2017, 10, 2, 12, 23, 48), datetime(2017, 10, 2, 12, 45, 5),
#                       datetime(2017, 10, 2, 12, 48, 8), datetime(2017, 10, 2, 12, 10, 54),
#                       datetime(2017, 10, 2, 19, 18, 10), datetime(2017, 10, 2, 12, 31, 45),
#                       datetime(2017, 10, 3, 20, 57, 10), datetime(2017, 10, 4, 7, 4, 57),
#                       datetime(2017, 10, 4, 7, 13, 31), datetime(2017, 10, 4, 7, 13, 42),
#                       datetime(2017, 10, 4, 7, 21, 54), datetime(2017, 10, 4, 14, 22, 12),
#                       datetime(2017, 10, 4, 14, 50), datetime(2017, 10, 4, 15, 7, 27),
#                       datetime(2017, 10, 4, 12, 44, 49), datetime(2017, 10, 4, 12, 46, 41),
#                       datetime(2017, 10, 4, 16, 32, 33), datetime(2017, 10, 4, 16, 34, 44),
#                       datetime(2017, 10, 4, 16, 46, 59), datetime(2017, 10, 4, 12, 26, 6)]
# count_purch = 0
#
# for i in times_of_purchases:
#     if i.time().hour < 12:
#         count_purch -= 1
#     else:
#         count_purch += 1
#
# print('До полудня') if count_purch < 0 else print('После полудня')

# from datetime import date, time, datetime
#
# dates = [date(2020, 11, 12), date(2021, 7, 2), date(2020, 9, 25)]
# times = [time(12, 50, 22), time(12, 19, 1), time(7, 30, 1)]
#
# datetimes = []
#
# for i in range(len(dates)):
#     datetimes.append(datetime.combine(dates[i], times[i]))
#
#
# print(*sorted(datetimes, key=lambda x: x.second), sep='\n')


# from datetime import datetime
#
# data = {'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'),
#         'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'),
#         'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'),
#         'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'),
#         'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'),
#         'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'),
#         'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'),
#         'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'),
#         'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'),
#         'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'),
#         'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}
#
# dt = datetime.strptime
# new_data = {}
# for k, v in data.items():
#     tmp = dt(v[1], '%d.%m.%Y %H:%M:%S').timestamp() - dt(v[0], '%d.%m.%Y %H:%M:%S').timestamp()
#     new_data.update({k: tmp})
# print(min(new_data.items(), key=lambda x: x[1])[0])

# from datetime import datetime
#
# with open('diary.txt', 'r', encoding='UTF-8') as txt:
#         txt_lst = txt.read().split('\n\n')
#         print(*sorted(txt_lst, key=lambda x: datetime.strptime(x[0:17], '%d.%m.%Y; %H:%M')), sep='\n\n')

# from datetime import datetime
#
# def is_available_date(booked_dates, date_for_booking):
#     book_date = date(boo)
#     if datetime.strptime(date_for_booking, '%d.%m.%Y').timestamp()
#     pass
#
# dates = ['04.11.2021', '05.11.2021-09.11.2021']
# some_date = '01.11.2021'
# print(is_available_date(dates, some_date))






