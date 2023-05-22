asd = 0
# def recursive_sum(nested_list, total=0):
#     if not nested_list:
#         return 0
#     for i in nested_list:
#         if isinstance(i, int):
#             total += i
#         else:
#             total += recursive_sum(i)
#     return total
#
# my_list = [1, [4, 4], 2, [1, [2, 10]]]
#
# print(recursive_sum(my_list))


# def linear(li):
#     new_list = []
#     for elem in li:
#         if isinstance(elem, list):
#             new_list.extend(linear(elem))
#         else:
#             new_list.append(elem)
#     return new_list
#
#
# my_list = [3, [4], [5, [6, [7, 8]]]]
#
# print(linear(my_list))


# def get_value(nested_dict, key):
#     if key in nested_dict:
#         return nested_dict[key]
#     for v in nested_dict.values():
#         if type(v) == dict:
#             value = get_value(v, key)
#             if value is not None:
#                 return value
#
# data = {'firstName': 'Тимур', 'lastName': 'Гуев', 'birthDate': {'day': 10, 'month': 'October', 'year': 1993}, 'address': {'streetAddress': 'Часовая 25, кв. 127', 'city': {'region': 'Московская область', 'type': 'город', 'cityName': 'Москва'}, 'postalCode': '125315'}}
#
# print(get_value(data, 'cityName'))

def get_all_values(nested_dict, key):
    myset = set()
    if key in nested_dict:
        return nested_dict[key]
    for v in nested_dict.values():
        if type(v) == dict:
            value = get_all_values(v, key)
            if value is not None:
                myset.add(value)
    return myset

my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
result = get_all_values(my_dict, 'top_grade')

print(*sorted(result))

# my_dict = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 'Timur': {'hobby': 'math'}}
# result = get_all_values(my_dict, 'top_grade')
#
# print(len(sorted(result)))



