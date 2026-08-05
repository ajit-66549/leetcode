# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Time and Space complexity: O(n)
        inorder_positions = {}

        for index, value in enumerate(inorder):
            inorder_positions[value] = index

        preorder_index = 0

        def buildTree(inorder_left, inorder_right):
            nonlocal preorder_index

            if inorder_left > inorder_right:
                return None

            root_value = preorder[preorder_index]
            preorder_index += 1

            inorder_index = inorder_positions[root_value]

            root = TreeNode(root_value)
            root.left = buildTree(inorder_left, inorder_index - 1)
            root.right = buildTree(inorder_index + 1, inorder_right)

            return root

        return buildTree(0, len(inorder) - 1)