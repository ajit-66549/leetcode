class Solution:
    def rob(self, nums: List[int]) -> int:
        # Time complexity: O(n) and Space complexity: O(1)
        if len(nums) < 3:
            return max(nums)

        previousOne = previousTwo = 0

        for money in nums:
            current = max(previousOne, money + previousTwo)
            previousTwo = previousOne
            previousOne = current

        return previousOne