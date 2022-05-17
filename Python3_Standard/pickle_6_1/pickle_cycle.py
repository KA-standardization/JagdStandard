import pickle


class Node:

    def __init__(self, name):
        self.name = name
        self.connections = []

    def add_edge(self, node):
        self.connections.append(node)

    def __iter__(self):
        return iter(self.connections)


def preorder_traversal(root, seen=None, parent=None):
    if seen is None:
        seen = set()
    yield (parent, root)
    if root in seen:
        return
    seen.add(root)
    for node in root:
        recurse = preorder_traversal(node, seen, root)
        for parent, subnode in recurse:
            yield (parent, subnode)


def show_edges(root):
    for parent, child in preorder_traversal(root):
        if not parent:
            continue
        print('{:>5} -> {:>2} ({})'.format(parent.name, child.name, id(child)))


root = Node('root')
a = Node('a')
b = Node('b')
c = Node('c')

root.add_edge(a)
root.add_edge(b)
a.add_edge(b)
a.add_edge(a)
b.add_edge(a)
b.add_edge(c)

show_edges(root)

dumped = pickle.dumps(root)
reloaded = pickle.loads(dumped)

print('=' * 88)
show_edges(reloaded)
