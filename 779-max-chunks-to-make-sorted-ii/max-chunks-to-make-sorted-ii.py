class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # Time and Space complexity: O(n)
        stack = []

        for num in arr:
            if not stack or num >= stack[-1]:
                stack.append(num)
            else:
                max_of_chunk = stack.pop()

                while stack and num < stack[-1]:
                    stack.pop()
                
                stack.append(max_of_chunk)

        return len(stack)