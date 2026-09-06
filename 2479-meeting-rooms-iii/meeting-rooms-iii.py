import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Time complexity: O(m log m) + O(m log n) and Space complexity: O(n)
        available = list(range(n))
        heapq.heapify(available)
        count = [0] * n

        busy = []
        meetings.sort()

        for meeting in meetings:
            start = meeting[0]
            end = meeting[1]

            while busy and busy[0][0] <= start:
                finish, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                count[room] += 1
                heapq.heappush(busy, (end, room))
            else:
                finish, room = heapq.heappop(busy)
                count[room] += 1
                heapq.heappush(busy, (finish + end - start, room))

        maximum = max(count)
        for i in range(n):
            if count[i] == maximum:
                return i