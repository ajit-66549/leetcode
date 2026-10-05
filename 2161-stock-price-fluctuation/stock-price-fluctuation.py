import heapq
class StockPrice:

    def __init__(self):
        self.records = {}
        self.latest_timestamp = 0

        self.max_heap = []
        self.min_heap = []

    def update(self, timestamp: int, price: int) -> None:
        # Time complexity: O(log u) and Space complexity: O(u)
        if timestamp >= self.latest_timestamp:
            self.latest_timestamp = timestamp
        self.records[timestamp] = price

        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))

    def current(self) -> int:
        # Time complexity: O(1) and Space complexity: O(1)
        return self.records[self.latest_timestamp]

    def maximum(self) -> int:
        # Time complexity: O(1 + klogu) and Space complexity: O(1)
        while self.max_heap:
            neg_price, time = self.max_heap[0]
            price = -neg_price

            dict_price = self.records[time]
            if dict_price != price:
                heapq.heappop(self.max_heap)
            else:
                return price


    def minimum(self) -> int:
        # Time complexity: O(1 + klogu) and Space complexity: O(1)
        while self.min_heap:
            price, time = self.min_heap[0]

            dict_price = self.records[time]
            if dict_price != price:
                heapq.heappop(self.min_heap)
            else:
                return price


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()