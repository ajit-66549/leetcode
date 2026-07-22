class Solution:
    def jump(self, nums: List[int]) -> int:
        # Time complexity: O(n) and Space complexity: O(1)
        if len(nums) == 1:
            return 0

        farthest = current_end = jumps = 0

        for index in range(len(nums)-1):
            farthest = max(farthest, index+nums[index])

            if index == current_end:
                jumps += 1
                current_end = farthest

                if current_end >= len(nums)-1:
                    return jumps

        return jumps