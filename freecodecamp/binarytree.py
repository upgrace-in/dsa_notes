class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def parse_tuple(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node


def display_keys(node, space, level=0):
    if node is None:
        print(space*level + '*')
        return

    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return

    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left, space, level+1)


def tranverse_in_order(node):
    if node is None:
        return []
    return(tranverse_in_order(node.left) +
           [node.key] +
           tranverse_in_order(node.right))


def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))


def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_height(node.left) + tree_height(node.right)

# Optional PART
def tree_inorder_iterate(root):
    ''' 
        Test cases -> if the node is empty or contains no left and right element
        Inorder tranversal -> Print the left then root and then go to the right ones
        Work -> 
    '''
    res = list()
    if not root:
        return res

    s = list()
    cur = root
    while cur or s:
        print("CUR:", cur)
        print("S:", s)
        if cur:
            s.append(cur)
            cur = cur.left
        else:
            node = s[-1]
            s.pop()
            res.append(node.key)
            cur = node.right
    return res

# A Binary Search tree follow two rules :
# 1) left tree of any node only contains nodes with keys less than the node's key
# 1) right tree of any node only contains nodes with keys greater than the node's key


def remove_none(nums):
    return [x for x in nums if x is not None]


def is_bst(node):
    if node is None:
        return True, None, None

    is_bst_l, min_l, min_r = is_bst(node.left)
    is_bst_r, max_l, max_r = is_bst(node.right)

    is_bst_node = (is_bst_l and is_bst_r and 
                    (max_l is None or node.key > max_l) and 
                    (max_r is None or node.key < min_l))

    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))

    print(is_bst_node, min_key, max_key)

    return is_bst_node, min_key, max_key

# n = parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
# n = parse_tuple((2,3,(1,5,4)))
# is_bst(n)
# tree_inorder_iterate(n)
# display_keys(n, '  ')
# print(tranverse_in_order(n))
# print(tree_size(n))
# ENCAPSULATION means keeping all functions realting to a particular data structure in one class - it's a very good method of coding
