# Merge k Sorted lists

from typing import List
from linked_list import ListNode, parse_linked_list, linked_to_list

'''
    1) Create a function to compare two elements and put them into the newly create linked list PARA: (ele1, ele2, node)
    2) Call the above function while iterating over the lists

    Test Cases:
    1) Check if it contians only one list node -> return it then
    2) Check if its empty -> return empty list
'''
class Solution:
    def mergeKLists(self, lists):

        node = ListNode(0)

        if len(lists) == 0:
            return []
        elif len(lists) == 1:
            return lists


        def compare_eles(ele1, ele2, node):
            if ele1 > ele2:
                node = ListNode(ele2)
                node.next = ListNode(ele1)
            else:
                node = ListNode(ele1)
                node.next = ListNode(ele2)

        i = 0
        def iterate_the_lists(l1, l2):
            if i == len(lists):
                return node.next

        
        iterate_the_lists(lists[i], lists[i+1])

        return node.next

k1 = parse_linked_list([1,4,5])
k2 = parse_linked_list([1,3,4])
k3 = parse_linked_list([2,6])
lists = [k1, k2, k3]
output = [1,1,2,3,4,4,5,6]
s = Solution().mergeKLists(lists)
if output == linked_to_list(s):
    print(True)
else:
    print(False)


