from functools import lru_cache
from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        n = len(stoneValue)

        @lru_cache(None)
        def dfs(i):
            if i >= n:
                return 0

            best = float("-inf")
            curr = 0

            for k in range(3):
                if i + k < n:
                    curr += stoneValue[i + k]
                    best = max(best, curr - dfs(i + k + 1))

            return best

        ans = dfs(0)

        if ans > 0:
            return "Alice"
        elif ans < 0:
            return "Bob"
        else:
            return "Tie"
        