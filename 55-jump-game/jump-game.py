class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Time complexity: O(n) and Space complexity: O(1)
        farthest = 0

        for i in range(len(nums)):
            if i > farthest:
                return False
            
            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1:
                return True

        return True