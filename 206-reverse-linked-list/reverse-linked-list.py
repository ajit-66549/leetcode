# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time complexity: O(n) and Space complexity: O(1)
        current = head
        previous = None
        nxt = None

        while current:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt

        return previous