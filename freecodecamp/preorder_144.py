from django.conf import PASSWORD_RESET_TIMEOUT_DAYS_DEPRECATED_MSG
from binarytree import parse_tuple

class Solution:
    def preorderTraversal(self, root):
        final_list = []
        def recurs(root, lst):
            if root is None:
                return []
            else:
                _recurs = lst.append(root.key)
                left = recurs(root.left, lst)
                right = recurs(root.right, lst)
            return root
        recurs(root, final_list)
        return final_list

root_arr = (None, 1, (3, 2, None))
output = [1,2,3]
root = parse_tuple(root_arr)
s = Solution().preorderTraversal(root)
print(s==output)
