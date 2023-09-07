
def is_all_empty(*strings: str):
    for string in strings:
        if string:
            return False
    return True


def is_all_numeric(*strings: str):
    for string in strings:
        if not string.isnumeric():
            return False
    return True


def convert_to_int(*strings: str):
    numbers = []
    for string in strings:
        try:
            numbers.append(int(string))
        except ValueError:
            return None
    return numbers