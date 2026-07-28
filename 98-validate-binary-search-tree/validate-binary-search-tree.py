# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Time and Space complexity: O(n)
        def helper(node, lowerBound, upperBound):
            if node is None:
                return True

            if not (lowerBound < node.val < upperBound):
                return False

            left_is_valid = helper(node.left, lowerBound, node.val)

            right_is_valid = helper(node.right, node.val, upperBound)

            return left_is_valid and right_is_valid

        return helper(root, -float("inf"), float("inf"))