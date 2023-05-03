# from collections import defaultdict
#
# data = [('Books', 1343), ('Books', 1166), ('Merch', 616), ('Courses', 966), ('Merch', 1145), ('Courses', 1061), ('Books', 848), ('Courses', 964), ('Tutorials', 832), ('Merch', 642), ('Books', 815), ('Tutorials', 1041), ('Books', 1218), ('Tutorials', 880), ('Books', 1003), ('Merch', 951), ('Books', 920), ('Merch', 729), ('Tutorials', 977), ('Books', 656)]
# tmp = defaultdict(int)
# for i in data:
#     tmp[i[0]] += i[1]
# for key, value in sorted(tmp.items()):
#     print(f'{key}: ${value}')


# from collections import defaultdict
#
# staff = [('Sales', 'Robert Barnes'), ('Developing', 'Thomas Porter'), ('Accounting', 'James Wilkins'), ('Sales', 'Connie Reid'), ('Accounting', 'Brenda Davis'), ('Developing', 'Miguel Norris'), ('Accounting', 'Linda Hudson'), ('Developing', 'Deborah George'), ('Developing', 'Nicole Watts'), ('Marketing', 'Billy Lloyd'), ('Sales', 'Charlotte Cox'), ('Marketing', 'Bernice Ramos'), ('Sales', 'Jose Taylor'), ('Sales', 'Katie Warner'), ('Accounting', 'Steven Diaz'), ('Accounting', 'Kimberly Reynolds'), ('Accounting', 'John Watts'), ('Accounting', 'Dale Houston'), ('Developing', 'Arlene Gibson'), ('Marketing', 'Joyce Lawrence'), ('Accounting', 'Rosemary Garcia'), ('Marketing', 'Ralph Morgan'), ('Marketing', 'Sam Davis'), ('Marketing', 'Gail Hill'), ('Accounting', 'Michelle Wright'), ('Accounting', 'Casey Jenkins'), ('Sales', 'Evelyn Martin'), ('Accounting', 'Aaron Ferguson'), ('Marketing', 'Andrew Clark'), ('Marketing', 'John Gonzalez'), ('Developing', 'Wilma Woods'), ('Sales', 'Marie Cooper'), ('Accounting', 'Kay Scott'), ('Sales', 'Gladys Taylor'), ('Accounting', 'Ann Bell'), ('Accounting', 'Craig Wood'), ('Accounting', 'Gloria Higgins'), ('Marketing', 'Mario Reynolds'), ('Marketing', 'Helen Taylor'), ('Marketing', 'Mary King'), ('Accounting', 'Jane Jackson'), ('Marketing', 'Carol Peters'), ('Sales', 'Alicia Mendoza'), ('Accounting', 'Edna Cunningham'), ('Developing', 'Joyce Rivera'), ('Sales', 'Joseph Lee'), ('Sales', 'John White'), ('Marketing', 'Charles Bailey'), ('Sales', 'Chester Fernandez'), ('Sales', 'John Washington')]
#
# tmp = defaultdict(list)
# for i in staff:
#     tmp[i[0]].append(i[1])
# for key, value in sorted(tmp.items()):
#     print(f'{key}: {len(value)}')


