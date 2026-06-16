class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Time complexity: O(log n) and Space complexity: O(1)
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2
            
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        return -1