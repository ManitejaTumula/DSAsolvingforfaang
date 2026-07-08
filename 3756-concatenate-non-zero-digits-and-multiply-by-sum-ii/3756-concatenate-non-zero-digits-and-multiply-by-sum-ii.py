class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD= 10**9 + 7
        num=len(s)

        psum=[0] * num
        pcount=[0] * num
        prefixx=[0] * num

        digit = int(s[0])
        psum[0] = digit
        pcount[0] = 1 if digit !=0 else 0
        prefixx[0] =digit if digit !=0 else 0
        for i in range(1,num):
            digit =int(s[i])
            psum[i]=(psum[i-1] +digit) % MOD
            pcount[i]=pcount[i-1] + (1 if digit!=0 else 0)
            if digit!=0:
                prefixx[i] =(prefixx[i-1] * 10 + digit) % MOD
            else:
                prefixx[i] =prefixx[i-1]
        result=[]
        for l,r in queries:
            sum=(psum[r]-(psum[l-1] if l-1 >=0 else 0)) % MOD
            NZD=pcount[r]-(pcount[l-1] if l-1 >=0 else 0)
            x=(prefixx[r] -(prefixx[l-1] *pow(10,NZD,MOD) if l-1 >=0 else 0)) % MOD
            result.append((x * sum) % MOD)
        return result 


        