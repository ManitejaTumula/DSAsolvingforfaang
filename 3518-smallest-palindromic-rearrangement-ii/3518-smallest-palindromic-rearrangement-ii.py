from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        m = n // 2
        
        # Count character frequencies for the left half
        freq = Counter(s[:m])
        INF = 1_000_001
        
        # Helper function to compute the number of unique permutations of remaining characters
        def count_permutations(counts, total_len):
            ways = 1
            curr_len = total_len
            for c in sorted(counts.keys()):
                f = counts[c]
                if f > 0:
                    ways *= comb(curr_len, f)
                    if ways >= INF:
                        return INF
                    curr_len -= f
            return ways

        # Check total possible palindromic rearrangements
        total_ways = count_permutations(freq, m)
        if k > total_ways:
            return ""

        left = []
        rem_len = m
        
        # Construct the left half greedily character by character
        for _ in range(m):
            for c_code in range(26):
                c = chr(ord('a') + c_code)
                if freq[c] > 0:
                    # Try using character c
                    freq[c] -= 1
                    cnt = count_permutations(freq, rem_len - 1)
                    
                    if cnt >= k:
                        left.append(c)
                        rem_len -= 1
                        break
                    else:
                        k -= cnt
                        freq[c] += 1  # Backtrack

        left_str = "".join(left)
        mid_str = s[m] if n % 2 == 1 else ""
        right_str = left_str[::-1]

        return left_str + mid_str + right_str