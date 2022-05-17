import pickle


class SimpleObject:

    def __init__(self, name):
        self.name = name
        l = list(name)
        l.reverse()
        self.name_backwards = ''.join(l)


if __name__ == '__main__':
    data = []
    data.append(SimpleObject('Kaiser'))
    data.append(SimpleObject('Jagd'))
    data.append(SimpleObject('Laune'))

    with open('./file.dat', 'wb') as out_s:
        for o in data:
            print('{} {}'.format(o.name, o.name_backwards))
            pickle.dump(o, out_s)
