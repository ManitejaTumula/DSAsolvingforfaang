import math
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        
        # Helper function using Inclusion-Exclusion Principle
        def count_amounts(x: int) -> int:
            total = 0
            # Iterate through all non-empty subsets using bitmasking
            for mask in range(1, 1 << n):
                lcm_val = 1
                bits_set = 0
                for i in range(n):
                    if (mask >> i) & 1:
                        bits_set += 1
                        lcm_val = math.lcm(lcm_val, coins[i])
                        if lcm_val > x:  # Early pruning
                            break
                
                if lcm_val <= x:
                    terms = x // lcm_val
                    if bits_set % 2 == 1:
                        total += terms
                    else:
                        total -= terms
            return total

        # Binary search for the answer
        left = 1
        right = min(coins) * k
        ans = right

        while left <= right:
            mid = (left + right) // 2
            if count_amounts(mid) >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans