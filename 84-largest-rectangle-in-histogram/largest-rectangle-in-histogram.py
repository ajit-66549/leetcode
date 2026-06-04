class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Time and Space complexity: O(n)
        maxArea = 0
        stack = []

        for i in range(len(heights) + 1):
            current_height  = heights[i] if i < len(heights) else 0

            while stack and current_height < heights[stack[-1]]:
                height_index = stack.pop()
                height = heights[height_index]
                left_boundry = stack[-1] if stack else -1
                width = i - left_boundry - 1
                maxArea = max(maxArea, height * width)

            stack.append(i)
        return maxArea