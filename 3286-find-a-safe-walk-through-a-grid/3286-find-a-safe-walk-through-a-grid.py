import heapq
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        rows=len(grid)
        cols=len(grid[0])
        directions = [
        (1,0),   # down
        (-1,0),  # up
        (0,1),   # right
        (0,-1)   # left
        ]
        if grid[0][0]==1:
            health-=1
        heap=[(-health,0,0)]
        best=[[-1] * cols for _ in range(rows)]
        while heap:
            health,r,c=heapq.heappop(heap)
            health=-health
            if health <= best[r][c]:
                continue
            best[r][c] = health
            if (r,c) == (rows-1,cols-1):
                 return True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                new_health = health - grid[nr][nc]
                if new_health <= 0:
                    continue
                if new_health > best[nr][nc]:
                    heapq.heappush(heap, (-new_health, nr, nc))
        return False

