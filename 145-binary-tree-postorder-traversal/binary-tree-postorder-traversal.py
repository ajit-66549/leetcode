# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Time and Space complexity: O(n)
        output = []

        def postOrder(node):
            if not node:
                return None

            postOrder(node.left)
            postOrder(node.right)
            output.append(node.val)

        postOrder(root)
        return output