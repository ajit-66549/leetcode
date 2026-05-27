class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Time complexity: O(n) and Space complexity: O(1)
        count_freq = {}
        zero_freq = 0
        result = 0
        left = 0

        for right in range(len(nums)):
            count_freq[nums[right]] = count_freq.get(nums[right], 0) + 1
            zero_freq = count_freq.get(0, 0)

            while zero_freq > k:
                count_freq[nums[left]] -= 1
                left += 1
                zero_freq = count_freq.get(0, 0)

            result = max(result, right - left + 1)
        return result