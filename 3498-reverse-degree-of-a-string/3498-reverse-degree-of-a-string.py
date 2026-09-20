class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum(
            (ord('z') - ord(char)+ 1) * (i + 1) for i,char in enumerate(s) 
        )
        