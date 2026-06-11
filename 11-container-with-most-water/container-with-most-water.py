class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Time complexity: O(n) and Space complexity: O(1)
        area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            low_height = min(height[left], height[right])
            area = max(area, width*low_height)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area