import math
from functools import lru_cache
from typing import List

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        @lru_cache(None)
        def solve(i, g1, g2):
            # Base Case: processed all elements
            if i == n:
                # Both subsequences must be non-empty and have equal GCD
                return 1 if (g1 == g2 and g1 > 0) else 0
            
            # Choice 1: Skip the current element
            res = solve(i + 1, g1, g2)
            
            # Choice 2: Include nums[i] in the first subsequence
            new_g1 = nums[i] if g1 == 0 else math.gcd(g1, nums[i])
            res = (res + solve(i + 1, new_g1, g2)) % MOD
            
            # Choice 3: Include nums[i] in the second subsequence
            new_g2 = nums[i] if g2 == 0 else math.gcd(g2, nums[i])
            res = (res + solve(i + 1, g1, new_g2)) % MOD
            
            return res
        
        # Start from index 0, with both subsequence GCDs initially 0 (empty)
        return solve(0, 0, 0)