# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Time complexity: O(n) and Space complexity: O(1)
        if k == 0 or not head or not head.next:
            return head

        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        k = k % length

        tail.next = head

        target_loc = length - k - 1

        new_tail = head
        for _ in range(target_loc):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head