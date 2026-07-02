from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
      graph=[[] for _ in range(numCourses)]
      indegree = [0]*numCourses

      for course,prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course]+=1
      queue=deque()
      for i in range(numCourses):
        if indegree[i]==0:
            queue.append(i)
      finish=0
      while queue:
        curr=queue.popleft()
        finish+=1
        for course in graph[curr]:
            indegree[course]-=1
            if indegree[course]== 0:
                queue.append(course)
      return finish==numCourses

