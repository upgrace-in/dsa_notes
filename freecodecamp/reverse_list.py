class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    def __init__(self):
        self.arr = []

    def reverse_list(self, node):
        values = []
        temp = node
        new_node = temp

        while node:
            values.append(node.val)
            node = node.next

        while temp:
            temp.val = values.pop()
            temp = temp.next

        return new_node

def parse_to_linked_list(data, i=0):
    if i == len(data):
        return None
    node = ListNode(data[i])
    node.next = parse_to_linked_list(data, i+1)
    return node

def linked_to_list(node):
    while node:
        print(node.val)
        node = node.next
    

lst = [1,3,4]
s = Solution().reverse_list(parse_to_linked_list(lst))
linked_to_list(s)