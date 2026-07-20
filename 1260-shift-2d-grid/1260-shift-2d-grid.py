class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        total = m * n
        ans = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                flat_idx = r * n + c
                new_flat = (flat_idx + k) % total

                new_row = new_flat // n
                new_col = new_flat % n
                ans[new_row][new_col] =grid[r][c]
        return ans
