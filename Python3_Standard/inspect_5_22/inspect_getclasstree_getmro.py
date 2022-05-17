import inspect

import inspect_example


class C(inspect_example.B):
    pass


class D(C, inspect_example.A):
    pass


def print_tree(tree, indent=1):
    if isinstance(tree, list):
        for node in tree:
            print_tree(node, indent + 1)
    else:
        print('   ' * indent, tree[0].__name__)
    return


print_tree(inspect.getclasstree([inspect_example.A, inspect_example.B, C, D]))
print('=' * 88)
print_tree(inspect.getclasstree([inspect_example.A, inspect_example.B, C, D], unique=True))
print('=' * 88)
# 深度优先
for c in inspect.getmro(inspect_example.B):
    print('  {}'.format(c.__name__))
print('=' * 88)
for c in inspect.getmro(C):
    print('  {}'.format(c.__name__))




