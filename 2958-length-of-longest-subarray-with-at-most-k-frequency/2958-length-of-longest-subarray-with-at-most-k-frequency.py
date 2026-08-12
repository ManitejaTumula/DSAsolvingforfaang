from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        freq=defaultdict(int)
        max_length=0
        n=len(nums)
        left=0

        for right in range(n):
            freq[nums[right]] += 1

            while freq[nums[right]] > k:
                freq[nums[left]]-=1
                left+=1
            max_length =max(max_length,right-left+1)
        return max_length



        