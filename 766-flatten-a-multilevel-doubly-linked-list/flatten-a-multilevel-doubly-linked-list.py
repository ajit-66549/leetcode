"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Time and Space complexity: O(n)
        if not head:
            return None

        current = head
        while current:
            nextPtr = current.next
            if current.child:
                current.next = self.flatten(current.child)
                current.next.prev = current
                current.child = None

                while current.next:
                    current = current.next

                if nextPtr:
                    current.next = nextPtr
                    current.next.prev = current
            else:
                current = nextPtr

        return head