from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Time and Space complexity: O(n + m)
        answer = []
        indegree = [0] * numCourses
        graph = defaultdict(list)

        for course, pre in prerequisites:
            indegree[course] += 1
            graph[pre].append(course)

        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        while queue:
            pre = queue.popleft()
            answer.append(pre)

            for course in graph[pre]:
                indegree[course] -= 1

                if indegree[course] == 0:
                    queue.append(course)

        if len(answer) == numCourses:
            return answer
        else:
            return []