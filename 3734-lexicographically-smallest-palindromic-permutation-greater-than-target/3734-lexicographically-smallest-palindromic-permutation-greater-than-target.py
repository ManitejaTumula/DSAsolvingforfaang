from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = Counter(s)
        
        # Check if a palindrome can be formed
        odd_char = ""
        half_counts = {}
        for char, count in counts.items():
            if count % 2 != 0:
                if odd_char:
                    return ""  # More than 1 odd character
                odd_char = char
            if count // 2 > 0:
                half_counts[char] = count // 2
        
        half_len = n // 2
        
        def build_palindrome(half_str: str) -> str:
            """Constructs the full palindrome from the first half."""
            if n % 2 == 1:
                return half_str + odd_char + half_str[::-1]
            return half_str + half_str[::-1]

        # Try to find the smallest valid first half using backtracking / greedy approach
        # We try prefix matching target's first half from longest to shortest
        
        def find_smallest_greater(prefix_len: int) -> str:
            target_half = target[:half_len]
            curr_counts = half_counts.copy()
            
            # 1. Match prefix of target_half up to prefix_len
            prefix = []
            for i in range(prefix_len):
                char = target_half[i]
                if curr_counts.get(char, 0) <= 0:
                    return ""
                prefix.append(char)
                curr_counts[char] -= 1
            
            # 2. Pick a character at position `prefix_len` strictly greater than target_half[prefix_len]
            # (If prefix_len == half_len, we handle odd middle char comparison separately)
            if prefix_len < half_len:
                target_char = target_half[prefix_len]
                candidates = sorted([c for c in curr_counts if c > target_char and curr_counts[c] > 0])
                
                for next_char in candidates:
                    temp_counts = curr_counts.copy()
                    temp_counts[next_char] -= 1
                    
                    # 3. Fill the remaining half with smallest available characters
                    suffix = []
                    for c in sorted(temp_counts.keys()):
                        suffix.append(c * temp_counts[c])
                    
                    candidate_half = "".join(prefix) + next_char + "".join(suffix)
                    full_pal = build_palindrome(candidate_half)
                    if full_pal > target:
                        return full_pal
            else:
                # prefix_len == half_len: exact match on the first half
                suffix = "".join(prefix)
                full_pal = build_palindrome(suffix)
                if full_pal > target:
                    return full_pal
                    
            return ""

        # Try starting from exact prefix match down to length 0
        for prefix_len in range(half_len, -1, -1):
            res = find_smallest_greater(prefix_len)
            if res:
                return res

        return ""