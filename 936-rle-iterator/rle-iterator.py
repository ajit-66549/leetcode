class RLEIterator:
    # Time complexity: O(n) and Space complexity: O(1)
    def __init__(self, encoding: List[int]):
        self.encoding = encoding

    def next(self, n: int) -> int:
        for i in range(0, len(self.encoding)-1, 2):
            count = self.encoding[i]
            if count == 0:
                continue
            
            if count >= n:
                self.encoding[i] = count - n
                return self.encoding[i+1]
            else:
                n = n - count
                self.encoding[i] = 0
        
        return -1
    
# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)