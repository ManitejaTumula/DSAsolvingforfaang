class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph={i:[] for i in range(numCourses)}
        for course,preq in prerequisites:
            graph[course].append(preq)
        visited=set()
        def dfs(course):
            if course in visited:
                return False
            if graph==[course]:
                return True
            visited.add(course)
            for preq in graph[course]:
                if not dfs(preq): return False
            visited.remove(course)
            graph[course]=[]
            return True
        for course in range(numCourses):
            if not dfs(course):return False
        return True





