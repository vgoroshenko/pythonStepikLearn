# blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2},
#               {'Likes': 13, 'Comments': 2, 'Shares': 1},
#               {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3},
#               {'Comments': 4, 'Shares': 2},
#               {'Photos': 8, 'Comments': 1, 'Shares': 1},
#               {'Photos': 3, 'Likes': 19, 'Comments': 3}]
#
# total_likes = 0
#
# for post in blog_posts:
#     try:
#         total_likes += post['Likes']
#     except:
#         total_likes -= 1
#
# print(total_likes)

# food = ['chocolate', 'chicken', 'corn', 'sandwich', 'soup', 'potatoes', 'beef', 'lox', 'lemonade']
# fifth = []
#
# for x in food:
#     try:
#         fifth.append(x[4])
#     except:
#         fifth.append('_')
#
# print(fifth)


# numbers = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]
#
# remainders = []
#
# for number in numbers:
#     try:
#         remainders.append(36 % number)
#     except:
#         pass
#
# print(remainders)

import sys

txt = sys.stdin
total = 0
total_notdigit = 0

for i in txt:
    try:
        total += int(i)
    except :
        try:
            total += float(i)
        except:
            total_notdigit += 1


print(total, total_notdigit, sep='\n')