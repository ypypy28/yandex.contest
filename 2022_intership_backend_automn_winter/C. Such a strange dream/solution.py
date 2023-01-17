from collections import deque


class Node:
    root = None
    ALL_NODES = dict()

    def __init__(self, val, parent=None, left=None, right=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right
        Node.ALL_NODES[val] = self
        if parent is None:
            Node.root = self

    def add_node(self, val):
        parent_val, right_child = divmod(val, 2)
        path = []
        while parent_val != 1:
            parent_val, to_right = divmod(parent_val, 2)
            path.append(to_right)
        node = self
        while path:
            if path.pop() == 1:
                node = node.right
            else:
                node = node.left
        if right_child == 1:
            node.right = Node(val, parent=node)
        else:
            node.left = Node(val, parent=node)

    def swap(self):
        if self.parent is None:
           return
        p = self.parent
        pp = p.parent
        vl = self.left
        vr = self.right
        pl = p.left
        pr = p.right

        if pp is not None:
            if p is pp.left:
                pp.left = self
                self.parent = pp
            elif p is pp.right:
                pp.right = self
                self.parent = pp
        else:
            Node.root = self
            self.parent = None

        p.parent = self

        if self is pl:
            self.left = p
            p.left = vl
            if vl is not None:
                vl.parent = p
        elif self is pr:
            self.right = p
            p.right = vr
            if vr is not None:
                vr.parent = p

    def lvr(self):
        res = []
        if self.parent is None:
            res.append(f"{self.val}")
        if self.left is not None:
            res.extend(self.left.lvr())
        if self.parent is not None:
            res.append(f"{self.val}")
        if self.right is not None:
            res.extend(self.right.lvr())
        return res

    def __str__(self):
        return ' '.join(Node.root.lvr())


n, q = [int(x) for x in input().split()]
root = Node(1)
for i in range(2, n+1):
    root.add_node(i)

vs = [int(x) for x in input().split()]
for v in vs:
    Node.ALL_NODES[v].swap()
print(Node.root)
