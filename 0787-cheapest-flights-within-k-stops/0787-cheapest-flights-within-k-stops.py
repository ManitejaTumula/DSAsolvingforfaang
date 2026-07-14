import heapq 
from typing import List
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph={i:[] for i in range(n)}
        for u,v,price in flights:
            graph[u].append((v,price))
        heap=[(0,src,0)] #(cost,node->current,stops)
        minstops=[float('inf')] * n
        while heap:
            cost,node,stops=heapq.heappop(heap)
            if node == dst:
                return cost
            if stops > k:
                continue
            if stops >= minstops[node]:
                continue
            minstops[node] =stops
            for nei,price in graph[node]:
                heapq.heappush(heap,
                (cost+price,nei,stops+1))
        return -1

        