# from collections import defaultdict
#
# staff_broken = [('Developing', 'Miguel Norris'), ('Sales', 'Connie Reid'), ('Sales', 'Joseph Lee'), ('Marketing', 'Carol Peters'), ('Accounting', 'Linda Hudson'), ('Accounting', 'Ann Bell'), ('Marketing', 'Ralph Morgan'), ('Accounting', 'Gloria Higgins'), ('Developing', 'Wilma Woods'), ('Developing', 'Wilma Woods'), ('Marketing', 'Bernice Ramos'), ('Marketing', 'Joyce Lawrence'), ('Accounting', 'Craig Wood'), ('Developing', 'Nicole Watts'), ('Sales', 'Jose Taylor'), ('Accounting', 'Linda Hudson'), ('Accounting', 'Edna Cunningham'), ('Sales', 'Jose Taylor'), ('Marketing', 'Helen Taylor'), ('Accounting', 'Kimberly Reynolds'), ('Marketing', 'Mary King'), ('Sales', 'Joseph Lee'), ('Accounting', 'Gloria Higgins'), ('Marketing', 'Andrew Clark'), ('Accounting', 'John Watts'), ('Accounting', 'Rosemary Garcia'), ('Accounting', 'Steven Diaz'), ('Marketing', 'Mary King'), ('Sales', 'Gladys Taylor'), ('Developing', 'Thomas Porter'), ('Accounting', 'Brenda Davis'), ('Sales', 'Connie Reid'), ('Sales', 'Alicia Mendoza'), ('Marketing', 'Mario Reynolds'), ('Sales', 'John White'), ('Developing', 'Joyce Rivera'), ('Accounting', 'Steven Diaz'), ('Developing', 'Arlene Gibson'), ('Sales', 'Robert Barnes'), ('Sales', 'Charlotte Cox'), ('Accounting', 'Craig Wood'), ('Marketing', 'Carol Peters'), ('Marketing', 'Ralph Morgan'), ('Accounting', 'Kay Scott'), ('Sales', 'Evelyn Martin'), ('Marketing', 'Billy Lloyd'), ('Sales', 'Gladys Taylor'), ('Developing', 'Deborah George'), ('Sales', 'Charlotte Cox'), ('Marketing', 'Sam Davis'), ('Sales', 'John White'), ('Sales', 'Marie Cooper'), ('Marketing', 'John Gonzalez'), ('Sales', 'John Washington'), ('Sales', 'Chester Fernandez'), ('Sales', 'Alicia Mendoza'), ('Sales', 'Katie Warner'), ('Accounting', 'Jane Jackson'), ('Sales', 'Chester Fernandez'), ('Marketing', 'Charles Bailey'), ('Marketing', 'Gail Hill'), ('Accounting', 'Casey Jenkins'), ('Accounting', 'James Wilkins'), ('Accounting', 'Casey Jenkins'), ('Marketing', 'Mario Reynolds'), ('Accounting', 'Aaron Ferguson'), ('Accounting', 'Kimberly Reynolds'), ('Sales', 'Robert Barnes'), ('Accounting', 'Aaron Ferguson'), ('Accounting', 'Jane Jackson'), ('Developing', 'Deborah George'), ('Accounting', 'Michelle Wright'), ('Accounting', 'Dale Houston')]
#
#
# tmp = defaultdict(list)
#
# [tmp[i[0]].append(i[1]) for i in staff_broken]
# [print(f'{key}: {", ".join(sorted(set(value)))}') for key, value in sorted(tmp.items(), key=lambda x: x[0])]


# from collections import defaultdict
#
# def wins(pairs):
#     wins = defaultdict(set)
#     for i in pairs:
#         wins[i[0]].add(i[1])
#     return wins
#
# result = wins([('Тимур', 'Артур'), ('Тимур', 'Дима'), ('Дима', 'Артур')])
#
# for winner, losers in sorted(result.items()):
#     print(winner, '->', *sorted(losers))


from collections import defaultdict

def best_sender(messages, senders):
    lst = list(zip(senders, messages))
    tmp = defaultdict(list)
    for i in lst:
        tmp[i[0]].append(len(i[1].split()))
    return max(sorted(tmp.items(), key=lambda x: len(x[0]), reverse=True), key=lambda x: sum(x[1]))[0]

messages = ['Hi, Linda', 'Hi, Sam', 'How are you doing?']
senders = ['Sam Fisher', 'Linda', 'Sam Fisher']

print(best_sender(messages, senders))

messages = ['How is Stepik for everyone', 'Stepik is useful for practice']
senders = ['Bob', 'Charlie']

print(best_sender(messages, senders))


