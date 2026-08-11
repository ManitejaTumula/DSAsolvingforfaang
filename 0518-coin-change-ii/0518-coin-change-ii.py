class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo={}
        def dfs(i,rem):
            if rem==0:
                return 1
            
            if rem < 0:
                return 0
            
            if i == len(coins):
                return 0
            
            if (i,rem) in memo:
                return memo[(i,rem)]
            
            take = dfs(i, rem - coins[i])
            
            skip = dfs(i + 1, rem)
            
            ans = take + skip
            
            memo[(i,rem)] =ans
            
            return ans
        return dfs(0, amount)
            
        