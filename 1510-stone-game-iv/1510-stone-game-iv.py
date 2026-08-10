class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @cache
        def dp(rem):
            if rem==0:return False
            for a in range(1, int(sqrt(rem))+1):
                if not dp(rem - a **2):return True
            return False
        return dp(n)
        