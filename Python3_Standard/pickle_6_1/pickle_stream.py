import io
import pickle
import pprint


# 处理文件的流

class SimpleOBJ:

    def __init__(self, name):
        self.name = name
        self.name_backwards = name[::-1]
        return


data = []
data.append(SimpleOBJ('Kaiser'))
data.append(SimpleOBJ('Kaiserin'))
data.append(SimpleOBJ('Jagd'))
data.append(SimpleOBJ('Tee'))

out_s = io.BytesIO()

for o in data:
    pickle.dump(o, out_s)
    out_s.flush()

in_s = io.BytesIO(out_s.getvalue())

while True:
    try:
        o = pickle.load(in_s)
    except EOFError:
        break
    else:
        print('READ: {} {}'.format(o.name, o.name_backwards))

