# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Time complexity: O(n log n) and Space complexity: O(log n)
        def buildTree(head):
            if head is None:
                return None

            if head.next is None:
                return TreeNode(head.val)

            slow = fast = head
            previous = None

            while fast and fast.next:
                previous = slow
                slow = slow.next
                fast = fast.next.next

            previous.next = None
            root = TreeNode(slow.val)
            root.left = buildTree(head)
            root.right = buildTree(slow.next)

            return root

        return buildTree(head)