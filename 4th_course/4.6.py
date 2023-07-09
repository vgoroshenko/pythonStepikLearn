# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @property
#     def fullname(self):
#         return self.name + ' ' + self.surname
#
#     @fullname.setter
#     def fullname(self, fullname):
#         self.name, self.surname = fullname.split()
#
#
# person = Person('Mike', 'Pondsmith')
#
# print(person.name)
# print(person.surname)
# print(person.fullname)


# def hash_function(password):
#     hash_value = 0
#     for char, index in zip(password, range(len(password))):
#         hash_value += ord(char) * index
#     return hash_value % 10 ** 9
#
# class Account:
#     def __init__(self, login, password):
#         self._login = login
#         self._password = hash_function(password)
#
#     @property
#     def login(self):
#         return self._login
#
#     @login.setter
#     def login(self, login):
#         raise AttributeError('Изменение логина невозможно')
#
#     @property
#     def password(self):
#         return self._password
#
#     @password.setter
#     def password(self, password):
#         self._password = hash_function(password)

# account = Account('timyr-guev', 'lovebeegeek')
# try:
#     account.login = 'timyrik30'
# except AttributeError as e:
#     print(e)


# class QuadraticPolynomial:
#     def __init__(self, a, b, c):
#         self.coefficients = (a, b, c)
#
#     @property
#     def x1(self):
#         return (- self.b - ((self.b ** 2) - (4 * self.a * self.c)) ** 0.5) / (2 * self.a) \
#             if (self.b ** 2) - (4 * self.a * self.c) >= 0 \
#             else None
#
#     @property
#     def x2(self):
#         return (- self.b + (self.b ** 2 - 4 * self.a * self.c) ** 0.5) / (2 * self.a) \
#             if (self.b ** 2) - (4 * self.a * self.c) >= 0 \
#             else None
#
#     @property
#     def view(self):
#         a = f'{self.a}'
#         b = f'+ {self.b}' if self.b >= 0 else f'- {abs(self.b)}'
#         c = f'+ {self.c}' if self.c >= 0 else f'- {abs(self.c)}'
#         return f'{a}x^2 {b}x {c}'
#
#     @property
#     def coefficients(self):
#         return (self.a, self.b, self.c)
#
#     @coefficients.setter
#     def coefficients(self, coef):
#         self.a, self.b, self.c = coef
#
#
#
# polynom = QuadraticPolynomial(500, -601, 101)
#
# print(polynom.a, polynom.b, polynom.c)
# print(polynom.x1)
# print(polynom.x2)
# print(polynom.coefficients)
# print(polynom.view)
#
# print()
#
# polynom.coefficients = (-1000, 1202, -202)
# print(polynom.a, polynom.b, polynom.c)
# print(polynom.x1)
# print(polynom.x2)
# print(polynom.coefficients)
# print(polynom.view)




import re
class Color:
    def __init__(self, hexcode):
        self.hexcode = hexcode
    @property
    def hexcode(self):
        return self._hexcode

    @hexcode.setter
    def hexcode(self, value):
        self.r, self.g, self.b = (int(i, 16) for i in re.findall(r'.{1,2}', value))
        self._hexcode = value

color = Color('0000FF')

color.hexcode = 'A782E3'
print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)
