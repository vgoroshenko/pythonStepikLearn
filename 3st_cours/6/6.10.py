# from collections import ChainMap
#
# fruits = ChainMap({'apple': 10, 'banana': 20},
#                   {'lemon': 10, 'pineapple': 15},
#                   {'kiwi': 15, 'lime': 5})
#
# fruits.maps.append({'mango': 20, 'melon': 20})
#
# print(fruits)


# from collections import ChainMap
#
# def get_all_values(chain, key):
#     return set(i[key] for i in chain.maps if key in i)
#
# chainmap = ChainMap({'name': 'Anri'}, {'name': 'Arthur', 'age': 20}, {'name': 'Timur', 'age': 29})
# result = get_all_values(chainmap, 'age')
#
# print(*sorted(result))

#
# from collections import ChainMap
#
# def deep_update(chain, key, value):
#     if any(map(lambda x: key in x, chain.maps)):
#         for i in chain.maps:
#             if key in i:
#                 i[key] = value
#     else:
#         chain.maps[0].update({key: value})
#
#
# chainmap = ChainMap({'city': 'Moscow'}, {'name': 'Arthur'}, {'name': 'Timur'})
# deep_update(chainmap, 'name', 'Dima')
#
# print(chainmap)
#
# chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
# deep_update(chainmap, 'age', 20)
#
# print(chainmap)


from collections import ChainMap

def get_value(chain, key, from_left=True):
    if not from_left:
        chain.maps.reverse()
    tmp = 0
    if key in chain:
        for i in chain.maps:
            if key not in i:
                tmp += 1
            else:
                return chain.maps[tmp][key]
    else:
        return None


chainmap = ChainMap({'age': 20}, {'city': 'Moscow'}, {'name': 'Anri', 'age': 20}, {'name': 'Timur', 'age': 29})

print(get_value(chainmap, 'name'))


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'name'))


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'name', False))

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'age'))