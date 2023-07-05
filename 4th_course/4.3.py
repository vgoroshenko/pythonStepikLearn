# class Gun():
#     def shoot(self):
#         print('pif')
#
#
# gun = Gun()
#
# gun.shoot()
# gun.shoot()
# gun.shoot()


# class User:
#     def __init__(self, name):
#         self.name = name
#         self.friends = 0
#
#     def add_friends(self, n):
#         self.friends += n


# class House:
#     def __init__(self, color, rooms):
#         self.color = color
#         self.rooms = rooms
#
#     def paint(self, new_color):
#         self.color = new_color
#
#     def add_rooms(self, n):
#         self.rooms += n
#
# house = House('white', 4)
#
# house.paint('black')
# house.add_rooms(1)
#
# print(house.color)
# print(house.rooms)

# from math import pi
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#         self.diameter = 2 * radius
#         self.area = pi * radius ** 2
#
#     def radius(self):
#         print(self.area)
#
# circle = Circle(5)
#
# print(circle.radius)
# print(circle.diameter)
# print(circle.area)


# class Bee:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def move_up(self, n):
#         self.y += n
#
#     def move_down(self, n):
#         self.y -= n
#
#     def move_right(self, n):
#         self.x += n
#
#     def move_left(self, n):
#         self.x -= n

# bee = Bee()
#
# bee.move_right(2)
# bee.move_right(2)
# bee.move_up(3)
# bee.move_left(1)
# bee.move_down(1)

# print(bee.x, bee.y)

# from itertools import cycle
# class Gun:
#     def __init__(self):
#         self.shoot_sound = cycle(['pif', 'paf'])
#     def shoot(self):
#         print(next(self.shoot_sound))
#
# gun = Gun()
#
# gun.shoot()
# gun.shoot()
# gun.shoot()
# gun.shoot()

# from itertools import cycle
# class Gun:
#     def __init__(self):
#         self.shoot_sound = (i for i in cycle(['pif', 'paf']))
#         self.shoot_count = 0
#     def shoot(self):
#         if not self.shoot_count:
#             self.shoot_sound.close()
#             self.shoot_sound = (i for i in cycle(['pif', 'paf']))
#         print(next(self.shoot_sound))
#         self.shoot_count += 1
#
#     def shots_count(self):
#         return self.shoot_count
#
#     def shots_reset(self):
#         self.shoot_count = 0
#
# gun = Gun()
#
# gun.shoot()
# gun.shoot()
# print(gun.shots_count())
# gun.shots_reset()
# print(gun.shots_count())
# gun.shoot()
# print(gun.shots_count())


# class Scales:
#     def __init__(self):
#         self.right = 0
#         self.left = 0
#
#     def add_right(self, n):
#         self.right += n
#
#     def add_left(self, n):
#         self.left += n
#
#     def get_result(self):
#         if self.right == self.left:
#             return 'Весы в равновесии'
#         else:
#             return 'Правая чаша тяжелее' if self.right > self.left else 'Левая чаша тяжелее'
#
# scales = Scales()
# scales1 = Scales()
#
# scales.add_right(1)
# scales.add_left(2)
#
# print(scales.get_result())
#
# print([scales, scales1])


# class Vector:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def abs(self):
#         return (self.x ** 2 + self.y ** 2) ** 0.5
#
# vector = Vector(3, 4)
#
# print(vector.x, vector.y)
# print(vector.abs())

# class Numbers():
#     def __init__(self):
#         self.numbers = []
#
#     def add_number(self,n):
#         self.numbers.append(n)
#
#     def get_odd(self):
#         return [i for i in self.numbers if i % 2]
#
#     def get_even(self):
#         return [i for i in self.numbers if not i % 2]

# numbers = Numbers()
#
# numbers.add_number(3)
# numbers.add_number(2)
# numbers.add_number(1)
# numbers.add_number(4)

# print(numbers.get_even())
# print(numbers.get_odd())


# class TextHandler:
#     def __init__(self):
#         self.words = []
#
#     def add_words(self, word):
#         [self.words.append(i) for i in word.split()]
#
#     def get_shortest_words(self):
#         return list(filter(lambda x: len(x) == len(min(self.words, key=len)), self.words))
#
#     def get_longest_words(self):
#         return list(filter(lambda x: len(x) == len(max(self.words, key=len)), self.words))
#
#
# texthandler = TextHandler()
#
# texthandler.add_words('The world will hold my trial for your sins')
# texthandler.add_words('Never meant to see the sky, never meant to live')
#
# print(texthandler.get_shortest_words())
# print(texthandler.get_longest_words())


# class Todo:
#     def __init__(self):
#         self.things = []
#
#     def add(self, *args):
#         self.things.append(args)
#
#     def get_by_priority(self, n: int):
#         return list(i[0] for i in self.things if i[1] == n)
#
#     def get_low_priority(self):
#         return list(i[0] for i in self.things if i[1] == min(self.things, key=lambda x: x[1])[1])
#
#     def get_high_priority(self):
#         return list(i[0] for i in self.things if i[1] == max(self.things, key=lambda x: x[1])[1])
#
# todo = Todo()
#
# todo.add('Ответить на вопросы', 5)
# todo.add('Сделать картинки', 1)
# todo.add('Доделать задачи', 4)
# todo.add('Дописать конспект', 5)
#
# print(todo.get_low_priority())
# print(todo.get_high_priority())
# print(todo.get_by_priority(3))

# class Postman:
#     def __init__(self):
#         self.delivery_data = []
#
#     def add_delivery(self, *args):
#         self.delivery_data.append(args)
#
#     def get_houses_for_street(self, street):
#         tmp = []
#         [(tmp.append(i[1]) if i[1] not in tmp else '') for i in self.delivery_data if street in i]
#         return tmp
#
#     def get_flats_for_house(self, street, house):
#         tmp = []
#         [(tmp.append(i[2]) if i[2] not in tmp else '') for i in self.delivery_data if street in i and house in i]
#         return tmp
#
#
# postman = Postman()
#
# postman.add_delivery('Советская', 151, 74)
# postman.add_delivery('Советская', 151, 75)
# postman.add_delivery('Советская', 90, 2)
# postman.add_delivery('Советская', 151, 74)
#
# print(postman.get_houses_for_street('Советская'))
# print(postman.get_flats_for_house('Советская', 151))


class Wordplay:
    def __init__(self, words=[]):
        self.words = [] + words

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, word_len: int):
        return [i for i in self.words if len(i) == word_len]

    def only(self, *args):
        return list(i for i in self.words if all(map(lambda x: x in args, i)))

    def avoid(self, *args):
        return list(i for i in self.words if all(map(lambda x: x not in args, i)))

words = ['Лейбниц', 'Бэббидж', 'Нейман', 'Джобс', 'да_Винчи', 'Касперский']
wordplay = Wordplay(words)

words.extend(['Гуев', 'Харисов', 'Светкин'])
print(words)
print(wordplay.words)



