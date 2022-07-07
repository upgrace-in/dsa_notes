# Return true if it is a palindrome number
from linked_list import ListNode, parse_linked_list, linked_to_list


class Solution:
    def isPalindrome(self, head):
        # Palindrome number are the number which are same when reversed i.e 121 is 121 when reversed
        def parse_linked_list(data, i=0):
            if i == len(data):
                return None
            node = ListNode(data[i])
            node.next = parse_linked_list(data, i+1)
            return node

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

        head2 = reverseList(head)
        while head:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        return True


lst = [1, 2, 3, 1]
s = Solution().isPalindrome(parse_linked_list(lst))
print(s)
