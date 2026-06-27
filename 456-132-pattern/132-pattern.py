class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # Time and Space complexity: O(n)
        stack = []
        third = -inf

        for right in range(len(nums)-1, -1, -1):
            if nums[right] < third:
                return True

            while stack and nums[right] > stack[-1]:
                third = stack.pop()
            stack.append(nums[right])

        return False