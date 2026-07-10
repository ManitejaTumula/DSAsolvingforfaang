import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
         rows=len(grid)
         cols=len(grid[0])
         swimheap=[[grid[0][0],0,0]] #time,r,c
         directions=[[1,0],[0,-1],[0,1],[-1,0]]
         visit=set()
         while swimheap:
            time,r,c=heapq.heappop(swimheap)
            if (r,c) in visit:
                continue
            visit.add((r,c))
            if (r,c) ==(rows-1,cols-1):
                return time
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if(nr< 0 or nr >=rows or nc< 0 or nc >=cols or (nr,nc) in visit):
                    continue
                timechange=max(time,grid[nr][nc])
                heapq.heappush(swimheap,[timechange,nr,nc])
