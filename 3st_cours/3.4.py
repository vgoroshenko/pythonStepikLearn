# from datetime import datetime, timedelta
#
# dt = datetime(2021, 11, 4, 13, 6) + timedelta(weeks=1, hours=12)
#
# print(dt.strftime('%d.%m.%Y %H:%M:%S'))

# from datetime import date, timedelta
#
# today = date(2021, 11, 4)
# birthday = date(2022, 10, 6)
#
# days = birthday - today
#
# print(days.days)

# from datetime import datetime, date, timedelta
# my_date = input().split('.')
# my_date = datetime(int(my_date[2]), int(my_date[1]), int(my_date[0]))
# dt1 = my_date - timedelta(days=1)
# dt2 = my_date + timedelta(days=1)
# print(dt1.strftime('%d.%m.%Y'))
# print(dt2.strftime('%d.%m.%Y'))

# from datetime import datetime, date, timedelta, time
#
# h, m, s = input().split(':')
# #my_time = time(int(h), int(m), int(s))
# delta = timedelta(hours=int(h), minutes=int(m), seconds=int(s))
# print(int(delta.total_seconds()))


# from datetime import datetime, date, timedelta, time
#
# h, m, s = map(int, input().split(':'))
# ring = int(input())
#
# delta = timedelta(hours=h, minutes=m, seconds=s) + timedelta(seconds=ring)
# my_time = datetime(1, 1, 1, hour=h, minute=m, second=s) + timedelta(seconds=ring)
# print(my_time.time())

# from datetime import datetime, date, timedelta, time
# def num_of_sundays(year):
#     print(timedelta(year))
#     pass

# from datetime import datetime, date, timedelta, time
# d, m, y = map(int, input().split('.'))
#
# start_date = datetime(y, m , d)
#
# print(start_date.strftime('%d.%m.%Y'))
# for i in range(2, 11):
#     dt = start_date + timedelta(days=i)
#     print(dt.strftime('%d.%m.%Y'))
#     start_date = dt


# from datetime import datetime, date, timedelta, time
#
# dates = [list(map(int, i.split('.'))) for i in input().split()]
#
# tmp = []
# for i in range(1, len(dates)):
#     days = datetime(dates[i - 1][2], dates[i - 1][1], dates[i - 1][0]) - datetime(dates[i][2], dates[i][1], dates[i][0])
#     tmp.append(abs(days.days))
#
# print(tmp)

# from datetime import datetime, date, timedelta, time
#
# def fill_up_missing_dates(dates):
#     tmp = []
#     dates = list(map(lambda x: datetime.strptime(x, '%d.%m.%Y'), dates))
#     first_date = min(dates)
#     last_date = max(dates)
#     total_days = (last_date - first_date).days
#     print(first_date.date())
#     tmp.append(first_date.strftime('%d.%m.%Y'))
#     for i in range(total_days):
#         next_date = first_date + timedelta(days=1)
#         tmp.append(next_date.strftime('%d.%m.%Y'))
#         first_date = next_date
#     return tmp
#
# dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']
#
# print(fill_up_missing_dates(dates))
#
#
# dates = ['01.11.2021', '04.11.2021', '09.11.2021', '15.11.2021']
#
# print(fill_up_missing_dates(dates))

# dates = ['20.07.2021', '16.05.2021', '19.01.2021', '18.11.2021', '17.10.2021', '15.03.2021']
# print(len(fill_up_missing_dates(dates)))


# from datetime import datetime, date, timedelta, time
#
# times = list(map(lambda x: datetime.strptime(x, '%H:%M'), [input() for i in range(2)]))
#
# current_time = times[0]
#
# while current_time < times[1]:
#         old_time = current_time
#         current_time += timedelta(minutes=45)
#         new_time = current_time #10:45
#         if current_time <= times[1]:
#             print(f'{old_time.strftime("%H:%M")} - {new_time.strftime("%H:%M")}')
#         current_time += timedelta(minutes=10)





