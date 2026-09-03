from collections import defaultdict, deque
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # Time and Space complexity: O(n+m)
        finish = [0] * (n+1)
        indegree = [0] * (n+1)
        graph = defaultdict(list)

        for pre, course in relations:
            indegree[course] += 1
            graph[pre].append(course)

        for course in range(1, n+1):
            finish[course] = time[course-1]

        queue = deque()

        for course in range(1, n+1):
            if indegree[course] == 0:
                queue.append(course)

        while queue:
            pre = queue.popleft()

            for course in graph[pre]:
                finish[course] = max(finish[course], finish[pre]+time[course-1])

                indegree[course] -= 1

                if indegree[course] == 0:
                    queue.append(course)

        return max(finish)