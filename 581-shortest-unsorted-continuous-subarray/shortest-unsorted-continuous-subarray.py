class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # Time complexity: O(n) and Space complexity: O(1)
        if len(nums) == 1:
            return 0

        left = len(nums) - 1
        right = -1
        max_so_far = -inf

        for i in range(len(nums)):
            if nums[i] >= max_so_far:
                max_so_far = nums[i]
            else:
                right = i

        min_so_far = inf
        for j in range(len(nums)-1, -1, -1):
            if nums[j] <= min_so_far:
                min_so_far = nums[j]
            else:
                left = j

        if right == -1:
            return 0

        return right - left + 1