class Solution:
    def digitSum(self, s: str, k: int) -> str:
        res=[]
        while len(s) > k:
            res=[]
            for i in range(0,len(s),k):
                currsum=0
                for j in range(i,min(i+k,len(s))):
                    currsum+=int(s[j])
                res.append(str(currsum))
            s="".join(res)
        return s

        