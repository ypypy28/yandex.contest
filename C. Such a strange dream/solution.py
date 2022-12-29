from collections import deque


ALL_NODES = dict()


class Node:
    root = None
    def __init__(self, val, parent=None, left=None, right=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right
        ALL_NODES[val] = self
        if parent is None:
            Node.root = self

    def add_node(self, val):
        if self.left is None:
            self.left = Node(val, parent=self)
        elif self.right is None:
            self.right = Node(val, parent=self)
        else:
            self.add_node_children(val)

    def add_node_children(self, val):
        q = deque((self.left, self.right))
        node = q.popleft()
        while True:
            if None in (node.left, node.right):
                node.add_node(val)
                break
            q.append(node.left)
            q.append(node.right)
            node = q.popleft()

    def swap(self):
        if self.parent is None:
            return
        pp = self.parent.parent
        p = self.parent
        pl = self.parent.left
        vl = self.left
        vr = self.right
        self.parent = pp
        if pp is not None:
            if p is pp.left:
                pp.left = self
            else:
                pp.right = self
        else:
            Node.root = self
        p.parent = self
        if self is pl:
            self.left = p
            p.left = vl
            if vl is not None:
                vl.parent = p
        else:
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
        return ' '.join(self.lvr())


n, q = [int(x) for x in input().split()]
root = Node(1)
for i in range(2, n+1):
    root.add_node(i)

vs = [int(x) for x in input().split()]
for v in vs:
    ALL_NODES[v].swap()
print(Node.root)
