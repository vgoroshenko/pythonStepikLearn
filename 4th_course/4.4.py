# from math import pi
# class Circle:
#     def __init__(self, radius):
#         self._radius = radius
#         self._diameter = 2 * radius
#         self._area = pi * radius ** 2
#
#     def get_radius(self):
#         return self._radius
#
#     def get_diameter(self):
#         return self._diameter
#
#     def get_area(self):
#         return self._area
#
#
# circle = Circle(5)
#
# print(circle.get_radius())
# print(circle.get_diameter())
# print(round(circle.get_area()))


# class BankAccount:
#     def __init__(self, balance=0):
#         self._balance = balance
#
#     def get_balance(self):
#         return self._balance
#
#     def deposit(self, amount: int):
#         self._balance += amount
#
#     def withdraw(self, amount: int):
#         if amount <= self._balance:
#             self._balance -= amount
#         else:
#             raise ValueError ('На счете недостаточно средств')
#
#     def transfer(self, account, amount):
#         self.withdraw(amount)
#         account.deposit(amount)
#
#
# account = BankAccount(balance=10)
# account.withdraw(10)
# print(account.get_balance())


class User:
    def __init__(self, name, age):
        self._name = self.check_name(name)
        self._age = self.check_age(age)

    def check_name(self, name: str):
        if isinstance(name, str) and name.isalpha() and len(name):
            return name
        else:
            raise ValueError('Некорректное имя')

    def check_age(self, age: int):
        if isinstance(age, int) and age in range(0, 111):
            return age
        else:
            raise ValueError('Некорректный возраст')

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self.check_name(new_name)
        self._name = new_name

    def set_age(self, new_age):
        self.check_name(new_age)
        self._age = new_age

    def get_age(self):
        return self._age


user = User('Гвидо', 67)

print(user.get_name())
print(user.get_age())

