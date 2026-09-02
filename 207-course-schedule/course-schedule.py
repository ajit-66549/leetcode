from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = defaultdict(list)
        answer = []

        for i in range(len(prerequisites)):
            course = prerequisites[i][0]
            pre = prerequisites[i][1]

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
                    
        return len(answer) == numCourses