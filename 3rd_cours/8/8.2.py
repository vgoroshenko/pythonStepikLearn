# def message(times):
#     if times > 0:
#         print('Это рекурсивная функция.')
#         message(times - 1)
#         print(times)
#
# message(5)


# import sys
#
# nums = [i.strip() for i in sys.stdin]
#
# def print_nums(nums):
# 	def tmp(n):
# 		if n < len(nums):
# 			tmp(n+1)
# 			print(nums[n])
# 	tmp(0)
#
# print_nums(nums)


# def triangle(h):
# 	if h > 0:
# 		triangle(h - 1)
# 		print('*' * h)
#
# triangle(5)


# def clock(n):
# 	def tmp(h):
# 		if h -1 < n:
# 			print(f'{h}' * (20 - n))
# 			tmp(h + 1)
# 			print(f'{h}' * (20 - n))
# 	tmp(1)
#
#
# clock(4)


# def clock(n):
# 	def tmp(h):
# 		if n > 0:
# 			print(n)
# 			clock(n - 1)
# 	tmp(0)
# 	print(n)
# clock(4)


def print_digits(nums):
    nums = str(nums)
    def tmp(n):
        if n < len(nums):
            print(nums[n])
            tmp(n + 1)

    tmp(0)

print_digits(2077)




