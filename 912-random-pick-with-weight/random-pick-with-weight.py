import random

class Solution:
    # Time complexity: O(n + k log n) and Space complexity: O(n) 
    def __init__(self, w: List[int]):
        # Time complexity and Space complexity: O(n)
        self.prefixSum = []
        self.prefixSum.append(w[0])

        for i in range(1, len(w)):
            self.prefixSum.append(self.prefixSum[i-1] + w[i])
        

    def pickIndex(self) -> int:
        # Time complexity: O(log n) and Space complexity: O(1)
        randomNum = random.randint(1, self.prefixSum[-1])
        left = 0
        right = len(self.prefixSum) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if randomNum <= self.prefixSum[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return left
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()