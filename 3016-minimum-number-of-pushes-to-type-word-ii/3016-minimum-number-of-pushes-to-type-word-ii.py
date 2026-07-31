from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Step 1: Count character frequencies
        counts = Counter(word)
        
        # Step 2: Sort frequencies in descending order
        freqs = sorted(counts.values(), reverse=True)
        
        total_pushes = 0
        
        # Step 3: Accumulate cost based on character rank
        for i, freq in enumerate(freqs):
            multiplier = (i // 8) + 1
            total_pushes += freq * multiplier
            
        return total_pushes