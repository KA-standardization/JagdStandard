class RBTree:
    def __init__(self):
        self.nil = RBTreeNode(0)
        self.root = self.nil


class RBTreeNode:
    def __init__(self, x):
        self.key = x
        self.size = None
        self.left = None
        self.right = None
        self.parent = None
        self.color = 1


def alter_color(T):
    T.root.color = 2
    T.left.color = 1
    T.right.color = 1


def left_rotate(T, x):
    y = x.right
    x.right = y.left
    if y.left != T.nil:
        y.left.parent = x

    y.parent = x.parent
    if x.parent == T.nil:
        T.root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x
    x.parent = y


def right_rotate(T, x):
    y = x.left
    x.left = y.right
    if y.right != T.nil:
        y.right.parent = x
    y.parent = x.parent
    if x.parent == T.nil:
        T.root = y
    elif x == x.parent.right:
        x.parent.right = y
    else:
        x.parent.left = y
    y.right = x
    x.parent = y
