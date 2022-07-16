class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def recurse_to_the_last(self, prev_node, node, to):
        prev_node = node
        if to == 'right':
            if node is None:
                return node
            else:
                self.recurse_to_the_last(prev_node, node.right, to)
        else:
            if node is None:
                return None
            else:
                self.recurse_to_the_last(prev_node, node.left, to)
        return prev_node

    def insert(self, new_val):
        new_node = Node(new_val)

        if new_val > self.root.value:
            node = self.recurse_to_the_last(self.root, self.root, 'right')
        else:
            node = self.recurse_to_the_last(self.root, self.root, 'left')

        if node.value > new_val:
            node.left = new_node
        else:
            node.right = new_node

    def recursive_search(self, node, ele):
        if node is None:
            return False
        elif node.value == ele:
            return True
        else:
            self.recursive_search(node.left, ele)
            self.recursive_search(node.right, ele)
            return False

    def search(self, find_val):
        return self.recursive_search(self.root, find_val)


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))
