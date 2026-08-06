# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Time complexity: O(n) and Space complexity: O(log n)
        def buildTree(left, right):
            if left > right:
                return None

            middle = left + (right-left)//2
            root = TreeNode(nums[middle])

            root.left = buildTree(left, middle-1)
            root.right = buildTree(middle+1, right)

            return root

        return buildTree(0, len(nums)-1)