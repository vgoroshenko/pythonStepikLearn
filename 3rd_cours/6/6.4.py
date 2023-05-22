# from collections import namedtuple
#
# Fruit = namedtuple('Fruit', ['name', 'color', 'vitamins'])
import pickle
# from collections import namedtuple
#
# Game = namedtuple('Game', 'name developer publisher')
#
# ExtendedGame = namedtuple('ExtendedGame', [*Game._fields, *['release_date', 'price']])
#
# print(ExtendedGame._fields)


# from collections import namedtuple
#
# Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])
#
# with open('data.pkl', 'rb') as file:
#     p_file = pickle.load(file)
#     for i in p_file:
#         [print(field, value, sep=': ') for field, value in zip(i._fields, i)]
#         print()

# from collections import namedtuple
#
# User = namedtuple('User', ['name', 'surname', 'email', 'plan'])
#
# users = [User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
#          User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
#          User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
#          User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
#          User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
#          User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
#          User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
#          User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
#          User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
#          User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
#          User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
#          User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
#          User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
#          User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
#          User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')]
#
# users.sort(key=lambda x: (('Gold', 'Silver', 'Bronze', 'Basic').index(x.plan), x.email))
#
# [print(f'{i.name} {i.surname}\n  Email: {i.email}\n  Plan: {i.plan}\n') for i in users]


from collections import namedtuple
import csv
from datetime import datetime

with open('meetings.csv', 'r', encoding='utf-8') as file:
    meets = list(csv.reader(file))
    Meet = namedtuple('Meet', meets[0])
    meetings = [Meet(i[0], i[1], datetime.strptime(i[2], '%d.%m.%Y'), datetime.strptime(i[3], '%H:%M')) for i in meets[1:]]
    meetings.sort(key=lambda x: (x.meeting_date, x.meeting_time))
    [print(i.surname, i.name) for i in meetings]





