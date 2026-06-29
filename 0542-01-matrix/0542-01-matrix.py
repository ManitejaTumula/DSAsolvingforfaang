from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return mat
        queue=deque()
        rows=len(mat)
        cols=len(mat[0])
        dist = [[-1] * cols for _ in range(rows)]
        directions = [
        (1,0),   # down
        (-1,0),  # up
        (0,1),   # right
        (0,-1)   # left
        ]
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    queue.append((r,c))
        while queue:
            r,c=queue.popleft()
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if nr < 0 or nr>=rows or nc < 0 or nc >=cols:
                    continue
                if dist[nr][nc] ==-1:
                    dist[nr][nc]=dist[r][c] + 1
                    queue.append((nr,nc))
        return dist



        