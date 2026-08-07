class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def roblinear(arr:List[int]):
            memo={}
            def dfs(i):
                if i >=len(arr):
                    return 0
                if i in memo:
                    return memo[i]
                rob=arr[i] + dfs(i+2)
                skip=dfs(i+1)
                memo[i] =max(rob,skip)
                return memo[i]
            return dfs(0)
        case1=roblinear(nums[:-1])
        case2=roblinear(nums[1:])
        return max(case1,case2)
