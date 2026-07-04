class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        # Time and Space complexity: O(n)
        remove = len(nums) - k
        stack = []

        for num in nums:
            while stack and remove > 0 and num < stack[-1]:
                stack.pop()
                remove -= 1

            stack.append(num)

        return stack[:k]