from typing import List
import bisect

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        
        # Step 1: Count occurrences of each number in nums
        counts = [0] * (max_val + 1)
        for num in nums:
            counts[num] += 1
            
        # Step 2: Compute how many elements are divisible by each i
        # divisible_cnt[i] stores the count of numbers in nums that are multiples of i
        divisible_cnt = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            for j in range(i, max_val + 1, i):
                divisible_cnt[i] += counts[j]
                
        # Step 3: Use Inclusion-Exclusion to compute exact GCD pair frequencies
        # G[i] will store the exact number of pairs with GCD equal to i
        G = [0] * (max_val + 1)
        for i in range(max_val, 0, -1):
            # Total pairs that have GCD as a multiple of i
            total_pairs = divisible_cnt[i] * (divisible_cnt[i] - 1) // 2
            
            # Subtract pairs that have a strictly larger multiple of i as their GCD
            subtract = 0
            for j in range(2 * i, max_val + 1, i):
                subtract += G[j]
                
            G[i] = total_pairs - subtract
            
        # Step 4: Build a prefix sum array of the frequencies of GCDs
        prefix_sums = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix_sums[i] = prefix_sums[i - 1] + G[i]
            
        # Step 5: Answer each query using binary search
        ans = []
        for q in queries:
            # We look for the first index where cumulative pair count is strictly greater than q
            idx = bisect.bisect_right(prefix_sums, q)
            ans.append(idx)
            
        return ans
        