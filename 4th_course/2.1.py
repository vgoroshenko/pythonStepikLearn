from collections import Counter
def is_correct_bracket(text):
    if text[0] == ')' or text[-1] == '(':
        return False
    count = Counter(text)
    return True if count['('] == count[')'] else False


print(is_correct_bracket(input()))