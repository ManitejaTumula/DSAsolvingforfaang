from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count=Counter(nums)
        max_num=max(nums)
        dp=[0] * (max_num+1)
        dp[1] =1 * count[1] 
        for i in range(2,max_num+1):
            skip=dp[i-1]
            take= i * count[i] + dp[i-2]
            dp[i] =max(skip,take)
        return dp[max_num]

        
        