# from random import choice
#
# def test_iter():
#     values = list(range(1, 11))
#     return choice(values)
#
# random_iterator = iter(test_iter, 2)
#
# for num in random_iterator:
#     print(num)


# infinite_love = iter(lambda : 'i love beegeek!', 1)
#
# print(next(infinite_love))
# print(next(infinite_love))
# print(next(infinite_love))


# def is_iterable(obj):
#     try:
#         next(iter(obj))
#         return True
#     except:
#         return False
#
# print(is_iterable('18731'))



# def is_iterator(obj):
#     try:
#         next(obj)
#         return True
#     except:
#         return False
#
# beegeek = map(str.upper, 'beegeek')
#
# print(is_iterator(beegeek))

# import random as r
# def random_numbers(left, right):
#     tmp = [*range(left, right + 1)]
#     print(tmp)
#     return iter(lambda: r.choice(tmp), right + 1)
#
#
#
# iterator = random_numbers(1, 1)
#
# print(next(iterator))
# print(next(iterator))