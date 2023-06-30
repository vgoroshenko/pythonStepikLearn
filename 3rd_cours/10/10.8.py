# from itertools import count
# def tabulate(func):
#     return map(func, count(1))
#
# func = lambda x: x + 10
# values = tabulate(func)
#
# print(next(values))
# print(next(values))
# print(next(values))

# from itertools import accumulate
#
# def factorials(n):
#     return accumulate(range(1, n + 1), lambda x, y: y*x)
#
# numbers = factorials(6)
#
# print(*numbers)


# import string
# from itertools import cycle
# def alnum_sequence():
#     return (i for it in cycle(zip(range(1, 27), string.ascii_uppercase)) for i in it)
#
# alnum = alnum_sequence()
#
# print(*(next(alnum) for _ in range(55)))


# def roundrobin(*args):
#     print(*zip(*args))
#
# print(*roundrobin('abc', 'd', 'ef'))


def sort_priority(values, group):
  def helper(x):
    if x in group:
      return (0, x)
    return (1, x)
  values.sort(key=helper)

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {5, 7, 2, 3}
sort_priority(numbers, group)

print(numbers)



