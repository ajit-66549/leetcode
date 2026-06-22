# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Time and Space complexity: O(n)
        if not head:
            return None

        current = head
        count = 0

        while current and count < k:
            current = current.next
            count += 1

        if count < k:
            return head

        prev = None
        curr = head

        for _ in range(k):
            nextPtr = curr.next
            curr.next = prev
            prev = curr
            curr = nextPtr

        head.next = self.reverseKGroup(current, k)

        return prev