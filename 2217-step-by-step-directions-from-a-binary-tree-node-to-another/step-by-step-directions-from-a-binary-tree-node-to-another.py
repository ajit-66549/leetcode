# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # Time complexity: O(n) and Space complexity: O(h)
        if root is None:
            return None
        
        def findPath(node, target, path) -> str:
            if node is None:
                return None

            if node.val == target:
                return "".join(path)
            
            path.append('L')
            leftPath = findPath(node.left, target, path)
            path.pop()
            if leftPath is not None:
                return leftPath

            path.append('R')
            rightPath = findPath(node.right, target, path)
            path.pop()
            if rightPath is not None:
                return rightPath

        startPath = findPath(root, startValue, [])
        destPath = findPath(root, destValue, [])

        # find common prefix and remove that
        index = 0
        while (index < len(startPath) and index < len(destPath) and startPath[index] == destPath[index]):
            index += 1

        return ("U" * (len(startPath)-index)) + destPath[index:]