# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        # Time complexity: O(n) and Space complexity: O(1)
        """
        Do not return anything, modify root in-place instead.
        """
        previous = first = second = None

        current = root
        
        while current:
            # no left subtree, process current and move right
            if not current.left:
                if previous and previous.val > current.val:
                    if first is None:
                        first = previous
                    second = current

                previous = current
                current = current.right

            # has left subtree
            else:
                predecessor = current.left

                while predecessor.right and predecessor.right is not current:
                    predecessor = predecessor.right

                if predecessor.right is None:
                    predecessor.right = current
                    current = current.left

                else:
                    predecessor.right = None

                    if previous and previous.val > current.val:
                        if first is None:
                            first = previous
                        second = current

                    previous = current
                    current = current.right

        if first and second:
            first.val, second.val = second.val, first.val