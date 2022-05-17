class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.color = False


class RedBlackTree:
    def __init__(self):
        self.root = None
        self.N = 0

    def size(self):
        return self.N

    def is_red(self, node):
        return str(node.color).lower() == 'red' if node else False

    def rotate_left(self, node):
        """Rotate left when the edge from the current node to its right child node is red"""
        # h is the current node
        h = node
        # x is the current node's right child
        x = node.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = 'Red'
        return x

    def rotate_right(self, node):
        """Rotate right when both the left edge and the left child's left edge are red"""
        h = node
        x = node.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = 'Red'
        return x

    def alter_color(self, node):
        """Alter a node's color"""
        node.color = 'Red'
        node.left.color = 'Black'
        node.right.color = 'Black'

    def put(self, key, val):
        """Put an element into this tree"""

        def put_into(node, key, val):
            if not node:
                return Node(key, val)
            # Rank the order
            if key < node.key:  # Recursively to compare key with its left child
                node.left = put_into(node.left, key, val)
            elif key > node.key:
                node.right = put_into(node.right, key, val)
            else:  # Swap their the node.value with val
                node.value = val
                return node
            # Rotation or alter color
            if self.is_red(node.right) and not self.is_red(node.left):
                # Rotate left
                self.rotate_left(node)
            if self.is_red(node.left) and self.is_red(node.left.left):
                # Rotate right
                self.rotate_right(node)
            if self.is_red(node.left) and self.is_red(node.right):
                # Alter color
                self.alter_color(node)
            self.N += 1
            return node

        self.root = put_into(self.root, key, val)
        self.root.color = 'Black'
        return self.root

    def get(self, key):
        """Get a value according to the given key"""

        def get_value(node, key):
            if not node:
                return
            if key < node.key:
                return get_value(node.left, key)
            elif key > node.key:
                return get_value(node.right, key)
            else:
                return node.value

        val = get_value(self.root, key)
        return val


if __name__ == '__main__':
    RBT = RedBlackTree()

    RBT.put(1, 'G')
    RBT.put(2, 'K')
    RBT.put(3, 'd')
    RBT.put(3, 'D')

    for i in range(1, 4):
        print(RBT.get(i), end=' ')

    print('\n', RBT.size())

    print(RBT.root.color)
    print(RBT.root.key, RBT.root.value)
    print(RBT.root.right.key, RBT.root.right.value)
    print(RBT.root.right.right.key, RBT.root.right.right.value)
