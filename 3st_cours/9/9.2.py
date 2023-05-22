from collections import defaultdict
# def hash_as_key(object):
#     tmp = dict()
#     for i in object:
#         if i not in tmp:
#             tmp[i] = hash(i)
#         else:
#             tmp[i] = [tmp[i]] + [hash(i)]
#     return tmp

# def hash_as_key(object):
#     hash_list = [hash(i) for i in object]
#     hash_list = dict(zip(object, hash_list))
#     result = dict()
#     for i in object:
#         result[hash_list[i]] = result.get(hash_list[i], []) + [i]
#     for i in result:
#         if len(result[i]) == 1:
#             result[i] = i
#     return result
#
#
#
# data = [1, 2, 3, 4, 5, 5]
#
# print(hash_as_key(data))
#
# data = [-1, -2, -3, -4, -5]
#
# print(hash_as_key(data))
#
# data = [11, 22, 33, 44, 55, 66, 77, 88, 99, 111]
#
# print(hash_as_key(data))
#
# data = [(1, 2, 3), (1, 2, 3), (0, 0, 0), 10, (144, 75, 60), 20, 30]
#
# print(hash_as_key(data))


# code = '100 + 10*7 - 14'
#
# result = exec(code)
#
# print(result)


