class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjLst = { i: [] for i in range(numCourses)}
        for bundle in prerequisites:
            course, prereq = bundle
            adjLst[course].append(prereq)
        
        # solution using dfs cycle detection
        path = set()

        def dfs(course):
            if course in path:
                return False
            path.add(course)
            
            for neig in adjLst[course]:
                if not dfs(neig):
                    return False
            path.remove(course)
            adjLst[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True