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
#         if self.n < 2:
#             self.n += 1
#             return 1
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


# class PowerOf:
#     def __init__(self, number):
#         self.number = number
#         self.value = 1
#         self.falg = True
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.falg:
#             self.falg = False
#             return 1
#         self.value *= self.number
#         return self.value
#
# power_of_two = PowerOf(2)
#
# print(next(power_of_two))
# print(next(power_of_two))
# print(next(power_of_two))
# print(next(power_of_two))

# class DictItemsIterator:
#     def __init__(self, data):
#         self.dct_key = [*data]
#         self.data = data
#         self.count = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.count += 1
#         if self.count > len(self.data) - 1:
#             raise StopIteration
#         else:
#             return (self.dct_key[self.count], self.data[self.dct_key[self.count]])
#
#
#
# data = {'Arthur': [100, 5], 'Timur': [100, 6], 'Dima': [100, 7, 8],
#         'Anri': [100, 101], 'Roma': [99]}
#
# pairs = DictItemsIterator(data)
#
# print(next(pairs))
# print(next(pairs))
# print(next(pairs))
# print(next(pairs))
# print(next(pairs))
#
# try:
#     print(next(pairs))
# except StopIteration:
#     print('Error')
#
#
#
# data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}
#
# pairs = DictItemsIterator(data)
#
# print(tuple(pairs))
#
# try:
#     print(next(pairs))
# except StopIteration:
#     print('Error')


# class CardDeck:
#     def __init__(self):
#         self.mast = ("пик", "треф", "бубен", "червей")
#         self.card = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз")
#         self.cards = []
#         [[self.cards.append((j, i)) for j in self.card] for i in self.mast]
#         self.count = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.count += 1
#         if self.count == len(self.cards):
#             raise StopIteration
#         return ' '.join(self.cards[self.count])
#
#
#
# cards = list(CardDeck())
#
# print(cards[9])
# print(cards[23])
# print(cards[37])
# print(cards[51])


# class Cycle:
#     def __init__(self, iterable):
#         self.iterable = iterable
#         self.index = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.index += 1
#         if self.index > len(self.iterable) - 1:
#             self.index = 0
#         return self.iterable[self.index]
#
#
# cycle = Cycle([1])
#
# print(next(cycle) + next(cycle) + next(cycle))

# import random as r
#
# class RandomNumbers:
#     def __init__(self, left, right, n):
#         self.n = n
#         self.count = 0
#         self.range = [*range(left, right + 1)]
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.count += 1
#         if self.count > self.n:
#             raise StopIteration
#         return r.choice(self.range)
#
# iterator = RandomNumbers(-1000, -900, 1)
#
# print(next(iterator) in range(-1000, -899))
#
# try:
#     next(iterator)
# except StopIteration:
#     print('Error')


# class Alphabet:
#     def __init__(self, lang):
#         self.lang = {'ru': [chr(i) for i in range(1072, 1104)], 'en': [chr(i) for i in range(97, 123)]}[lang]
#         self.count = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.count += 1
#         if self. count > len(self.lang) - 1:
#             self.count = 0
#         return self.lang[self.count]
#
# en_alpha = Alphabet('en')
#
# letters = [next(en_alpha) for _ in range(28)]
#
# print(*letters)


# class Xrange:
#     def __init__(self, start, end, step=1):
#         self.flag = True
#         if all(map(lambda x: isinstance(x, int), [start, end, step])):
#             self.num_lst = [*range(start, end, step)]
#         else:
#             self.num_lst = [*range(int(start * 100), int(end * 100), int(step * 100))]
#             self.flag = False
#         self.index = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.index += 1
#         if self.index > len(self.num_lst) - 1:
#             raise StopIteration
#         if self.flag:
#             return self.num_lst[self.index]
#         else:
#             return self.num_lst[self.index]/100
#
# xrange = Xrange(0, 3, 0.5)
#
# print(*xrange, sep='; ')
#
# print(type(xrange))


class Fibonacci:
    def __init__(self):
        self.current_index = 0
        self.cache = {1: 1, 2: 1}

    def __iter__(self):
        return self

    def __next__(self):
        self.current_index += 1
        result = self.cache.get(self.current_index)
        if result is None:
            first = self.cache[self.current_index - 2]
            second = self.cache[self.current_index - 1]
            first, second = second, second + first
            result = second
            self.cache[self.current_index] = result
        return result

fibonacci = Fibonacci()

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(type(fibonacci))













