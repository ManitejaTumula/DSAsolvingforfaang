class Solution:
    def sumGame(self, num: str) -> bool:
        n=len(num)
        s1,a1=0,0
        s2,a2=0,0
        for i in range(n):
            if i < n //2:
                if num[i]=='?':a1+=1
                else:s1+=int(num[i])
            else:
                if num[i]=='?':a2+=1
                else:s2+=int(num[i])
        return (a1+a2) % 2==1 or s1-s2!=(a2-a1)//2 * 9

        