# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Time complexity: O(n) and Space complexity: O(1)
        small_dummy = ListNode(0)
        big_dummy = ListNode(0)

        small = small_dummy
        big = big_dummy

        current = head

        while current:
            if current.val < x:
                small.next = current
                small = small.next
            else:
                big.next = current
                big = big.next
            current = current.next

        big.next = None
        small.next = big_dummy.next

        return small_dummy.next