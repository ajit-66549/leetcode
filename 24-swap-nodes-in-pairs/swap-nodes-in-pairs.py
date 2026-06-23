# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time and Space complexity: O(n)
        if not head:
            return None

        if not head.next:
            return head
        
        prev = None
        current = head

        for _ in range(2):
            nextPtr = current.next
            current.next = prev
            prev = current
            current = nextPtr
        
        head.next = self.swapPairs(current)
        return prev