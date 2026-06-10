class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # Time complexity: O(n) and Space complexity: O(1)
        if len(nums) < 3:
            return 0

        current = 0
        result = 0

        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                current += 1
                result = result + current
            else:
                current = 0
        return result