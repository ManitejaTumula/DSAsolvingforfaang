from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        queue=deque()
        fresh=0
        time=0
        directions = [
        (1, 0),   # down
        (-1, 0),  # up
        (0, 1),   # right
        (0, -1)   # left
        ]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh+=1
        while queue and fresh > 0:
            size =len(queue)
            for _ in range(size):
                r,c=queue.popleft()
                for dr,dc in directions:
                    nr=r+dr
                    nc=c+dc
                    if nr < 0 or nr>=rows or nc < 0 or nc>=cols or grid[nr][nc]!=1:
                        continue
                    grid[nr][nc] = 2
                    queue.append([nr,nc])
                    fresh-=1
            time+=1
        return time if fresh==0 else -1


    


        