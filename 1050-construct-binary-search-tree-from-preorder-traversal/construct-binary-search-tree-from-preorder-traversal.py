# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # Time and Space complexity: O(n)
        root = TreeNode(preorder[0])

        stack = [root]
        for num in preorder[1:]:
            current = TreeNode(num)
            if current.val < stack[-1].val:
                stack[-1].left = current
            else:
                while stack and current.val > stack[-1].val:
                    last_popped = stack.pop()

                last_popped.right = current

            stack.append(current)

        return root