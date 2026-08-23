from collections import deque

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # Time complexity: O(n^3) and Space complexity: O(n^2)
        n = len(bombs)
        graph = [[] for _ in range(n)]

        for i in range(n):
            xi, yi, ri = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                xj, yj, rj = bombs[j]
                distance = ((xj - xi) ** 2) + ((yj - yi) ** 2)
                if distance <= ri ** 2:
                    graph[i].append(j)

        maxBombs = 0  
        for i in range(n):
            queue = deque([i])
            visited = {i}

            while queue:
                removed = queue.popleft()
                for neighbor in graph[removed]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            
            maxBombs = max(maxBombs, len(visited))

        return maxBombs