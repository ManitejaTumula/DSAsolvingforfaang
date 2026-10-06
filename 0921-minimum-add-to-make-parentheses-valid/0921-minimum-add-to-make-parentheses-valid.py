class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        d=0
        count=0
        for ch in s:
            if ch=='(':d+=1
            else:
                d-=1
            if d <0:
                count+=1
                d=0
        return count+abs(d)
            
        