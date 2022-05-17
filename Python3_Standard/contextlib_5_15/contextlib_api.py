class Context:

    def __init__(self):
        print('1: __init__')

    def __enter__(self):
        print('2: __enter__')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('4: __exit__')


with Context():
    print('3: Context')
