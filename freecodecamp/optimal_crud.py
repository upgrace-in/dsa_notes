# Doing CRUD function for a USERDATABASE efficiently

# Basic way implementing objects and classes in PYTHON
from binarytree import tree_size

class User:
    def __init__(self, username, name, email):
        self.username = username
        self.email = email
        self.name = name
    
    def __repr__(self):
        return "Hi {}".format(self.username)

    def __str__(self):
        return self.__repr__()

#Brute Force
class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)
        return user.email

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user
    
    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users

# Optimal Solution using BST
class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
            
def insert(node, key, value):
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node


def find(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key)
    if key > node.key:
        return find(node.right, key)

def update(node, key, value):
    target = find(node, key)
    if target is not None:
        target.value = value

def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)

def balanced_bst(node):
    return make_balanced_bst(list_all(node))

# Check if the BST is BALANCED
def is_balanced(node):
    if node is None:
        return True, 0
    balanced_l, height_l = is_balanced(node.left)
    balanced_r, hieght_r = is_balanced(node.right)
    balanced = balanced_l and balanced_r and abs(height_l - hieght_r) <= 1
    height = 1 + max(height_l, hieght_r)
    return balanced, height

def make_balanced_bst(data, lo=0, hi=None, parent=None):
    if hi is None:
        hi = len(data)-1
    if lo > hi:
        return None

    mid = (lo+hi) // 2
    key, value = data[mid]

    root = BSTNode(key, value)
    root.parent = parent
    root.left = make_balanced_bst(data, lo, mid-1, root)
    root.right = make_balanced_bst(data, mid+1, hi, root)

    return root

class Treemap():
    def __init__(self):
        self.root = None

    def __setitem__(self, key, value):
        node = find(self.root, key)
        if not node:
            self.root = insert(self.root, key, value)
            self.root = make_balanced_bst(self.root)
        else:
            update(self.root, key, value)

    def __getitem__(self, key):
        node = find(self.root, key)
        return node.value if node else None

    def __iter__(self):
        return (x for x in list_all(self.root))

    def __len__(self):
        return tree_size(self.root)


# u1 = User("Hari", "hari", "hari")
# b1 = BSTNode(u1.username, u1)
# print(b1.key)
