class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # Time and Space complexity: O(n)
        answer = prices[:]
        stack = []

        for i in range(len(prices)):
            while stack and prices[i] <= prices[stack[-1]]:
                previous_index = stack.pop()
                answer[previous_index] = prices[previous_index] - prices[i]
            stack.append(i)

        return answer