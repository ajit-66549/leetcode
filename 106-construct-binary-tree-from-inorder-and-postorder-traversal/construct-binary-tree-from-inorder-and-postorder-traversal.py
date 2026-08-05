# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Time and Space complexity: O(n)
        postorder_index = len(postorder) - 1

        inorder_position = {}
        for index, value in enumerate(inorder):
            inorder_position[value] = index

        def build(inorder_left, inorder_right):
            if inorder_left > inorder_right:
                return None

            nonlocal postorder_index
            root_value = postorder[postorder_index]
            postorder_index -= 1
            inorder_index = inorder_position[root_value]

            root = TreeNode(root_value)
            root.right = build(inorder_index+1, inorder_right)
            root.left = build(inorder_left, inorder_index-1)

            return root

        return build(0, len(inorder) - 1)