from sortedcontainers import SortedList
import heapq
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        # Time complexity: O(n log k) and Space complexity: O(k)
        busy = []
        available = SortedList(range(k))
        count = [0] * k

        for i in range(len(arrival)):
            current_time = arrival[i]

            while busy and busy[0][0] <= current_time:
                finish_time, server = heapq.heappop(busy)
                available.add(server)

            if not available:
                continue

            target = i % k
            idx = available.bisect_left(target)

            if idx == len(available):
                idx = 0

            server_id = available[idx]

            available.remove(server_id)
            count[server_id] += 1
            finish_time = load[i] + arrival[i]
            heapq.heappush(busy, (finish_time, server_id))

        max_request = max(count)
        answer = []
        for server, requests in enumerate(count):
            if requests == max_request:
                answer.append(server)

        return answer