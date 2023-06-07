# class Repeater:
#     def __init__(self, obj):
#         self.obj = obj
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         return self.obj
#
#
# geek = Repeater('geek')
#
# print(next(geek))
# print(next(geek))
# print(next(geek))


# class BoundedRepeater:
#     def __init__(self, obj, times):
#         self.obj = obj
#         self. times = times
#         self.tmp = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.tmp == self.times:
#             raise StopIteration
#         else:
#             self.tmp += 1
#             return self.obj
#
#
# bee = BoundedRepeater('bee', 2)
#
# print(next(bee))
# print(next(bee))


# class Square:
#     def __init__(self, n):
#         self.n = n
#         self.tmp = 0
#         self.count = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.tmp == self.n:
#             raise StopIteration
#         else:
#             self.tmp += 1
#             value = self.count
#             self.count += 1
#             return value ** 2
#
# squares = Square(10)
#
# print(list(squares))

# class Fibonacci:
#     def __init__(self):
#         self.n = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.n == 0:
#             value = 2
#         else:
#             value = self.n
#         fib = (value - 1) + (value - 2)
#         self.n += fib
#         return fib
#
# fibonacci = Fibonacci()
#
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))


class PowerOf:
    def __init__(self, number):
        self.number = number
        self.value = 1
        self.falg = True

    def __iter__(self):
        return self

    def __next__(self):
        if self.falg:
            self.falg = False
            return 1
        self.value *= self.number
        return self.value

power_of_two = PowerOf(2)

print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))







