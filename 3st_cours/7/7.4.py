# def is_good_password(string):
#     return len(string) >= 9\
#         and any(map(lambda x: x.isdigit(), string)) \
#         and any(map(lambda x: x.isupper(), string))\
#         and any(map(lambda x: x.islower(), string))
#
# print(is_good_password('2asdaAsdasda'))

# class PasswordError(Exception):
#     pass
#
# class LengthError(PasswordError):
#     pass
#
# class LetterError(PasswordError):
#     pass
#
# class DigitError(PasswordError):
#     pass
#
# def is_good_password(string):
#     try:
#         if len(string) < 9:
#             raise LengthError
#         elif not any(map(lambda x: x.isupper(), string)) or not any(map(lambda x: x.islower(), string)):
#             raise LetterError
#         elif not any(map(lambda x: x.isdigit(), string)):
#             raise DigitError
#         else:
#             return True
#     except PasswordError:
#         raise
#
#
# try:
#     print(is_good_password('qwd123asdaw'))
# except Exception as err:
#     print(type(err))
#
#
# try:
#     print(is_good_password('Short7'))
# except Exception as err:
#     print(type(err))
#
# print(is_good_password('еПQSНгиfУЙ70qE'))
#
# try:
#     print(is_good_password('41157081231232'))
# except Exception as err:
#     print(type(err))



class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass

def is_good_password(string):
    try:
        if not len(string) >= 9:
            raise LengthError('LengthError')
        elif not any(map(lambda x: x.isupper(), string)) or not any(map(lambda x: x.islower(), string)):
            raise LetterError('LetterError')
        elif not any(map(lambda x: x.isdigit(), string)):
            raise DigitError('DigitError')
        else :
            print('Success!')
            return True
    except PasswordError:
        raise

import sys

passwords = sys.stdin

for i in passwords:
    try:
        is_good_password(i.strip())
    except PasswordError as e:
        print(e)
        pass
    else:
        break






