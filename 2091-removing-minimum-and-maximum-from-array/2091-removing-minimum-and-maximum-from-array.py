class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minim = nums.index(min(nums))
        maxim = nums.index(max(nums))
        left = min(minim, maxim)
        right = max(minim,maxim)
        lef_del=right+1
        rig_del=len(nums)-left
        both=(left+1) + (len(nums)-right)
        return min(lef_del,rig_del,both)


        