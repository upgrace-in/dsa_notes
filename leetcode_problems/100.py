class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):

        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False

        def recurse(node, node2):
            if node is None and node2 is None:
                return True
            elif node.val == node2.val:
                left = recurse(node.left, node2.left)
                right = recurse(node.right, node2.right)
                return (left == True and right == True) if True else False
            else:   
                return False

        return recurse(p, q)


def make_tree(arr):
    i = 0
    while i < len(arr)-1:
        node = TreeNode(arr[i])
        node.left = TreeNode(arr[i+1])
        node.right = TreeNode(arr[i+2])
        i += 3
    return node


fst_tree = [1, 2, 3]
snd_tree = [1, 2, 3]

s = Solution()
fst, snd = make_tree(fst_tree), make_tree(snd_tree)
print(s.isSameTree(fst, snd))
