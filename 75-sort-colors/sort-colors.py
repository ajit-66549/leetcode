class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Time complexity: O(n) and Space complexity: O(1)
        left = 0
        right = len(nums) - 1
        curr = 0

        while curr <= right:
            if nums[curr] == 0:
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
                curr += 1

            elif nums[curr] == 1:
                curr += 1

            else:
                nums[right], nums[curr] = nums[curr], nums[right]
                right -= 1            