# import pickle
# import sys
#
# with open(input(), 'rb') as file:
#     my_func = pickle.load(file)
#     print(my_func(*[i.strip() for i in sys.stdin]))

# import pickle
#
# def filter_dump(filename, object, type):
#     with open(filename, 'wb') as file:
#         pickle.dump(list(filter(lambda x: isinstance(x, type), object)), file)


import pickle

with open(input(), 'rb') as file:
    control = int(input())
    obj = pickle.load(file)
    if type(obj) == dict:
        obj_sum = sum(list(filter(lambda x: isinstance(x, int), obj.keys())))
        print('Контрольные суммы совпадают' if obj_sum == control else 'Контрольные суммы не совпадают')
    elif type(obj) == list:
        obj = list(filter(lambda x: isinstance(x, int), obj))
        if obj:
            obj_mnoj = min(obj, key=int) * max(obj, key=int)
        else:
            obj_mnoj = 0
        print('Контрольные суммы совпадают' if obj_mnoj == control else 'Контрольные суммы не совпадают')




