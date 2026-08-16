class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        counter=[0,0,0]
        for stone in stones:
            counter[stone%3]+=1
        c0,c1,c2=counter[0],counter[1],counter[2]

        if c0 % 2 ==0:
            return c1>=1 and c2>=1
        return abs(c1-c2) > 2
        