class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = x
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        # Step 1: Clone each node and insert it next to original
        p = head
        while p:
            copy = Node(p.val)
            copy.next = p.next
            p.next = copy
            p = copy.next

        # Step 2: Assign random pointers for the copy
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next

        # Step 3: Separate original and copied list
        p = head
        head_copy = head.next
        while p:
            copy = p.next
            p.next = copy.next
            copy.next = p.next.next if p.next else None
            p = p.next

        return head_copy
