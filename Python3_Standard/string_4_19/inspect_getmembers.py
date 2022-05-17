import string
import inspect
import re


def is_str(data):
    return isinstance(data, str)


def start_with(data):
    start_word = data[0]
    pattern = re.compile(r'[0-9]')
    res = re.findall(pattern, start_word)
    if res:
        return True
    return False


for name, var in inspect.getmembers(string, is_str):
    if name.startswith('_') or start_with(name):
        continue
    print(name, ':', var)
