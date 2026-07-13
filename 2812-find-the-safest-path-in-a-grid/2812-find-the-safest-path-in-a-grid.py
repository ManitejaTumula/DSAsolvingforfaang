from collections import deque
import heapq
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        if grid[0][0]==1 or grid[-1][-1]==1: return 0
        dist=[[-1] * cols for _ in range(rows)]
        queue =deque()
        directions = [
        (1,0),   # down
        (-1,0),  # up
        (0,1),   # right
        (0,-1)   # left
        ]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dist[r][c] =0
                    queue.append((r,c))
        while queue:
            r,c=queue.popleft()

            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if nr < 0 or nr>=rows or nc < 0 or nc >=cols:
                    continue
                if dist[nr][nc] == -1:
                    dist[nr][nc]=dist[r][c]+1
                    queue.append((nr,nc))

        heap=[(-dist[0][0],0,0)]
        visit=set()
        while heap:
            safe,r,c=heapq.heappop(heap)
            safe=-safe
            if (r,c) in visit:
                continue
            if (r, c) == (rows - 1, cols - 1):
                return safe
            visit.add((r,c))                
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if (nr < 0 or nr>=rows or nc < 0 or nc >=cols or (nr,nc) in visit):
                    continue
                
                safepath=min(safe,dist[nr][nc])
                heapq.heappush(heap,(-safepath,nr,nc))

