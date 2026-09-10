class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        left=max(nums)
        right=sum(nums)
        while left < right:
            mid = left +(right-left)//2
            current_sum=0
            parts=1
            for num in nums:
                if current_sum + num <= mid:
                    current_sum += num
                else:
                    parts += 1
                    current_sum = num
            if parts <=k:
                right=mid
            else:
                left=mid+1
        return left

