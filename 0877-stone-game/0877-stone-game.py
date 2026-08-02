class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n=len(piles)
        if n % 2==0:
            return True
        dp= [0] * n
        for i in range(n-1,-1,-1):
            dp[i]=piles[i]
            for j in range(i+1,n):
                dp[j] = max(piles[i] - dp[j], piles[j] -dp[j-1])
        return dp[n-1] >=0
