# Remove Linked List Element
# Iterate through the linked lists and check
# if the element is not same put the ele into new node
from linked_list import ListNode, parse_linked_list, linked_to_list

class Solution:
    def removeElements(self, head, val):
        if (head is None):
            return head

        elif head.next == None and head.val == val:
            head = None
            return head

        else:
            dummy = ListNode()
            tail = dummy
            while head:
                if head.val != val:
                    tail.next = head
                    tail = tail.next
                head = head.next

            while tail.next is not None:
                if tail.next.val == val:
                    tail.next = None

        return dummy.next


lst = [1, 2, 6, 3, 4, 5, 6]
l1 = parse_linked_list(lst[::-1])
s = Solution().removeElements(l1, 6)
linked_to_list(s)
