class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        ans=0
        nonzero=False
        for num in nums:
            ans^=num
            if num!=0:
                nonzero=True
        if not nonzero:
            return 0
        return len(nums) if ans!=0 else len(nums)-1
                
        