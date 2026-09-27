class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjLst = { i: [] for i in range(numCourses)}
        for bundle in prerequisites:
            course, prereq = bundle
            adjLst[course].append(prereq)
        
        indegrees = [0] * numCourses
        for i in range(numCourses):
            for neigh in adjLst[i]:
                indegrees[neigh] += 1

        queue = deque()
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i)
        
        while queue:
            course = queue.popleft()
            for neig in adjLst[course]:
                indegrees[neig] -= 1
                if indegrees[neig] == 0:
                    queue.append(neig)

        for i in range(numCourses):
            if indegrees[i] != 0:
                return False
        return True