class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n =len(s)
        if n < k:
            return ""
        ones=0
        left =0
        ans=""
        for right in range(n):
            if s[right] == '1':
                ones+=1
            while ones == k:
                sub =s[left:right+1]
                if not ans or len(sub) < len(ans) or (len(sub) == len(ans) and sub < ans):
                    ans = sub
                
                if s[left] == '1':
                    ones -= 1
                left += 1
        return ans


        
        