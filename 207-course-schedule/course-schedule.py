from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Time and Space complexity: O(n+m) where n = numCourses and m = len(prerequisites)
        indegree = [0] * numCourses
        graph = defaultdict(list)

        answer = []

        for course, pre in prerequisites:
            indegree[course] += 1
            graph[pre].append(course)

        queue = deque()  # queue holds the courses which can be taken

        # take the courses which has 0 prerequisites and add in queue
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        while queue:  # process the course as it can be pre of other course
            pre = queue.popleft()
            answer.append(pre)

            # get the courses depended on this 
            courses = graph[pre]
            for course in courses:
                indegree[course] -= 1

                if indegree[course] == 0: # this course can be taken, so add in queue
                    queue.append(course)

        return len(answer) == numCourses