# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Time complexity: O(n) and Space complexity: O(w) => w: maximum width of the tree
        if root is None:
            return []

        queue = deque([root])
        answer = []
        left_to_right = True

        while queue:
            level_size = len(queue)
            current_nodes = deque()

            for _ in range(level_size):
                node = queue.popleft()
            
                if left_to_right:
                    current_nodes.append(node.val)
                else:
                    current_nodes.appendleft(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            
            left_to_right = not left_to_right
            answer.append(list(current_nodes))

        return answer
            