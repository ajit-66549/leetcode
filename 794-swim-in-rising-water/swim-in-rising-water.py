import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Time complexity: O(n^2 log(n)) and Space complexity: O(n^2)
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        heapq.heapify(heap)

        visited = set()

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while heap:
            time, row, col = heapq.heappop(heap)

            if (row, col) in visited:
                continue

            if (row, col) == (n-1, n-1):
                return time

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if (0 <= new_row < n) and (0 <= new_col < n):
                    if (new_row, new_col) not in visited:
                        new_time = max(time, grid[new_row][new_col])
                        heapq.heappush(heap, (new_time, new_row, new_col))

            visited.add((row, col))