# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def get_perimeter(self):
#         return 2 * (self.length + self.width)
#
#     def get_area(self):
#         return self.width * self.length
#
#     perimeter = property(get_perimeter)
#     area = property(get_area)
#
# rectangle = Rectangle(4, 5)
#
# print(rectangle.length)
# print(rectangle.width)
# print(rectangle.perimeter)
# print(rectangle.area)



# class HourClock:
#     def __init__(self, hours):
#         self.hours = hours
#
#     def get_hours(self):
#         return self._hours
#
#     def set_hours(self, hours):
#         if isinstance(hours, int) and hours in range(1, 13):
#             self._hours = hours
#         else:
#             raise ValueError('Некорректное время')
#
#     hours = property(get_hours, set_hours)
#
# time = HourClock(7)
#
# try:
#     time.hours = 15
# except ValueError as e:
#     print(e)


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_name(self):
        return self.name + ' ' + self.surname

    def set_name(self, name):
        self.name, self.surname = name.split()

    fullname = property(get_name, set_name)

person = Person('Джон', 'Маккарти')

person.fullname = 'Алан Тьюринг'
print(person.name)
print(person.surname)