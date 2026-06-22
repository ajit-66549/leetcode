"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Time and Space complexity: O(n)
        if not head:
            return None

        copy_to_new = {}
        old = head

        while old:
            newNode = Node(old.val)
            copy_to_new[old] = newNode
            old = old.next

        old = head
        while old:
            copy = copy_to_new[old]
            copy.next = copy_to_new[old.next] if old.next else None
            copy.random = copy_to_new[old.random] if old.random else None
            old = old.next

        return copy_to_new[head]