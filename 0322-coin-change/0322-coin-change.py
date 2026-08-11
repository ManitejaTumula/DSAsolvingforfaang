class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo={}
        def dfs(rem):
            if rem==0:
                return 0
            if rem < 0:
                return float("inf")
            if rem in memo:
                return memo[rem]
            ans=float("inf")
            for coin in coins:
                ans=min(ans,1+dfs(rem-coin))
                memo[rem]=ans
            return ans
        ans=dfs(amount)
        if ans == float("inf"):
            return -1
        return ans

            