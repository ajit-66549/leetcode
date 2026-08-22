class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # Time complexity: O(m * n) and Space complexity: O(n)
        prev = points[0]

        for r in range(1, len(points)):
            curr = [0] * len(prev)

            bestLeft = prev[0] + 0
            for c in range(len(prev)):
                bestLeft = max(bestLeft, prev[c] + c)
                curr[c] = points[r][c] + bestLeft - c

            bestRight = prev[-1] - (len(prev) - 1)
            for c in range(len(prev)-1, -1, -1):
                bestRight = max(bestRight, prev[c] - c)
                curr[c] = max(curr[c], points[r][c] + bestRight + c)

            prev = curr

        return max(prev)