from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count=Counter(nums)
        memo={}
        max_num=max(nums)
        

        def dfs(num:int):
            if num <=0:
                return 0
            if num in memo:
                return memo[num]
            
            skip=dfs(num-1)
            take= num * count[num] + dfs(num-2)
            memo[num] =max(skip,take)
            return memo[num]

        return dfs(max_num)
        