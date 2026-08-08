class Solution:
    def trap(self, height: List[int]) -> int:
        # Time complexity: O(n) and Space complexity: O(1)
        leftMax = height[0]
        rightMax = height[-1]
        left = 1
        right = len(height) - 2

        totalWater = 0

        while left <= right:
            if leftMax <= rightMax:
                if height[left] >= leftMax:
                    leftMax = height[left]
                
                totalWater += leftMax - height[left]
                left += 1
            else:
                if height[right] >= rightMax:
                    rightMax = height[right]
                
                totalWater += rightMax - height[right]
                right -= 1

        return totalWater