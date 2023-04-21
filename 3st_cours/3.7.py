# import calendar
#
# for i in range(int(input())):
#     print(calendar.isleap(int(input())))


# import calendar
#
# day = input().split()
# month_lst = list(calendar.month_abbr)
#
# print(calendar.month(int(day[0]), month_lst.index(day[1])))

# import calendar
#
# inp = list(map(int, input().split('-')))
# print(calendar.day_name[calendar.weekday(inp[0], inp[1], inp[2])])

# import calendar
# month_lst = list(calendar.month_name)
# inp = input().split(' ')
#
#
# print(calendar.monthrange(int(inp[0]), month_lst.index(inp[1]))[1])


# import calendar
# import datetime
#
#
# def get_days_in_month(year, month):
#     month = list(calendar.month_name).index(month)
#     days_month = calendar.monthcalendar(year, month)[-1]
#     for _ in range(days_month.count(0)):
#         days_month.remove(0)
#     qq = [i for i in range(1, int(days_month[-1]) + 1)]
#     dates = []
#     for i in qq:
#         dates.append(datetime.date(year, month, i))
#     print(dates[0])
#     return dates
#
# print(get_days_in_month(2021, 'December'))

# import calendar, datetime
#
# def get_all_mondays(year):
#     mondays = []
#     for month in range(1, 13):
#         days = []
#         [days.extend(list(filter(lambda x: x > 0, i))) for i in calendar.monthcalendar(year, month) if i!= 0]
#         for day in days:
#             if calendar.weekday(year, month, day) == 0:
#                 mondays.append(datetime.date(year, month, day))
#     return mondays
#
# print(get_all_mondays(2021))

import calendar, datetime

year = int(input())
for month in range(1, 13):
    days_month = calendar.monthcalendar(year, month)
    if days_month[0][3] != 0:
        day = days_month[2][3]
    else:
        day = days_month[3][3]
    print(datetime.date(year, month, day).strftime('%d.%m.%Y'))




