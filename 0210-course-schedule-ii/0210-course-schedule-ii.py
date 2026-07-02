from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=[ [] for _ in range(numCourses)]
        indegree=[0] * numCourses
        for course,preqreq in prerequisites:
            graph[preqreq].append(course)
            indegree[course]+=1
        q=deque()
       
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        finish=0
        order=[]
        while q:
            curr=q.popleft()
            finish+=1
            order.append(curr)
            for course in graph[curr]:
                indegree[course]-=1
                if indegree[course]==0:
                    q.append(course)
        if len(order)==numCourses:
            return order
        return[] 




        