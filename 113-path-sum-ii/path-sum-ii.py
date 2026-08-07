# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # Time complexity: O(n + kh) and Space complexity: O(kh)
        result = []
        path = []

        def dfs(root, remainingSum):
            if root is None:
                return 
            
            path.append(root.val)
            remainingSum -= root.val

            if root.left is None and root.right is None:
                if remainingSum == 0:
                    result.append(path.copy())

            else:
                dfs(root.left, remainingSum)
                dfs(root.right, remainingSum)

            path.pop()

        dfs(root, targetSum)
        return result