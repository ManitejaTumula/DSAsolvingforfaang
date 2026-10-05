class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        t=n-1
        for i in range(n-1,-1,-1):
            m_jump=nums[i]
            if i+nums[i] >=t:
                t=i
        return t==0




     