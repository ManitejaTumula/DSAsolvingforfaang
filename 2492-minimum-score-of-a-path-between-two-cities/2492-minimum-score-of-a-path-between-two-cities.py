from collections import deque
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph={i:[] for i in range(1,n+1)}
        for u,v,w in roads:
            graph[u].append((v,w))
            graph[v].append((u,w))
        ans=float('inf')
        visited=set()
        q=deque([1])
        visited.add(1)
        while q:
            node=q.popleft()
            for neighbour,weight in graph[node]:
                ans=min(ans,weight)
                if neighbour not in visited:
                    visited.add(neighbour)
                    q.append(neighbour)
        return ans
        
        