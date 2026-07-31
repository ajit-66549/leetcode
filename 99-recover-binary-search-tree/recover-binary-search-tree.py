# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        # Time and Space complexity: O(n)
        """
        Do not return anything, modify root in-place instead.
        """
        previous = first = second = None

        def inorder(node):
            if not node:
                return 
            
            nonlocal previous, first, second

            inorder(node.left)

            if previous and previous.val > node.val:
                if first is None:
                    first = previous
                
                second = node
            previous = node

            inorder(node.right)

        inorder(root)

        first.val, second.val = second.val, first.val