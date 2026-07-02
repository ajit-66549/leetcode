# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # Time and Space complexity: O(n)
        values = []

        current = head
        while current:
            values.append(current.val)
            current = current.next

        answer = [0] * len(values)
        stack = []

        for i in range(len(values)):
            while stack and values[i] > values[stack[-1]]:
                answer[stack.pop()] = values[i]

            stack.append(i)

        return answer