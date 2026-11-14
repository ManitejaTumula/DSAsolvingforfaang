class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum=float("inf")
        for k in range(l,r+1):
            curr_sum=sum(nums[:k])
            if curr_sum >0:
                min_sum=min(min_sum,curr_sum)
            for i in range(k,len(nums)):
                curr_sum+=nums[i]-nums[i-k]
                if curr_sum>0:
                    min_sum=min(min_sum,curr_sum)
        return -1 if min_sum == float("inf") else min_sum