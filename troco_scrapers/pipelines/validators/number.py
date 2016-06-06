import re

def is_number(number):
    if isinstance(number, int) or isinstance(number, long):
        return True
    elif isinstance(number, list):
        for num in number:
            if not re.search(r'\d+', num):
                return False
        return True
    elif number is not None:
        return re.search(r'\d+', number)
    return False

def is_not_number(number):
    return not is_number(number)
