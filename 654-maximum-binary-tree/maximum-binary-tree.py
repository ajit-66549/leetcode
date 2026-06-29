# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # Time and Space complexity: O(n)
        stack = []

        for num in nums:
            current = TreeNode(num)
            last_popped = None

            while stack and current.val > stack[-1].val:
                last_popped = stack.pop()

            current.left = last_popped

            if stack:
                stack[-1].right = current

            stack.append(current)

        return stack[0]