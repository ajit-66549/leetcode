# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time complexity: O(n) and Space complexity: O(1)
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        current = head

        while current:
            if current.next and current.val == current.next.val:
                duplicate = current.val

                while current and current.val == duplicate:
                    current = current.next

                prev.next = current
            else:
                prev = current
                current = current.next

        return dummy.next