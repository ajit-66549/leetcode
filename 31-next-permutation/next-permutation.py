class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Time complexity id O(n) and Space complexity: O(1)
        n = len(nums)
        pivot = -1

        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                pivot = i
                break

        if pivot >= 0:
            for i in range(n-1, pivot-1, -1):
                if nums[i] > nums[pivot]:
                    nums[pivot], nums[i] = nums[i], nums[pivot]
                    break

        left = pivot + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1