# def print_hello(name: str, upper: bool = False) -> None:
#     if upper:
#         name = name.upper()
#     print(f'Hello, {name}')
#
# print_hello()

# def get_digits(number: int | float) -> list[int]:
#     return [int(i) for i in str(number) if i.isdigit()]
#
#
# print(get_digits(16733))
# print(get_digits(13.909934))
# annotations = get_digits.__annotations__
#
# print(annotations['return'])


# def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
#     return {'name': grades['name'], 'top_grade': max(grades['grades'])}
#
#
# print(top_grade({'name': 'Ruslan', 'grades': [19, 48, 86, 45, 32]}))

# from collections import deque
#
# def cyclic_shift(numbers: list[int | float], step: int) -> None:
#     dc = deque(numbers)
#     dc.rotate(step)
#     numbers[:] = [c for c in dc]
#
#
#
# numbers = [1, 2, 3, 4, 5]
# cyclic_shift(numbers, -2)
#
# print(numbers)


def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
    return {k: v for k, v in enumerate(matrix, 1)}

matrix = [[5, 6, 7], [8, 3, 2], [4, 9, 8]]

print(matrix_to_dict(matrix))




