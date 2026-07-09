import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows=len(heights)
        cols=len(heights[0])
        minheap=[[0,0,0]] # [diff,r,c]
        visit=set()
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        while minheap:
            diff,r,c=heapq.heappop(minheap)

            if (r,c) in visit:
                continue
            visit.add((r,c))
            if (r,c) ==(rows-1,cols-1):
                return diff

            for dr,dc in directions:
                newR,newC=r+dr,c+dc
                if (newR < 0 or newC < 0 or newR==rows or newC==cols or (newR,newC) in visit):
                    continue
                newdiff = max(diff,abs(heights[r][c] - heights[newR][newC]))
                heapq.heappush(minheap,[newdiff,newR,newC])
            


        