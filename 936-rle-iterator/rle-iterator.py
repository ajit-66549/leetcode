class RLEIterator:
    # Time complexity: O(n) and Space complexity: O(1)
    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.index = 0

    def next(self, n: int) -> int:
        while self.index < len(self.encoding)-1:
            count = self.encoding[self.index]

            if count >= n:
                self.encoding[self.index] -= n
                return self.encoding[self.index+1]
            else:
                n -= count
                self.encoding[self.index] = 0
                self.index += 2

        return -1
    
# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)