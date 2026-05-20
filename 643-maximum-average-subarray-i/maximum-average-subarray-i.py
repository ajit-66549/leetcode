class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Time complexity: O(n) and Space complexity: O(1)

        window_sum = sum(nums[:k])
        max_avg = window_sum / k

        for right in range(k, len(nums)):
            window_sum = window_sum + nums[right] - nums[right - k]
            max_avg = max(max_avg, window_sum / k)
        return max_avg