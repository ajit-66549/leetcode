class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time complexity: O(n) and Space complexity: O(1)
        if len(prices) <= 1:
            return 0

        answer = 0

        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                answer += (prices[i+1] - prices[i])

        return answer