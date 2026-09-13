from collections import defaultdict
class DetectSquares:
    # Time and Space complexity: O(n)

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        # Time complexity: O(1)
        x, y = point
        self.points[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        # Time complexity: O(n)
        x, y = point
        ans = 0

        for (x1, y1), freq in self.points.items():
            if x1 == x and y1!= y:
                side = abs(y1 - y)

                # Right side square
                new_x = x + side
                ans += (self.points.get((new_x, y1), 0) * self.points.get((new_x, y), 0) * freq)

                # Left side square
                new_x = x - side
                ans += (self.points.get((new_x, y1), 0) * self.points.get((new_x, y), 0) * freq)
        
        return ans


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)