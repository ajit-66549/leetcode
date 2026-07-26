class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # Time complexity: O(rows × columns) and Space complexity: O(columns)

        if not matrix or not matrix[0]:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        def largest_rectangle_area(heights):
            stack = []
            area = 0

            for i in range(len(heights)+1):
                current = heights[i] if i < len(heights) else 0

                while stack and current < heights[stack[-1]]:
                    index = stack.pop()
                    height = heights[index]
                    
                    if stack:
                        width = i - stack[-1] - 1
                    else:
                        width = i

                    area = max(area, height * width)
                stack.append(i)
                
            return area

        for row in range(len(matrix)):
            for col in range(cols):
                if matrix[row][col] == "1":
                    heights[col] += 1
                else:
                    heights[col] = 0

            current_area = largest_rectangle_area(heights)
            max_area = max(max_area, current_area)

        return max_area