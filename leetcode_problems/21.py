# Merging two Sorted Lists
# lists1 = [1,2,4] and lists2 = [1,3,4]
# final_list = [1,1,2,3,4,4]

from linked_list import ListNode, parse_linked_list, linked_to_list

class Solution:

    def get_the_len(node):
        n = node
        len_list1 = 0
        while n.next is not None:
            n = n.next
            len_list1 += 1
        return len_list1+1

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1

        if l2:
            tail.next = l2

        return tail.next

l1 = parse_linked_list([1, 2, 4])
l2 = parse_linked_list([1, 3, 4])
s = Solution().mergeTwoLists(l1, l2)
linked_to_list(s)

