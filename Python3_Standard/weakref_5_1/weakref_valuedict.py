import gc
import weakref
from pprint import pprint

gc.set_debug(gc.DEBUG_UNCOLLECTABLE)


class TestObj:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Obj <--> {}'.format(self.name)

    def __del__(self):
        print('deleting-->{}'.format(self))


def demo(cache_factory):
    all_refs = {}
    print(cache_factory)
    cache = cache_factory()
    for name in ['one', 'two', 'three']:
        o = TestObj(name)
        cache[name] = o
        all_refs[name] = o
        del o
    print('all_reds', all_refs)
    print('list_1', list(cache.keys()))
    for name, value in cache.items():
        print('-->{}={}'.format(name, value))
        del value
    print('Cleanup:')
    del all_refs
    gc.collect()

    print('list_2', list(cache.keys()))
    for name, value in cache.items():
        print('>>>{}={}'.format(name, value))
    return


demo(dict)
print('=' * 50)
demo(weakref.WeakValueDictionary)
