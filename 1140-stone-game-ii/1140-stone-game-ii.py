class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        
        # Calculate suffix sums so suffix_sum[i] stores sum(piles[i:])
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        memo = {}
        
        def dfs(i: int, M: int) -> int:
            # Base Case: All piles are taken
            if i >= n:
                return 0
            
            # If current player can take all remaining piles, take them all
            if i + 2 * M >= n:
                return suffix_sum[i]
            
            if (i, M) in memo:
                return memo[(i, M)]
            
            max_stones = 0
            
            # Try taking X piles where 1 <= X <= 2M
            for X in range(1, 2 * M + 1):
                # Opponent gets dfs(i + X, max(M, X)) from remaining piles
                opponent_stones = dfs(i + X, max(M, X))
                
                # Current player gets the total remaining minus what opponent gets
                current_stones = suffix_sum[i] - opponent_stones
                max_stones = max(max_stones, current_stones)
                
            memo[(i, M)] = max_stones
            return memo[(i, M)]
            
        return dfs(0, 1)