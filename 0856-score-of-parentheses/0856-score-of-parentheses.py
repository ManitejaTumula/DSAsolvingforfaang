class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        d=0
        prev=''
        score=0
        for b in s:
            if b == '(':
                 d+=1
            else: 
                d-=1
            if prev =='(' and b ==')': 
                score+=1 << d
            prev=b
        return score
        

        