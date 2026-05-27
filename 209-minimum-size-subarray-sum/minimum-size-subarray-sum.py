class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Time complexity: O(n) and Space complexity:O(1)
        ans = float("inf")
        total = 0
        left = 0

        for i in range(len(nums)):
            total = total + nums[i]

            while total >= target:
                ans = min(ans, i - left + 1)
                total = total - nums[left]
                left += 1

        return 0 if ans == float("inf") else ans