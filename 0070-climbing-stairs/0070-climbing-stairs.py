class Solution:
        def climbStairs(self, n: int) -> int:
            #Using memoization
            memo=[-1] * (n+1)
            def check(i):
                if i==0 or i==1:
                    return 1
                if memo[i]!=-1:
                    return memo[i]
                memo[i]=check(i-1) + check(i-2)
                return memo[i]
            return check(n)
        