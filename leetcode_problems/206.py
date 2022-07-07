# Reverse any linked list
from linked_list import ListNode, parse_linked_list, linked_to_list

class Solution:
    def reverseList(self, head):
        lst = []
        # iterating over the head node
        while head:
            # putting all into a list
            lst.append(head.val)
            head = head.next
        # itrating over a reverse list

        l1 = parse_linked_list(lst[::-1])
        return l1

lst = [1, 2, 6, 3, 4, 5, 6]
s = Solution().reverseList(parse_linked_list(lst))
linked_to_list(s)
