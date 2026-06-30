class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count=0
        freq=collections.Counter()
        left=0
        for right in range(len(s)):
            freq[s[right]]+=1
            while freq["a"] > 0 and freq["b"] > 0 and freq["c"] > 0:
                freq[s[left]]-=1
                left+=1
            count+=left
        return count

        