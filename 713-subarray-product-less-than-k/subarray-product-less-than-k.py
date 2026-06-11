class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Time complexity: O(n) and Space complexity: O(1)
        if k <= 1:
            return 0

        left = 0
        product = 1
        result = 0

        for right in range(len(nums)):
            product *= nums[right]
            
            while product >= k:
                product = product / nums[left]
                left += 1

            result += right - left + 1

        return result