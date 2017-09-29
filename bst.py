class BST:
    class _Node:
        __slots__ = '_key', '_parent', '_left', '_right'
        def __init__(self, key):
        # create a new node
            self._key = key
            self._left = None
            self._right = None
            self._parent = None

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._root
    
    def inorder_walk(self, x):
        if x != None:
            self.inorder_walk(x._left)
            print(x._key)
            self.inorder_walk(x._right)

    def preorder_walk(self, x):
        if x != None:
            print(x._key)
            self.preorder_walk(x._left)
            self.preorder_walk(x._right)

    def postorder_walk(self, x):
        if x != None:
            self.postorder_walk(x._left)
            self.postorder_walk(x._right)
            print(x._key)

    def search(self, key):
        x = self._root
        while x != None and x._key != key:
            if x._key < key:
                x = x._right
            else:
                x = x._left
        if x == None:
            print('Key not found!')
        else:
            print('Key found!')

    def insert(self, key):
        x = self._root
        if x == None:
            self._root = self._Node(key)
            self._size += 1
            return
        while x != None:
            y = x
            if key < x._key:
                x = x._left
            else:
                x = x._right
        #link parent with child and child with parent
        if y._left == None:
            y._left = self._Node(key)
            y._left._parent = y
        else:
            y._right = self._Node(key)
            y._right._parent = y
        self._size += 1

    def minimum(self, x):
        while x != None:
            y = x
            x = x._left
        return y

    def maximum(self, x):
        while x != None:
            y = x
            x = x._right
        return y

    def predecessor(self, x):
        if x._left != None:
            return self.maximum(x._left)
        y = x._parent
        while y != None and y._left == x:
            x = y
            y = y._parent
        return y

    def successor(self, x):
        if x._right != None:
            return self.minimum(x._right)
        y = x._parent
        while y != None and y._right == x:
            x = y
            y = y._parent
        return y

    def _transplant(self, u, v):
        if u._parent == None:
            self._root = v
        elif u._parent._left == u:
            u._parent._left = v
        else:
            u._parent._right = v
        if v != None:
            v._parent = u._parent

    def delete(self, z):
        self._size -= 1
        if z._right == None:
            self._transplant(z, z._left)
        elif z._left == None:
            self._transplant(z, z._right)
        else:
            y = self.successor(z)
            if y._parent != z:
                self._transplant(y, y._right)
                y._right = z._right
                y._right._parent = y
            self._transplant(z, y)
            y._left = z._left
            y._left._parent = y


T = BST()
T.insert(9)
T.insert(7)
T.insert(10)
T.insert(6)
T.insert(9.5)
T.insert(6.5)


print(len(T))
print(T.minimum(T.root())
#T.inorder_walk(T.root())
T.search(-4)
T.search(13)
#T.delete(T.root())
print()
T.inorder_walk(T.root())
