class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        first=nums[-1] * nums[-2] * nums[-3]
        second=nums[0] * nums[1] * nums[-1]
        return max(first,second)
        