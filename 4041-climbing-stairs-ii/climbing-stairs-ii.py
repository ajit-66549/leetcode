class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # Time complexity: O(n) and Space complexity: O(1)
        one_back = 0
        two_back = float("inf")
        three_back = float("inf")

        for i in range(1, n+1):
            current = costs[i-1] + min(one_back + 1, two_back + 4, three_back + 9)
            three_back, two_back, one_back = two_back, one_back, current

        return one_back