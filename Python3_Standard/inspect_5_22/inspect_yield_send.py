import inspect


def shorten(string_list):
    length = len(string_list[0])
    print('length:', length)
    for s in string_list:
        print('length2: {}, string_element: {}'.format(length, s))
        length = yield s[:length]


print(inspect.isgeneratorfunction(shorten))

string_list = ['Kaiser', 'Jagd', 'Kaiserin', 'buch']

shortstringlist = shorten(string_list)

res = []

try:
    s = next(shortstringlist)
    res.append(s)
    while True:
        number_of_words = len(list(filter(lambda word: word in 'aeiou', s)))
        s = shortstringlist.send(number_of_words)
        res.append(s)
except StopIteration:
    pass

print(res)
