# # импортируем тип date из модуля datetime
# from datetime import date
#
# # выводим текущую дату
# print(date.today())

# # импортируем тип date из модуля datetime
# from datetime import date
#
# # создаем объект, соответсвующий дате урагана
# hurricane_andrew = date(1992, 8, 24)
#
# # выводим день недели
# print(hurricane_andrew.weekday())

# from datetime import date
#
# florida_hurricane_dates = [date(1987, 11, 15), date(1988, 3, 12), date(1976, 5, 12)]
#
# # счетчик для нужного количества ураганов
# early_hurricanes = 0
#
# # цикл по датам в которые был ураган
# for hurricane in florida_hurricane_dates:
#     # если месяц урагана меньше чем июнь (порядковый номер 6)
#     if hurricane.month < 6:
#         early_hurricanes += 1
#
# print(early_hurricanes)


# from datetime import date
#
# dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11), date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21), date(1666, 6, 6), date(1968, 5, 26)]
#
# for i in dates:
#     print(f'{i.year}-Q{(i.month + 2) // 3}')

# from datetime import date
#
# def get_min_max(dates):
#     if dates:
#         return min(dates), max(dates)
#     else:
#         return ()
#
#
# dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]
#
# print(get_min_max(dates))

# from datetime import date
#
# def get_date_range(start, end):
#     tmp = []
#     for i in range(start.toordinal(), end.toordinal() + 1):
#         tmp.append(date.fromordinal(i))
#     return tmp
#
# date1 = date(2021, 10, 1)
# date2 = date(2021, 10, 5)
#
# print(*get_date_range(date1, date2), sep='\n')

# from datetime import date
#
# def saturdays_between_two_dates(start, end):
#     print(start.weekday())
#     pass
#
#
# date1 = date(2021, 11, 1)
# date2 = date(2021, 11, 22)
#
# print(saturdays_between_two_dates(date1, date2))

